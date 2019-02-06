from django.urls import path

from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signboard/<int:pk>/', views.SignboardPage, name='signboard'),
    path('mypage', views.MypageView.as_view(), name='mypage'),
    path('grouptop', views.GrouptopView.as_view(), name='grouptop'),
    path('bord', views.BordView.as_view(), name='bord'),
]