from django.urls import path

from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('provisional_user_create/', views.MailSend.as_view(), name='provisional_user_create'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),

]