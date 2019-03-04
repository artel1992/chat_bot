from django.urls import path
from chat_room.views import *
urlpatterns =[
    path('room/',Room.as_view()),
    path('chat/',ChatViews.as_view())
]