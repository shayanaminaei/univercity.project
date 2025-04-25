from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'national_id')

# فرم ثبت‌نام
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'national_id')

# فرم ورود
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        
class UserRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'national_id']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email has been registerd before 😒 ")
        return email

    def clean_national_id(self):
        national_id = self.cleaned_data.get('national_id')
        if national_id and len(national_id) != 10:
            raise forms.ValidationError("National should be 10 digits 🔟 ")
        return national_id
    

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class WalletTopUpForm(forms.Form):
    amount = forms.IntegerField(min_value=1000, label='مبلغ (تومان)')