from django.urls import path

from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('temp_entry', views.Temp_entryView.as_view(), name='temp_entry'),
    path('temp_entry_result', views.Temp_entry_resultView.as_view(), name='temp_entry_result'),
    path('mypage', views.MypageView.as_view(), name='mypage'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('grouptop', views.GrouptopView.as_view(), name='grouptop'),
    path('grouplist', views.GrouplistView.as_view(), name='grouplist'),
    path('bordlist', views.BordlistView.as_view(), name='bordlist'),
    path('bord', views.BordView.as_view(), name='bord'),
    path('notfound', views.NotFoundView.as_view(), name='notfound'),
]