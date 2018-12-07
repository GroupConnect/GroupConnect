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
    path('notice_detail/<int:notice_id>/', views.detail, name='notice_detail'),
    path('group_create/', views.GroupCreate.as_view(), name='group_create'),
]