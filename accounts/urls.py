from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path("", views.AccountView.as_view(), name="accounts"),
    path("register/", views.UserRegisterView.as_view(), name="register_user"),
    path("verify/", views.UserRegistrationCodeView.as_view(), name="verify_code"),
]