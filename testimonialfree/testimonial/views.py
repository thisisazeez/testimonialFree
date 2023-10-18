from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Testimonial, TestimonialCampaign
from django.contrib.auth.decorators import login_required
from .models import TestimonialCampaign
from .forms import TestimonialCampaignForm 


@login_required
def create_testimonial_campaign(request):
    if request.method == 'POST':
        form = TestimonialCampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.user = request.user
            campaign.save()
            return redirect('view_testimonial_campaign', campaign.slug)  # Use the slug for redirection
    else:
        form = TestimonialCampaignForm()
    
    return render(request, 'campaign/create_testimonial_campaign.html', {'form': form})

def list_testimonial_campaigns(request):
    campaigns = TestimonialCampaign.objects.all()
    return render(request, 'campaign/list_testimonial_campaigns.html', {'campaigns': campaigns})

@login_required
def view_testimonial_campaign(request, campaign_slug):
    campaign = get_object_or_404(TestimonialCampaign, slug=campaign_slug)
    return render(request, 'view_testimonial_campaign.html', {'campaign': campaign})

@login_required
def edit_testimonial_campaign(request, campaign_slug):
    campaign = get_object_or_404(TestimonialCampaign, slug=campaign_slug)
    
    if request.method == 'POST':
        form = TestimonialCampaignForm(request.POST, request.FILES, instance=campaign)
        if form.is_valid():
            campaign = form.save()
            return redirect('view_testimonial_campaign', campaign.slug)  # Use the slug for redirection
    else:
        form = TestimonialCampaignForm(instance=campaign)
    
    return render(request, 'campaign/edit_testimonial_campaign.html', {'form': form, 'campaign': campaign})

@login_required
def delete_testimonial_campaign(request, campaign_slug):
    campaign = get_object_or_404(TestimonialCampaign, slug=campaign_slug)
    
    if request.method == 'POST':
        if campaign.user == request.user:
            campaign.delete()
            return redirect('list_testimonial_campaigns')  
    return render(request, 'campaign/delete_testimonial_campaign.html', {'campaign': campaign})


def list_testimonials_for_campaign(request, campaign_slug):
    campaign = get_object_or_404(TestimonialCampaign, slug=campaign_slug)
    testimonials = Testimonial.objects.filter(campaign=campaign)
    return render(request, 'campaign/list_testimonials_for_campaign.html', {'campaign': campaign, 'testimonials': testimonials})

@require_http_methods(['GET', 'POST'])
def submit_testimonial(request, campaign_slug):
    campaign = get_object_or_404(TestimonialCampaign, slug=campaign_slug)
    
    if request.method == 'POST':
        responses = {}
        for question in campaign.questions:
            response_key = f'question_{question}'
            responses[response_key] = request.POST.get(response_key, '')
        
        name = request.POST.get('name', '')  # Optional for unauthenticated users
        email = request.POST.get('email', '')  # Optional for unauthenticated users
        
        testimonial = Testimonial(
            campaign=campaign,
            name=name,
            email=email,
            responses=responses,
        )
        testimonial.save()
        # Redirect or render a success page
    return render(request, 'testimonial/testimonial.html', {'campaign': campaign})