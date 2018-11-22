from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

app_name = 'GroupConnect'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mysetting/', views.SettingView.as_view(), name='mysetting'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)