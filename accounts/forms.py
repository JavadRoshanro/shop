from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="You can change the password using <a href=\"../password/\">this form</a>."
    )

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial['password']
    
    
class UserRegistrationForm(forms.Form):
    phone = forms.CharField(max_length=11)
    email = forms.EmailField()
    full_name = forms.CharField(label='full name')
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_email(self):
        email = self.cleaned_data['email'] 
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValueError(" This Email Already Exists")
        
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = User.objects.filter(phone_number = phone)
        if user:
            raise ValueError(" This Phone Exists. Im Sorry")
        return phone
    
class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()
    
    
    
class UserLoginForm(forms.Form):
    name = forms.CharField(max_length=15)
    password = forms.CharField(max_length=20)