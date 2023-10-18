from django.db import models
from django.conf import settings
# Create your models here.
EXTRAINFO_CHOICES = (
    ("TEXT", "TEXT"),
    ("CHECKBOX", "CHECKBOX"),
)

class Question(models.Model):
    text = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.text
    
class ExtraInfo(models.Model):
    text = models.CharField(max_length=255, blank=True, null=True)
    required = models.BooleanField(default=False)
    type = models.CharField(max_length=20, blank=True, null=True, default="TEXT", choices=EXTRAINFO_CHOICES)

    def __str__(self):
        return self.text

class TestimonialCampaign(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    logo = models.ImageField(upload_to='testimonial_logos/', blank=True, null=True)
    header_title = models.CharField(max_length=200, blank=True, null=True)
    custom_message = models.TextField(blank=True, null=True)
    questions = models.ManyToManyField(Question, blank=True)
    extra_info = models.ManyToManyField(ExtraInfo, blank=True)
    
    def __str__(self):
       return '{} {}'.format(self.name, self.user.email)


class Testimonial(models.Model):
    campaign = models.ForeignKey(TestimonialCampaign, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    responses = models.JSONField()  # Store responses as JSON
    
    def __str__(self):
        return f"Testimonial for {self.campaign.name} by {self.name}"
    

