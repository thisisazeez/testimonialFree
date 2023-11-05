from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

EXTRAINFO_CHOICES = (
    ("TEXT", "TEXT"),
    ("CHECKBOX", "CHECKBOX"),
)


class CustomQuestion(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    text = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('testimonial:customquestion_list', args=[str(self.slug)])
    
    def save(self, *args, **kwargs):
        value = self.text
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class ExtraInfo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    text = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    required = models.BooleanField(default=False)
    type = models.CharField(max_length=20, default="TEXT", choices=EXTRAINFO_CHOICES)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('testimonial:extrainfo_detail', args=[str(self.slug)])
    
    def save(self, *args, **kwargs):
        value = self.text
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class TestimonialCampaign(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    logo = models.ImageField(upload_to='testimonial_logos/', blank=True, null=True)
    header_title = models.CharField(max_length=200, blank=True, null=True)
    q1 = models.CharField(max_length=100, verbose_name="Question One", blank=True, null=True)
    q2 = models.CharField(max_length=100, verbose_name="Question Two", blank=True, null=True)
    q3 = models.CharField(max_length=100, verbose_name="Question Three", blank=True, null=True)
    custom_message = models.TextField(blank=True, null=True)
    custom_questions = models.ManyToManyField(CustomQuestion, blank=True)
    extra_info = models.ManyToManyField(ExtraInfo, blank=True)
    
    def __str__(self):
       return '{} {}'.format(self.name, self.user.email)
   
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Testimonial(models.Model):
    campaign = models.ForeignKey(TestimonialCampaign, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    dynamic_data = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return f"Testimonial for {self.campaign.name} by {self.name}"

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)

        # Serialize dynamic data (custom questions and extra information) to JSON
        dynamic_data = {
            "q1": self.q1,
            "q2": self.q2,
            "q3": self.q3,
            "custom_questions": [str(custom_question) for custom_question in self.custom_questions.all()],
            "extra_info": [str(extra_info) for extra_info in self.extra_info.all()],
        }
        self.dynamic_data = json.dumps(dynamic_data)

        super().save(*args, **kwargs)
    


