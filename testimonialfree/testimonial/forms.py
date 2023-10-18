from django import forms
from .models import TestimonialCampaign, Testimonial, CustomQuestion, ExtraInfo


class TestimonialCampaignForm(forms.ModelForm):
    class Meta:
        model = TestimonialCampaign
        fields = ['name', 'logo', 'header_title', 'custom_message', 'custom_questions', 'extra_info', 'q1', 'q2', 'q3']
        

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'email', 'responses']
        
class CustomQuestionForm(forms.ModelForm):
    class Meta:
        model = CustomQuestion
        fields = ['text', 'type']

class ExtraInfoForm(forms.ModelForm):
    class Meta:
        model = ExtraInfo
        fields = ['text', 'required', 'type']