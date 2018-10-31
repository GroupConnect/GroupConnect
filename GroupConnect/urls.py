from django.urls import path

from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('logout/', views.Logout.as_view(), name='logout'),
]