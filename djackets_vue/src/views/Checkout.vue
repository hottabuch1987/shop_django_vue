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
                <p class="has-text=grey mb-4">Все поля обязательны для заполнения</p>
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
            addres: '',
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