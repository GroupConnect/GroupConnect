from django.urls import path, include
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
    #path('user_update/<int:user_id>/', views.UserUpdate, name='user_update'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('user_testupdate/<int:pk>/', views.UserTestUpdate.as_view(), name='user_testupdate'),
    path('user_mailaddress_update/<int:pk>/', views.UserMailaddressUpdate.as_view(), name='user_mailaddress_update'),
    path('user_testmailaddress_update/<int:pk>/', views.UserTestMailaddressUpdate.as_view(), name='user_testmailaddress_update'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change_test/', views.PasswordChangeTest.as_view(), name='password_change_test'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('user_delete/', views.user_delete, name='user_delete'),
    path('user_data_input/', views.UserDataInput.as_view(), name='user_data_input'),
    path('user_data_confirm/', views.UserDataConfirm.as_view(), name='user_data_confirm'),
    path('user_data_create/', views.UserDataCreate.as_view(), name='user_data_create'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)