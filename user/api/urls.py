from django.urls import path
from user.api.views import RegisterView

urlpatterns = [
    path('auth/register/', RegisterView.as_view())
]
