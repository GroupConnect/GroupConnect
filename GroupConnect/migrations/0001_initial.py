# Generated by Django 2.1 on 2019-02-08 01:19

import GroupConnect.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('group_id', models.IntegerField(db_column='group_id')),
                ('event_list', models.IntegerField(db_column='event_list')),
                ('updated_at', models.DateTimeField(db_column='updated_at')),
                ('delete_at', models.DateTimeField(db_column='delete_at', default='None')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=100, verbose_name='カテゴリー名')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('sender_id', models.IntegerField(db_column='sender_id')),
                ('receiver_id', models.IntegerField(db_column='receiver_id')),
                ('updated_at', models.DateTimeField(db_column='updated_at')),
                ('deleted_at', models.DateTimeField(db_column='deleted_at', default='None')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='title', max_length=100)),
                ('description', models.CharField(db_column='description', default='None', max_length=100)),
                ('date_time', models.DateTimeField(db_column='date_time')),
                ('all_day', models.BooleanField(db_column='all_day')),
                ('repeat', models.CharField(db_column='repeat', max_length=100)),
                ('place', models.CharField(db_column='place', default='None', max_length=100)),
                ('notice', models.CharField(db_column='notice', default='None', max_length=100)),
                ('release', models.BooleanField(db_column='release', default='None')),
                ('scheduled', models.BooleanField(db_column='scheduled')),
                ('add_guest', models.TextField(db_column='add_guest')),
                ('authority_guest', models.BooleanField(db_column='authority_guest')),
                ('created_at', models.DateTimeField(db_column='created_at')),
                ('updated_at', models.DateTimeField(db_column='updated_at')),
                ('deleted_at', models.DateTimeField(db_column='deleted_at', default='None')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('group_id', models.IntegerField(db_column='group_id')),
                ('file_name', models.CharField(db_column='file_name', default='None', max_length=100)),
                ('file_path', models.CharField(db_column='file_path', max_length=100)),
                ('folder_id', models.IntegerField(db_column='folder_id', default='None')),
                ('create_at', models.DateTimeField(db_column='create_at')),
                ('delete_at', models.DateTimeField(db_column='delete_at', default='None')),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('created_at', models.DateTimeField(db_column='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('group_name', models.CharField(db_column='group_name', max_length=100, verbose_name='グループ名')),
                ('icon', models.ImageField(blank=True, db_column='icon', null=True, upload_to='static/images/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('notice', models.TextField(db_column='notice', default='', null=True)),
                ('author', models.CharField(db_column='author', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GroupIcon',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('icon', models.ImageField(db_column='icon', upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=100)),
                ('authority', models.BooleanField(db_column='authority')),
                ('group_id', models.ForeignKey(db_column='group_id', on_delete=django.db.models.deletion.CASCADE, to='GroupConnect.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='title', max_length=200)),
                ('content', models.TextField(db_column='content')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('text', models.TextField(db_column='text')),
                ('created_at', models.DateTimeField(db_column='created_at')),
                ('read_number', models.IntegerField(db_column='read_number')),
                ('contributer', models.ForeignKey(db_column='contributer', on_delete=django.db.models.deletion.CASCADE, to='GroupConnect.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Signboard',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='title', max_length=100, verbose_name='タイトル')),
                ('text', models.TextField(db_column='text', verbose_name='説明')),
                ('updated_at', models.DateTimeField(db_column='updated_at', default=django.utils.timezone.now)),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='GroupConnect.Category')),
                ('group_id', models.ForeignKey(db_column='group_id', on_delete=django.db.models.deletion.CASCADE, to='GroupConnect.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('read_situation', models.BooleanField(db_column='read_situation')),
                ('post_id', models.ForeignKey(db_column='post_id', on_delete=django.db.models.deletion.CASCADE, to='GroupConnect.Post')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='GroupConnect.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('chat_id', models.IntegerField(db_column='chat_id')),
                ('text', models.TextField(db_column='text')),
                ('create_at', models.DateTimeField(db_column='create_at')),
                ('delete_at', models.DateTimeField(db_column='delete_at', default='None')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='メールアドレス')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='苗字')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='名前')),
                ('rome_last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='苗字(ローマ字)')),
                ('rome_first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='名前(ローマ字)')),
                ('password', models.CharField(max_length=250, verbose_name='パスワード')),
                ('icon', models.ImageField(blank=True, default='static/images/real-egg.jpg', null=True, upload_to='static/images/', verbose_name='icon')),
                ('introduction', models.TextField(blank=True, default='', null=True, verbose_name='introduction')),
                ('plan_mail_time', models.TimeField(default=datetime.time(7, 0), verbose_name='plan_time')),
                ('new_mail_stop_time', models.TimeField(default=datetime.time(1, 0), verbose_name='mail_stop_time')),
                ('new_mail_start_time', models.TimeField(default=datetime.time(6, 0), verbose_name='mail_start_time')),
                ('notice_signboard', models.BooleanField(default=True, verbose_name='notice_signboard')),
                ('notice_chat', models.BooleanField(default=True, verbose_name='notice_chat')),
                ('notice_calendar', models.BooleanField(default=True, verbose_name='notice_calendar')),
                ('notice_group', models.BooleanField(default=True, verbose_name='notice_group')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', GroupConnect.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='signboard_id',
            field=models.ForeignKey(db_column='signboard_id', on_delete=django.db.models.deletion.CASCADE, to='GroupConnect.Signboard'),
        ),
        migrations.AddField(
            model_name='member',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='group_id',
            field=models.ForeignKey(db_column='group_id', on_delete=django.db.models.deletion.CASCADE, to='GroupConnect.Group'),
        ),
    ]
