from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mysetting/', views.SettingView.as_view(), name='mysetting'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)