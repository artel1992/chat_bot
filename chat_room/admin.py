from django.contrib import admin
from chat_room.models import Rooms,Chat



class RoomAdmin(admin.ModelAdmin):
    list_display = ('creater','invited_user','date')
    def invited_user(self,obj):
        return "\n".join([user.username for user in obj.invited.all()])

class ChatAdmin(admin.ModelAdmin):
    list_display =('room', 'user', 'date','text')

admin.site.register(Rooms,RoomAdmin)
admin.site.register(Chat,ChatAdmin)
