from django.urls import path

from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mypage', views.MypageView.as_view(), name='mypage'),
    path('notice', views.NoticeView.as_view(), name='notice'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('grouptop', views.GrouptopView.as_view(), name='grouptop'),
    path('bord', views.BordView.as_view(), name='bord'),
]