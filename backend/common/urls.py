from django.urls import path

from common.views import CheckEmailView

urlpatterns = [
    path("check_email/", CheckEmailView.as_view())
]
