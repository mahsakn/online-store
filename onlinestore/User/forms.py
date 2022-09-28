

from django import forms
from django.contrib.auth.password_validation import validate_password
from User.models import OTP, User
from django.contrib.auth.forms import UserChangeForm

class LoginForm(forms.Form):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'e-field-inner', 'placeholder': "نام کاربری خود را وارد کنید"}),
        label='نام کاربری'
        )

    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'e-field-inner', 'placeholder': "رمز عبور خود را وارد کنید"}),
        label='رمز عبور'
        )


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'e-field-inner', 'placeholder': "ایمیل خود را وارد کنید"}),
        label='ایمیل'
        )

    def clean_username(self):
        email = self.cleaned_data.get('email')
        exists_email = User.objects.filter(email=email, is_email_verified=True).exists()
        if exists_email:
            raise forms.ValidationError('کاربری با این ایمیل وجود دارد')
        return email


class AuthenticateForm(forms.Form):
    code = forms.CharField(
        max_length=10, 
        widget=forms.TextInput(attrs={'class': "e-field-inner"}), 
        label="کد"
        )

    password = forms.CharField(
        max_length=20, 
        widget=forms.PasswordInput(attrs={'class': 'e-field-inner'}),
        label="رمز عبور",
        validators=[validate_password]
        )

    re_password = forms.CharField(
        max_length=20, 
        widget=forms.PasswordInput(attrs={'class': 'e-field-inner'}),
        label="تکرار رمز عبور"
        )




    def clean_code(self):
        code = self.cleaned_data.get("code")
        otp_obj = OTP.objects.filter(code=code , is_used=False).first()
        if not otp_obj:
            raise forms.ValidationError("کد وجود ندارد")
        if otp_obj.is_expired:
            raise forms.ValidationError("out of time")

        return otp_obj


    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return re_password



class ForgetPassForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'e-field-inner'})
        )

    def clean_email(self):
        user_obj = User.objects.filter(
            email=self.cleaned_data.get("email"), 
            is_email_verified=True,
            is_active=True
            ).first()

        if not user_obj:
            raise forms.ValidationError("not exist")
        return user_obj


class UserUpdateForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['phone'].required = False
        self.fields['profile_image'].required = False

    password = None

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','phone' , 'profile_image']
        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'e-field-inner'}),
            'first_name': forms.TextInput(attrs={'class': 'e-field-inner',}),
            'last_name': forms.TextInput(attrs={'class': 'e-field-inner'}),
            'phone' : forms.TextInput(attrs={'class': 'e-field-inner'}),
            'profile_image' : forms.FileInput()    }

    
