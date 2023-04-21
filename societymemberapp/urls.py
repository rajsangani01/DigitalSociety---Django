from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('societymember-profile/', views.societymember_profile,
         name='societymember-profile'),
    path('societymember-password-change/', views.societymember_pass_change,
         name='societymember-password-change'),
    path('notice-list-society/', views.notice_list_society,
         name='notice-list-society'),
    path('notice-detail-view-society/<int:pk>/',
         views.notice_detail_views_society, name='notice-detail-view-society'),
    path('add-complaint/', views.add_complaint, name='add-complaint'),
    path('all-complaint/', views.all_complaint, name='all-complaint'),
    path('add-events/', views.add_events, name='add-events'),
    path('all-events/', views.all_events, name='all-events'),
    path('member-maintenance/', views.member_maintenance,
         name='member-maintenance'),
    path('maintenance-payment/<int:pk>',
         views.maintenance_payment, name='maintenance-payment'),
]
