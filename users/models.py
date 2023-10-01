from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    # One-To-One Model : User 모델에 일대일로 연결되는 새로운 모델을 생성
    #  on_delete = models.CASCADE : 모델에서 데이터가 삭제될 때 연결된 데이터를 함께 삭제함
    nickname = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    subjects = models.CharField(max_length=128)
    image = models.ImageField(upload_to = 'profile/', default='default.png')


@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs): 
    # User 모델이 post_save E를 발생시키면 해당 유저 인스턴스와 연결되는 프로필 데이터를 생성
    if created:
        Profile.objects.create(user = instance)





