from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from chat_room.models import Rooms,Chat
from chat_room.serialsers import RoomSerializers,ChatSerializers

class Room(APIView):
    def get(self,request):
        rooms = Rooms.objects.all()
        serializer = RoomSerializers(rooms,many=True)
        return Response({"data":serializer.data})

class ChatViews(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    def get(self,request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({'data':serializer.data})
    def post(self,request):
        room = request.data.get("room")
