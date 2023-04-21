from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('chairman-profile/', views.chairman_profile, name='chairman-profile'),
    path('chairman-password-change/', views.chairman_pass_change, name='chairman-password-change'),
    path('add-societymember/' , views.add_societymember, name='add-societymember'),
    path('all-societymember/' , views.all_societymember, name='all-societymember'),
    path('add-notice/' , views.add_notice, name='add-notice'),
    path('notice-list/' , views.notice_list, name='notice-list'),
    path('notice-detail-view/<int:pk>/' , views.notice_deatil_view, name='notice-detail-view'),
    path('all-complaint-chairman-view/' , views.all_complaint_chairman_view, name='all-complaint-chairman-view'),
    path('all-events-chairman-view/' , views.all_events_chairman_view, name='all-events-chairman-view'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('change-password-otp/', views.change_password_otp, name='change-password-otp'),
    path('add-maintenance/', views.add_maintenance, name='add-maintenance'),
    path('all-maintenance/', views.all_maintenance, name='all-maintenance'),
 
]
