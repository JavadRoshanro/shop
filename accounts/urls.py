from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path("", views.AccountView.as_view(), name="accounts"),
    path("register/", views.UserRegisterView.as_view(), name="register_user"),
    path("verify/", views.UserRegistrationCodeView.as_view(), name="verify_code"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
]