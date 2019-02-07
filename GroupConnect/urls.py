from django.urls import path

from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('signboard/<int:pk>/', views.signboard_page_view, name='signboard'),
    path('mypage', views.MypageView.as_view(), name='mypage'),
    path('grouptop', views.GrouptopView.as_view(), name='grouptop'),
    path('bord', views.BordView.as_view(), name='bord'),
    path('bordlist/', views.bordlist.as_view(), name='bordlist'),
]
