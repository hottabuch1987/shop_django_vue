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
            <!--  endform -->
                    <div class="notification is-danger mt-4" v-if="errors.length">
                            <p v-for="error in erros" v-bind:key="error">{{error}}</p>
                    </div>
                    <hr>

                    <div id="card-element" class="mb-5"></div>
                    <templete v-if="cartTotalLength">
                        <hr>

                        <button class="button is-dark" @click="submitForm">Оплатить картой</button>
                    </templete>   

                </div>
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
        document.titile = 'Cчет | mobile'

        this.cart = this.$store.state.cart
    },
    methods: {
        getItemTotal(item){
            return item.quantity * item.product.price
        },
        submitForm() {
        }

    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
    }
}
</script>