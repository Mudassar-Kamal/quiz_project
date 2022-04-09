from django.urls import path
from .views import LoginView
app_name = "acnt"
urlpatterns = [
    path("login/",LoginView.as_view(),name="login")
]
