from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name='手机号码')

    class Meta:
        db_table = 'hippo_user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
