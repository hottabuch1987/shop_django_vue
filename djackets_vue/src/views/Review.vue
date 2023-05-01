<template>
<div class="column is-12">
    <h2 class="is-size-2 has-text-centered">Оцените нашу работу</h2>
         <StarRating  />
    
</div>
    
</template>
<script>
import StarRating from '@/components/StarRating'

export default {
    name: 'Review',
    components: {StarRating},

    
}
</script>
