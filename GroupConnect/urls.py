from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = 'GroupConnect'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
    path('mypage/', views.Mypage.as_view(), name='mypage'),
    path('<int:notice_id>/', views.NoticeDetail.as_view(), name='notice_detail'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)