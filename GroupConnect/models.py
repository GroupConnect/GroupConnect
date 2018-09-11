from django.db import models

# Create your models here.

class Account(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=100, db_column='name')
    rome_name = models.CharField(max_length=100, db_column='rome_name', blank=True, null=True)
    mail_address = models.EmailField(db_column='mail_address')
    password = models.CharField(max_length=250, db_column='password')
    icon = models.ImageField(upload_to='static/images/', db_column='icon', blank=True, null=True)
    introduction = models.TextField(db_column='introduction', blank=True, null=True)
    plan_mail_address = models.EmailField(db_column='plan_address', blank=True, null=True)
    plan_mail_time = models.TimeField(db_column='plan_time')
    new_mail_address = models.EmailField(db_column='new_address', blank=True, null=True)
    new_mail_stop_time = models.DateTimeField(db_column='mail_stop_time')
    new_mail_start_time = models.DateTimeField(db_column='mail_start_time')
    # notice_signboard = models.BooleanField(db_column='notice_signboard')
    # notice_chat = models.BooleanField(db_column='notice_chat')
    # notice_calendar = models.BooleanField(db_column='notice_calendar')
    # notice_group = models.BooleanField(db_column='notice_group')
