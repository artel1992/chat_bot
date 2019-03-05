<template>
    <div>
        <h1>Chat на vue js 1</h1>
        <button @click="goLogin()">Login</button>

    </div>
</template>

<script>
    export default {
        name: "Home",
        methods:{
            goLogin(){
                return this.$router.push({name:'login'})
            }
        }
    }
</script>

<style scoped>

</style>