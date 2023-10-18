from django import forms
from .models import TestimonialCampaign, Testimonial

class TestimonialCampaignForm(forms.ModelForm):
    class Meta:
        model = TestimonialCampaign
        fields = ['name', 'slug', 'logo', 'header_title', 'custom_message', 'questions', 'extra_info']
        

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'email', 'responses']