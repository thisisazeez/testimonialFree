from django.urls import path
from . import views

app_name = "testimonial"

urlpatterns = [
    path('submit/<str:campaign_slug>/', views.submit_testimonial, name='submit_testimonial'),
    path('list-testimonials-for-campaign/<slug:campaign_slug>/', views.list_testimonials_for_campaign, name='list_testimonials_for_campaign'),
    
    
    path('list-testimonial-campaigns/', views.list_testimonial_campaigns, name='list_testimonial_campaigns'),
    path('create-testimonial-campaign/', views.create_testimonial_campaign, name='create_testimonial_campaign'),
    path('view-testimonial-campaign/<slug:campaign_slug>/', views.view_testimonial_campaign, name='view_testimonial_campaign'),
    path('edit-testimonial-campaign/<slug:campaign_slug>/', views.edit_testimonial_campaign, name='edit_testimonial_campaign'),
    path('delete-testimonial-campaign/<slug:campaign_slug>/', views.delete_testimonial_campaign, name='delete_testimonial_campaign'),
]