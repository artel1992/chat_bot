from django.db import models
from django.contrib.auth.models import User

class Rooms(models.Model):
    creater = models.ForeignKey(User,verbose_name='Создатель',on_delete=models.CASCADE)
    invited = models.ManyToManyField(User,verbose_name='Гость',related_name="invited_user")
    date = models.DateField("Дата создания",auto_now_add=True)
    class Meta:
        verbose_name = 'Комната чата'
        verbose_name_plural = 'Комната чата'


class Chat(models.Model):
    room = models.ForeignKey(Rooms,verbose_name="Комната Чата",on_delete=models.CASCADE)
    user = models.ForeignKey(User,verbose_name="Пользователь", on_delete=models.CASCADE)
    text = models.TextField('Сообщение', max_length=500)
    date = models.DateTimeField('Дата отправкт', auto_now_add=True)