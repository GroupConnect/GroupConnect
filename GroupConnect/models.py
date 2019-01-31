import datetime
from django.conf import settings
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager

if settings.AUTH_USER_MODEL == 'GroupConnect.User':
    class UserManager(BaseUserManager):
        use_in_migrations = True

        def _create_user(self, email, password, **extra_fields):
            """Create and save a user with the given username, email, and
            password."""
            if not email:
                raise ValueError('The given email must be set')
            email = self.normalize_email(email)

            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_user(self, email, password=None, **extra_fields):
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)
            return self._create_user(email, password, **extra_fields)

        def create_superuser(self, email, password, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)

            if extra_fields.get('is_staff') is not True:
                raise ValueError('Superuser must have is_staff=True.')
            if extra_fields.get('is_superuser') is not True:
                raise ValueError('Superuser must have is_superuser=True.')

            return self._create_user(email, password, **extra_fields)


    class User(AbstractBaseUser, PermissionsMixin):

        email = models.EmailField(_('メールアドレス'), unique=True)
        last_name = models.CharField(_('苗字'), max_length=100, blank=True, null=True)
        first_name = models.CharField(_('名前'), max_length=100, blank=True, null=True)
        rome_last_name = models.CharField(_('苗字(ローマ字)'), max_length=100, blank=True, null=True)
        rome_first_name = models.CharField(_('名前(ローマ字)'), max_length=100, blank=True, null=True)
        password = models.CharField(_('パスワード'), max_length=250)
        icon = models.ImageField(_('icon'), upload_to='static/images/', blank=True, null=True)
        introduction = models.TextField(_('introduction'), blank=True, null=True)
        plan_mail_time = models.TimeField(_('plan_time'), default=datetime.time(7,0,0))
        new_mail_stop_time = models.TimeField(_('mail_stop_time'), default=datetime.time(1,0,0))
        new_mail_start_time = models.TimeField(_('mail_start_time'), default=datetime.time(6,0,0))
        notice_signboard = models.BooleanField(_('notice_signboard'), default=True)
        notice_chat = models.BooleanField(_('notice_chat'), default=True)
        notice_calendar = models.BooleanField(_('notice_calendar'), default=True)
        notice_group = models.BooleanField(_('notice_group'), default=True)   

        is_staff = models.BooleanField(
            _('staff status'),
            default=False,
            help_text=_(
                'Designates whether the user can log into this admin site.'),
        )
        is_active = models.BooleanField(
            _('active'),
            default=True,
            help_text=_(
                'Designates whether this user should be treated as active. '
                'Unselect this instead of deleting accounts.'
            ),
        )
        date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

        objects = UserManager()

        EMAIL_FIELD = 'email'
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []

        class Meta:
            verbose_name = _('user')
            verbose_name_plural = _('users')

        def get_full_name(self):
            """Return the first_name plus the last_name, with a space in
            between."""
            full_name = '%s %s' % (self.first_name, self.last_name)
            return full_name.strip()

        def get_short_name(self):
            """Return the short name for the user."""
            return self.first_name

        def email_user(self, subject, message, from_email=None, **kwargs):
            """Send an email to this user."""
            send_mail(subject, message, from_email, [self.email], **kwargs)

        @property
        def username(self):
            return self.email

class Group(models.Model):
    """
    グループのクラス

    Parameters
    ----------
    id : int
        対象の識別用PrimaryKey
    group_name : str
        対象のグループ名
    icon :  str
        対象のグループのアイコン
    date_joined : datetime
        対象のグループが作られた日時
    """
    id = models.AutoField(primary_key=True, db_column='id')
    group_name = models.CharField(max_length=100, db_column='group_name')
    icon = models.ImageField(upload_to='static/images/', db_column='icon', blank=True, null=True)
    created_at = models.DateTimeField(_('created_at'), default=timezone.now)

    def __str__(self):
        """
        Returns
        -------
        __str__ : str
            対象のグループ名を返す
        """
        return self.group_name

class Member(models.Model):
    """
    グループにおけるメンバーのクラス

    Parameters
    ----------
    user_id = int
        対象のユーザを参照する外部キー
    group_id : int
        対象の所属するグループを参照する外部キー
    name : str
        対象のメンバーの名前
    authority : boolean
        対象のメンバーの権限のフラグ
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_id')
    name = models.CharField(max_length=100, db_column='name')
    authority = models.BooleanField(db_column='authority')

class Signboard(models.Model):
    """
    掲示板のクラス

    Parameters
    ----------
    id : int
        対象の識別用PrimaryKey
    group_id : int
        対象のGroupクラスのidを参照する外部キー
    title : str
        対象の掲示板のタイトル
    category : str
        対象の掲示板を分類するカテゴリ
    text : str
        対象の掲示板の説明
    """
    id = models.AutoField(primary_key=True, db_column='id')
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_id')
    title = models.CharField(max_length=100, db_column='title')
    category = models.CharField(max_length=100, db_column='category')
    text = models.TextField(db_column='text')
    updated_at = models.DateTimeField(db_column='updated_at', default=timezone.now)

    def __str__(self):
        """
        Returns
        -------
        __str__ : str
            対象のタイトルを返す
        """
        return self.title

class Post(models.Model):
    """
    投稿のクラス

    Parameters
    ----------
    id : int
        対象の識別用PrimaryKey
    signboard_id : int
        対象のSignBoardクラスのidを参照する外部キー
    text : str
        対象の投稿の本文
    contributer : str
        対象のUserクラスのemailを参照する外部キー
    created_at : datetime.datetime
        対象の投稿日時をPython標準のdatetime型で保存する
    read_number : int
        対象の自クラスに結び付くSituationクラスのユーザ数を格納する
    """
    id = models.AutoField(primary_key=True, db_column='id')
    signboard_id = models.ForeignKey(Signboard, on_delete=models.CASCADE, db_column='signboard_id')
    text = models.TextField(db_column='text')
    attached_file = models.FileField(
        upload_to='files/',
        db_column='attached_file',
        blank=True,
        null=True
    )
    contributer = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='contributer')
    created_at = models.DateTimeField(db_column='created_at', default=timezone.now)
    read_number = models.IntegerField(db_column='read_number')
    reply = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        db_column='reply',
        blank=True,
        null=True
    )

class Situation(models.Model):
    """
    既読状況のクラス

    Parameters
    ----------
    id : int
        対象の識別用PrimaryKey
    post_id : int
        対象の元となる投稿IDを参照する外部キー
    user_id : int
        対象の投稿に対して既読になっているUserIDを参照する外部キー
    read_situation : boolean
        対象の元となる投稿の既読可否を保持する
    """
    id = models.AutoField(primary_key=True, db_column='id')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='post_id')
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='user_id')
    read_situation = models.BooleanField(db_column='read_situation')

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


class Notice(models.Model):
	id = models.AutoField(primary_key=True, db_column='id')
	title = models.CharField(max_length=200, db_column='title')
	content = models.TextField(db_column='content')

class GroupIcon(models.Model):
	id = models.AutoField(primary_key=True, db_column='id')
	icon = models.ImageField(upload_to='static/images/', db_column='icon')











