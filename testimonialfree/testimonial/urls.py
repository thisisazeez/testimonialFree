from django.urls import path
from . import views

app_name = "testimonial"

urlpatterns = [
    path('submit/<str:campaign_slug>/', views.submit_testimonial, name='submit_testimonial'),
    path('list-testimonials-for-campaign/<slug:campaign_slug>/', views.list_testimonials_for_campaign, name='list_testimonials_for_campaign'),
    
    path('customquestions/', views.customquestion_list, name='customquestion_list'),
    path('customquestions/create/', views.customquestion_create, name='customquestion_create'),
    path('customquestions/<slug:slug>/', views.customquestion_detail, name='customquestion_detail'),

    path('customquestions/<slug:slug>/update/', views.customquestion_update, name='customquestion_update'),
    path('customquestions/<slug:slug>/delete/', views.customquestion_delete, name='customquestion_delete'),
    
    path('extrainfos/', views.extrainfo_list, name='extrainfo_list'),
    path('extrainfos/create/', views.extrainfo_create, name='extrainfo_create'),
    path('extrainfos/<slug:slug>/', views.extrainfo_detail, name='extrainfo_detail'),

    path('extrainfos/<slug:slug>/update/', views.extrainfo_update, name='extrainfo_update'),
    path('extrainfos/<slug:slug>/delete/', views.extrainfo_delete, name='extrainfo_delete'),
    
    
    path('list-testimonial-campaigns/', views.list_testimonial_campaigns, name='list_testimonial_campaigns'),
    path('create-testimonial-campaign/', views.create_testimonial_campaign, name='create_testimonial_campaign'),
    path('view-testimonial-campaign/<slug:campaign_slug>/', views.view_testimonial_campaign, name='view_testimonial_campaign'),
    path('edit-testimonial-campaign/<slug:campaign_slug>/', views.edit_testimonial_campaign, name='edit_testimonial_campaign'),
    path('delete-testimonial-campaign/<slug:campaign_slug>/', views.delete_testimonial_campaign, name='delete_testimonial_campaign'),
]