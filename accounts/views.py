from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
import random
from utils import send_otp_code
from .models import OtpCode, User
from django.contrib import messages
from utils import send_otp_code
from .forms import VerifyCodeForm, UserLoginForm 


class AccountView(View):
    template_name = "base.html"
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self):
        pass
    
class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = "accounts/register.html"
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000,9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number= form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, "We Sent Your A code ...", 'success')
            return redirect("accounts:verify_code")
        return redirect("home:home")
    
    
    
class UserRegistrationCodeView(View):
    class_form = VerifyCodeForm
    template_name="accounts/verify.html"
    def get(self, request):
        form = self.class_form
        return render(request, self.template_name, {'form': form} )

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.class_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'], user_session['full_name'], user_session['password'])
                
                code_instance.delete()
                messages.success(request, "You Registered", 'success')
                return redirect("home:home")
            else:
                messages.error(request, "Code Not Correct!", 'danger')
                return redirect("accounts:verify_code")
        return render(request, self.template_name, {'form': form})



class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
        
    def post(self, request):
        if self.form_class.is_valid():
            messages.success(request, "You Login Perfect ... ", 'success')
            return redirect("accounts:accounts")



class UserLogoutView(View):
    def get(self, request):
        pass