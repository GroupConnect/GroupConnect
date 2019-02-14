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
    path('notice_detail/(?P<pk>[0-9]+)/', views.NoticeDetail.as_view(), name='notice_detail'),
    path('group_create/', views.GroupCreate.as_view(), name='group_create'),
    path('group_top/(?P<pk>[0-9]+)/', views.GroupTop.as_view(), name='group_top'),
    path('group_top/(?P<pk>[0-9]+)/group_setting/', views.GroupSet.as_view(), name='group_setting'),
    path('group_top/(?P<pk>[0-9]+)/member_list/', views.MemberList.as_view(), name='member_list'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('groupdel/', views.groupdelete, name='groupdelete'),
    path('secession/', views.groupsecession, name='groupsecession'),
    path('group_list/', views.GroupList.as_view(), name='group_list'),
    path('mailsend/', views.mailsend, name='mailsend'),
    path('groupinvite/<token>/(?P<id>[0-9]+)/', views.GroupInvite, name='groupinvite'),
    path('operation/', views.operation, name='operation'),
    path('bordlist/(<?P<pk>[0-9]+)/', views.bordlist.as_view(), name='bordlist'),
    path('signboardcategory/' , views.categoryget , name="categoryget"),
    path('signboardform/' , views.Signboardform , name="Signboardform"),
    path('Category/<int:pk>/', views.SignboardView.as_view() , name="Category" ),   
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
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    path('user_delete/done', views.UserDeleteDone.as_view(), name='user_delete_done'),
    path('user_data_input/', views.UserDataInput.as_view(), name='user_data_input'),
    path('user_data_confirm/', views.UserDataConfirm.as_view(), name='user_data_confirm'),
    path('user_data_create/', views.UserDataCreate.as_view(), name='user_data_create'),

    path('bordlist/(<?P<pk>[0-9]+)/(<?P<id>[0-9]+)/', views.CategoryView.as_view(), name='bordlist'),
    path('bord', views.BordView.as_view(), name='bord'),
    path('signboard/<int:pk>/', views.signboard_page_view, name='signboard'),
    path('signboard/<int:pk>/<int:serected_id>/', views.signboard_page_view, name='signboard'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
