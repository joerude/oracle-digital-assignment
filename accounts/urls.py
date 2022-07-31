from django.contrib.auth.views import LogoutView
from django.urls import path

from config import settings
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path(
        "signout/",
        LogoutView.as_view(),
        {"next_page": settings.LOGOUT_REDIRECT_URL},
        name="signout",
    ),
]
