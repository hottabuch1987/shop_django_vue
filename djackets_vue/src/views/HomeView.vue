<template>
<div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">Добро пожаловать в mobile - shop</p>
            <p class="subtitle">Лучший интернет-магазин телефонов</p>
        </div>
    </section>
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">Последние продукты</h2>
            </div>
            
            <ProductBox 
                v-for="product in latestProducts"
                v-bind:key="product.id"
                v-bind:product="product"
            />
            
        </div>
 </div>

</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'



export default {
  name: 'HomeView',
  components: { ProductBox },
 
  data() {
    return {
        latestProducts: []
    }
  },
  mounted() {
    this.getLatestProducts()

    document.title =  'Главная | mobile'   
  },
  methods: {
    async getLatestProducts(){
        this.$store.commit('setIsLoading', true)
        
        await axios
            .get('/api/v1/latest-products/')
            .then(response => {
                this.latestProducts = response.data
            })
            .catch(error =>{
                console.log(error)
            })
        this.$store.commit('setIsLoading', false)
    }
  },
  

}
</script>


