<template>
    <mu-col span="8" sm="8" xl="10">
        <mu-container class="bordered">
            <mu-row v-for="chat in chats" direction="column" justify-content="start" align-items="end">
                <p><strong>{{chat.user.username}}</strong></p>
                <hr>
                <p>{{chat.text}}</p>
                <small>{{chat.date}}</small>
            </mu-row>
        </mu-container>
        <mu-container>
            <mu-flex justify-content="center" align-items="center">
                <mu-text-field class="fullwidth" placeholder="Сообщение" multi-line :rows="3" :rows-max="6"
                               v-model="form.textarea"></mu-text-field>
            </mu-flex>
            <mu-flex justify-content="center" align-items="center">
                <mu-button full-width color="primary">Отправить</mu-button>
            </mu-flex>
        </mu-container>

    </mu-col>
</template>

<script>
    export default {
        name: "Chat",
        props: {"id": ''},
        data() {
            return {
                chats: '',
                form: {
                    textarea: '',
                }
            }
        },
        created() {
            this.loadChat()
        },
        methods: {
            loadChat() {
                $.ajax({
                    url: 'http://127.0.0.1:8011/api/v1/chat/chat/',
                    type: 'GET',
                    data: {
                        room: this.id,
                    },
                    success: (response) => {
                        this.chats = response.data.data
                    },
                    error: (response) => {
                        if (response.status == 400) {
                            console.log(response)
                            alert('Неверный логин либо пароль')
                        }
                    }
                })
            },

        }
    }
</script>

<style scoped>
    .fullwidth{
        width: 100%;
    }
    .bordered {
        border: 1px solid cadetblue;
    }
</style>