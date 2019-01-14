from django.urls import path

from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('temp_entry', views.Temp_entryView.as_view(), name='temp_entry'),
    path('temp_entry_result', views.Temp_entry_resultView.as_view(), name='temp_entry_result'),
    path('main_entry', views.Main_entryView.as_view(), name='main_entry'),
    path('main_entry_conf', views.Main_entry_confView.as_view(), name='main_entry_conf'),
    path('main_entry_comp', views.Main_entry_compView.as_view(), name='main_entry_comp'),
    path('mypage', views.MypageView.as_view(), name='mypage'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('pass_setting', views.Pass_settingView.as_view(), name='pass_setting'),
    path('pass_setting_comp', views.Pass_setting_compView.as_view(), name='pass_setting_comp'),
    path('mail_setting', views.Mail_settingView.as_view(), name='mail_setting'),
    path('withdraw', views.WithdrawView.as_view(), name='withdraw'),
    path('grouptop', views.GrouptopView.as_view(), name='grouptop'),
    path('grouplist', views.GrouplistView.as_view(), name='grouplist'),
    path('creategroup', views.CreategroupView.as_view(), name='creategroup'),
    path('bordlist', views.BordlistView.as_view(), name='bordlist'),
    path('bord', views.BordView.as_view(), name='bord'),
    path('notfound', views.NotFoundView.as_view(), name='notfound'),
]