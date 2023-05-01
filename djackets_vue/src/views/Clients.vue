<template>
<div class="page-my-account">
    <div class="columns is-multiline" v-for="client in getClients" :key="client.id">
        <div class="column is-12">{{client.id}}
        </div>
    </div>
</div>
</template>
/api/v1/users/
<script>
import axios from "axios";
export default{
    name: "Clients",
    data() {
        return {
            getClients: []
        }
    },
    mounted() {
        this.getLatestClients()

        document.title =  'Клиенты | mobile'   
    },
    methods: {
    async getLatestClients(){
        this.$store.commit('setIsLoading', true)
        
        await axios
            .get('/api/v1/users/')
            .then(response => {
                this.getClients = response.data
            })
            .catch(error =>{
                console.log(error)
            })
        this.$store.commit('setIsLoading', false)
    }
  },
}
</script>
