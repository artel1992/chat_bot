<template>
    <mu-col span="4" sm="4" xl="2" class="rooms-list">
        <div v-for="room in rooms">
            <h2 @click="openChat(room.id)">{{room.creater.username}}</h2>
            <small>{{room.date}}</small>
        </div>
    </mu-col>
</template>

<script>
    export default {
        name: "Room",
        data() {
            return {
                rooms: '',

            }
        },
        created() {
            $.ajaxSetup({
                headers: {
                    "Authorization": 'Token ' + sessionStorage.getItem("auth_token")
                }
            });
            this.loadRoom()
        },

        methods: {
            loadRoom() {
                $.ajax({
                    url: 'http://127.0.0.1:8011/api/v1/chat/room',
                    type: 'GET',
                    success: (response) => {
                        this.rooms = response.data.data;
                    }
                })

            },
            openChat(room_id) {
                this.$emit("openChat",room_id)
                // this.chat.id = room_id;
                // this.chat.show = true;
            }
        }
    }
</script>

<style scoped>
    h3 {
    cursor:pointer;
    }
    .rooms-list{
        box-shadow:1px 2px 3px #909cb2;
    }
</style>