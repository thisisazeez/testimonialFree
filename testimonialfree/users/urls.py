from django.urls import path

from testimonialfree.users.views import (
    user_redirect_view,
    user_update_view,
    profile,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path('~/', profile, name='users-profile'),
]
