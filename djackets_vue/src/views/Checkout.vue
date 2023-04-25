<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Расчетный счет</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Продукт</th>
                            <th>Цена</th>
                            <th>Количество</th>
                            <th>Общая стоимость</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="item in cart.items"
                            v-bind:key=item.product.id
                        >
                            <td>{{ item.product.name}}</td>
                            <td>${{ item.product.price}}</td>
                            <td>{{ item.quantity}}</td>
                            <td>${{ getItemTotal(item).toFixed(2)}}</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="2">К оплате:</td>
                            <td>{{cartTotalLength}}</td>
                            <td>${{cartTotalPrice.toFixed(2)}}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <div class="column is-12 box">
                <h2 class="subtitle">Оформление покупки</h2>
                
                <p class="has-text=grey mb-4">Все поля обязательны для заполнения*</p>
                
                <div class="columns is-multiline">
            <!-- form -->
                    <div class="column is-6">

                        <div class="field">
                            <label>Имя*</label>
                            <div class="contol">
                                <input type="text" class='input' v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Фамилия*</label>
                            <div class="contol">
                                <input type="text" class='input' v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Email*</label>
                            <div class="contol">
                                <input type="email" class='input' v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Телефон*</label>
                            <div class="contol">
                                <input type="text" class='input' v-model="phone">
                            </div>
                        </div>
                    </div>
            <!--  -->
                    <div class="column is-6">

                            <div class="field">
                                <label>Адрес*</label>
                                <div class="contol">
                                    <input type="text" class='input' v-model="address">
                                </div>
                            </div>

                            <div class="field">
                                <label>Почтовый индекс*</label>
                                <div class="contol">
                                    <input type="text" class='input' v-model="zipcode">
                                </div>
                            </div>

                            <div class="field">
                                <label>Место*</label>
                                <div class="contol">
                                    <input type="text" class='input' v-model="place">
                                </div>
                            </div>        
                    </div>
                </div>
            <!--  endform -->
                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{error}}</p>
                </div>
                <hr>

                <div id="card-element" class="mb-5"></div>
                <template v-if="cartTotalLength">
                    <hr>

                    <button class="button is-dark" @click="submitForm">Оплатить картой</button>
                </template>   

               
            </div>
        </div>
    </div>
</template>

<script>
import axios from'axios'

export default {
    name: "Checkout",
    data(){
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Cчет | mobile'

        this.cart = this.$store.state.cart

        if (this.cartTotalLength > 0) {
            this.stripe = Stripe('pk_test_51H1HiuKBJV2qfWbD2gQe6aqanfw6Eyul5PO2KeOuSRlUMuaV4TxEtaQyzr9DbLITSZweL7XjK3p74swcGYrE2qEX00Hz7GmhMI')
            const elements = this.stripe.elements()
            this.card = elements.create('card', {hidePostalCode: true})

            this.card.mount('#card-element')
        }
    },
    methods: {
        getItemTotal(item){
            return item.quantity * item.product.price
        },
        submitForm() {
            this.errors = []
            if (this.first_name === '') {
                    this.errors.push('поле "имя" отсутствует!')
            }
            if (this.last_name === '') {
                    this.errors.push('поле "фамилия" отсутствует!')
                }
            if (this.email === '') {
                    this.errors.push('поле "email" отсутствует!')
            }
            if (this.phone === '') {
                    this.errors.push('поле "телефон" отсутствует!')
            }
            if (this.address === '') {
                    this.errors.push('поле "адрес" отсутствует!')
            }
            if (this.zipcode === '') {
                    this.errors.push('поле "индекс" отсутствует!')
            }
            if (this.place === '') {
                    this.errors.push('поле "место" отсутствует!')
            }
            if (!this.errors.length) {
                    this.$store.commit('setIsLoading', true)

                    this.stripe.createToken(this.card).then(result => {
                        if (result.error) {
                            this.$store.commit('setIsLoading', false)

                            this.errors.push('Что то пошло не так, попробуйте еще раз')
                            
                            console.log(result.error.message)
                        } else {
                            this.stripeTokenHandler(result.token)
                        }
                    })
                }
        },
        async stripeTokenHandler(token) {
            const items = []

            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price * item.quantity
                }
                items.push(obj)
            }

            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'address': this.address,
                'zipcode': this.zipcode,
                'place': this.place,
                'items': items,
                'stripe_token': token.id
            }

            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                })
                .catch(error => {
                    this.errors.push('Что-то пошло не так. Пожалуйста попробуйте еще раз')
                    console.log(error)
                })
                this.$store.commit('setLoading', false)

        }

    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
        
    }
}
</script>