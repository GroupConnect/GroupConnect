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
    plan_mail_time = models.TimeField(db_column='plan_time')
    new_mail_stop_time = models.DateTimeField(db_column='mail_stop_time')
    new_mail_start_time = models.DateTimeField(db_column='mail_start_time')
    notice_signboard = models.BooleanField(db_column='notice_signboard')
    notice_chat = models.BooleanField(db_column='notice_chat')
    notice_calendar = models.BooleanField(db_column='notice_calendar')
    notice_group = models.BooleanField(db_column='notice_group')

class Group(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    group_name = models.CharField(max_length=100, db_column='group_name')
    icon = models.ImageField(upload_to='static/images/', db_column='icon', blank=True, null=True)
    create_date = models.DateTimeField(db_column='create_date')

class Member(models.Model):
    account_id = models.IntegerField(db_column='account_id')
    group_id = models.IntegerField(db_column='group_id')
    name = models.CharField(max_length=100, db_column='name')
    authority = models.BooleanField(db_column='authority')

class Signboard(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    group_id = models.IntegerField(db_column='group_id')
    title = models.CharField(max_length=100, db_column='title')
    category = models.CharField(max_length=100, db_column='category')
    text = models.TextField(db_column='text')

class Post(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    signboard_id = models.IntegerField(db_column='signboard_id')
    text = models.TextField(db_column='text')
    contributer = models.CharField(max_length=100, db_column='contributer')
    posted = models.DateTimeField(db_column='posted')
    read_number = models.IntegerField(db_column='read_number')

class Situation(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    post_id = models.IntegerField(db_column='post_id')
    account_id = models.IntegerField(db_column='account_id')
    read_situation = models.CharField(max_length=10, db_column='read_situation')

class Calendar(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    group_id = models.IntegerField(db_column='group_id')
    event_list = models.IntegerField(db_column='event_list')
    updated_at = models.DateTimeField(db_column='updated_at')
    delete_at = models.DateTimeField(default="None", db_column='delete_at')

class Event(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    title = models.CharField(max_length=100, db_column='title')
    description = models.CharField(default="None", max_length=100, db_column='description')
    date_time = models.DateTimeField(db_column='date_time')
    all_day = models.BooleanField(db_column='all_day')
    repeat = models.CharField(max_length=100, db_column='repeat')
    place = models.CharField(max_length=100, default="None", db_column='place')
    notice = models.CharField(max_length=100, default="None", db_column='notice')
    release = models.BooleanField(default="None", db_column='release')
    scheduled = models.BooleanField(db_column='scheduled')
    add_guest = models.TextField(db_column='add_guest')
    authority_guest = models.BooleanField(db_column='authority_guest')
    created_at = models.DateTimeField(db_column='created_at')
    updated_at = models.DateTimeField(db_column='updated_at')
    deleted_at = models.DateTimeField(default="None", db_column='deleted_at')

class File(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    group_id = models.IntegerField(db_column='group_id')
    file_name = models.CharField(default="None", max_length=100, db_column='file_name')
    file_path = models.CharField(max_length=100, db_column='file_path')
    folder_id = models.IntegerField(default="None", db_column='folder_id')
    create_at = models.DateTimeField(db_column='create_at')
    delete_at = models.DateTimeField(default="None", db_column='delete_at')

class Folder(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=100, db_column='name')
    created_at = models.DateTimeField(db_column='created_at')

class Chat(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    sender_id = models.IntegerField(db_column='sender_id')
    receiver_id = models.IntegerField(db_column='receiver_id')
    updated_at = models.DateTimeField(db_column='updated_at')
    deleted_at = models.DateTimeField(default="None", db_column='deleted_at')

class Talk(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    chat_id = models.IntegerField(db_column='chat_id')
    text = models.TextField(db_column='text')
    create_at = models.DateTimeField(db_column='create_at')
    delete_at = models.DateTimeField(default="None", db_column='delete_at')










