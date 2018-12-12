from django.urls import path

from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bordlist/', views.bordlist.as_view(), name='bordlist'),
    
]
