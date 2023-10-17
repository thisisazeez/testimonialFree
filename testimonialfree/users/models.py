from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, UUIDField, ImageField, OneToOneField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from testimonialfree.users.managers import UserManager
import uuid
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db import models
from PIL import Image


# fs = FileSystemStorage(location='/media/photos')

class User(AbstractUser):
    """
    Default custom user model for TestimonialFree.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
    


class UserProfile(models.Model):
    profile_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True
    )
    cover_image = models.ImageField(_("Cover Image"), upload_to='cover_images/', null=True, blank=True)
    avatar = models.ImageField(_("Profile Image"), upload_to='profile_images/',  null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('users-profile', kwargs={'uuid': self.profile_uuid})
    
    def __str__(self):
        return f'{self.user.email} Profile'