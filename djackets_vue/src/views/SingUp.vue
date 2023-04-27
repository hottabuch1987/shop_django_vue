<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Регистрация</h1>
                <form @submit.prevent="submiForm">
                    <!-- username -->
                    <div class="field">
                        <label>Имя пользователя</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>
                    <!-- password -->
                    <div class="field">
                        <label>Пароль</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>
                     <!-- password 2 -->
                    <div class="field">
                        <label>Повтор пароля</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>
                    <!-- errors -->
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{error}}</p>
                    </div>
                    <!-- button -->
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Зарегистрироваться</button>
                        </div>
                        <hr>
                         <router-link to="/log-in">Войти</router-link>
                    </div>
                </form>
            </div>
        </div>
        
    </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
    name:"SingUp",
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Регистрация | mobile'
    },
    methods: {
        submiForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('Имя пользователя не должно быть пустым')
            }
           
            if (this.password !== this.password2) {
                this.errors.push('Пароли не совпадают')
            }
           
            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }
                axios
                    .post('api/v1/users/', formData)
                    .then(response =>{
                        toast ({
                            message: 'Аккаунт создан, пожалуйста войдите!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: 2000,
                            position: 'bottom-right'
                        })
                        this.$router.push('/log-in')
                    })
                    .catch(error =>{
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.error.push('Что-то пошло не так. Пожалуйста попробуйте еще раз!')

                            console.log(JSON.stringify[error])
                        }
                    })
            }
        }
    },


}
</script>