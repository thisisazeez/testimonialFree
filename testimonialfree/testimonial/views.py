from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Testimonial, TestimonialCampaign
from django.contrib.auth.decorators import login_required
from .models import TestimonialCampaign
from .forms import TestimonialCampaignForm 
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomQuestion, ExtraInfo
from .forms import CustomQuestionForm, ExtraInfoForm

def extrainfo_list(request):
    extrainfos = ExtraInfo.objects.all()
    return render(request, 'campaign/extrainfos/extrainfo_list.html', {'extrainfos': extrainfos})

def extrainfo_detail(request, slug):
    extrainfo = get_object_or_404(ExtraInfo, slug=slug)
    return render(request, 'campaign/extrainfos/extrainfo_detail.html', {'extrainfo': extrainfo})

def extrainfo_create(request):
    if request.method == 'POST':
        form = ExtraInfoForm(request.POST)
        if form.is_valid():
            extrainfo = form.save()
            return redirect(extrainfo)
    else:
        form = ExtraInfoForm()
    return render(request, 'campaign/extrainfos/extrainfo_form.html', {'form': form})

def extrainfo_update(request, slug):
    extrainfo = get_object_or_404(ExtraInfo, slug=slug)
    if request.method == 'POST':
        form = ExtraInfoForm(request.POST, instance=extrainfo)
        if form.is_valid():
            form.save()
            return redirect(extrainfo)
    else:
        form = ExtraInfoForm(instance=extrainfo)
    return render(request, 'campaign/extrainfos/extrainfo_form.html', {'form': form})

def extrainfo_delete(request, slug):
    extrainfo = get_object_or_404(ExtraInfo, slug=slug)
    if request.method == 'POST':
        extrainfo.delete()
        return redirect('extrainfo_list')
    return render(request, 'campaign/extrainfos/extrainfo_confirm_delete.html', {'extrainfo': extrainfo})


def customquestion_list(request):
    questions = CustomQuestion.objects.all()
    return render(request, 'campaign/customquestions/customquestion_list.html', {'questions': questions})
 
def customquestion_detail(request, slug):
    question = get_object_or_404(CustomQuestion, slug=slug)
    return render(request, 'campaign/customquestions/customquestion_detail.html', {'question': question})

def customquestion_create(request):
    if request.method == 'POST':
        form = CustomQuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('testimonial:customquestion_list')
    else:
        form = CustomQuestionForm()
    return render(request, 'campaign/customquestions/customquestion_form.html', {'form': form})

def customquestion_update(request, slug):
    question = get_object_or_404(CustomQuestion, slug=slug)
    if request.method == 'POST':
        form = CustomQuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect(question)
    else:
        form = CustomQuestionForm(instance=question)
    return render(request, 'campaign/customquestions/customquestion_form.html', {'form': form})

def customquestion_delete(request, slug):
    question = get_object_or_404(CustomQuestion, slug=slug)
    if request.method == 'POST':
        question.delete()
        return redirect('customquestion_list')
    return render(request, 'campaign/customquestions/customquestion_confirm_delete.html', {'question': question})


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