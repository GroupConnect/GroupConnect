from django.urls import path

from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mysetting/', views.SettingView.as_view(), name='mysetting'),
]

