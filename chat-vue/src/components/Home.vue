<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="primary">
  Чат на vue js
  <mu-button v-if="!auth" @click="goLogin()" flat slot="right">LOGIN</mu-button>
  <mu-button v-else @click="loggout " flat slot="right">LOGOUT</mu-button>
</mu-appbar>

        <mu-row>
            <Room v-if="auth" @openChat="openChat"></Room>
            <Chat v-if="chat.show" :id="chat.id"></Chat>
        </mu-row>
    </mu-container>
</template>

<script>
    import Room from '@/components/Rooms/Room'
    import Chat from '@/components/Rooms/Chat'
    export default {
        name: "Home",
        data(){
          return {
              chat: {
                    id: '',
                    show: false
                }
          }
        },
        methods:{
            goLogin(){
                return this.$router.push({name:'login'})
            },
            loggout(){
                sessionStorage.removeItem("auth_token")
                window.location='/'
            },
            openChat(room_id){
                this.chat.show=true
                this.chat.id=room_id
            }
        },
        components:{
            Room,Chat
        },
        computed:{
            auth(){
                if(sessionStorage.getItem('auth_token')){
                    return true
                }
            }
        }
    }
</script>

<style scoped>

</style>