from django.contrib import admin
from .models import Testimonial, TestimonialCampaign, CustomQuestion, ExtraInfo

admin.site.register(Testimonial)
admin.site.register(TestimonialCampaign)
admin.site.register(CustomQuestion)
admin.site.register(ExtraInfo)