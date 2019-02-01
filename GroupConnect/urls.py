from django.urls import path

from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mypage', views.MypageView.as_view(), name='mypage'),
    path('grouptop', views.GrouptopView.as_view(), name='grouptop'),
    path('bord', views.BordView.as_view(), name='bord'),
    path('bord_setting', views.Bord_settingView.as_view(), name='bord_setting'),
]