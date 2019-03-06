<template>
    <div>
        <input v-model="login" placeholder="Login" type="text">
        <input v-model="password" placeholder="Password" type="password">
        <button @click="setLogin">Войти</button>
        <hr>
        {{login}}:{{password}}
    </div>
</template>

<script>
    export default {
        name: "Login",
        data(){
            return{
                login:'',
                password:''
            }
        },
        methods:{
            setLogin(){
                $.ajax({
                    url:'http://127.0.0.1:8011/auth/token/create/',
                    type:'POST',
                    data:{
                        username:this.login,
                        password: this.password
                    },
                    success:(response) =>{
                        alert('Вход выполнен успешно');
                        sessionStorage.setItem('auth_token',response.data.attributes.auth_token);
                        this.$router.push({name:'home'})
                    },
                    error:(response) =>{
                        if (response.status == 400) {
                            console.log(response)
                            alert('Неверный логин либо пароль')
                        }
                    }
                });
            }
        }


    }
</script>

<style scoped>

</style>