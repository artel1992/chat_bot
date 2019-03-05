from rest_framework import serializers
from chat_room.models import Rooms,Chat
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = User
        fields = ('id','username')

class RoomSerializers(serializers.ModelSerializer):
    """Сериализация комнат"""
    """Сериализация комнат"""
    creater = UserSerializer()
    invited = UserSerializer(many=True)
    class Meta:
        model = Rooms
        fields = ('creater','invited','date')
class ChatSerializers(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Chat
        fields = ('user', 'date','text')


class ChatSerializersPOST(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('text','room')

