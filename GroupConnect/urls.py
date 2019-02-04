from django.urls import path
from . import views

app_name = 'GroupConnect'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
    path('mypage/', views.Mypage.as_view(), name='mypage'),
    path('notice_detail/(?P<pk>[0-9]+)/', views.NoticeDetail.as_view(), name='notice_detail'),
    path('group_create/', views.GroupCreate.as_view(), name='group_create'),
    path('group_top/(?P<pk>[0-9]+)/', views.GroupTop.as_view(), name='group_top'),
    path('group_top/(?P<pk>[0-9]+)/group_setting/', views.GroupSet.as_view(), name='group_setting'),
    path('group_top/(?P<pk>[0-9]+)/member_list/', views.MemberList.as_view(), name='member_list'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('groupdel/', views.groupdelete, name='groupdelete'),
    path('secession/', views.groupsecession, name='groupsecession'),
    path('group_list/', views.GroupList.as_view(), name='group_list'),

    path('mailsend/', views.mailsend, name='mailsend'),
    path('groupinvite/<token>/(?P<id>[0-9]+)/', views.GroupInvite, name='groupinvite'),
    path('operation/', views.operation, name='operation'),


    path('bordlist/(<?P<pk>[0-9]+)/', views.bordlist.as_view(), name='bordlist'),
    path('signboard/<int:pk>/', views.SignboardView.as_view(), name='Signboard'),
    path('signboardcategory/' , views.categoryget , name="categoryget"),
    path('signboardform/' , views.Signboardform , name="Signboardform"),
    path('Category/<int:pk>/', views.SignboardView.as_view() , name="Category" ),

]