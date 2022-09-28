from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as _login, logout as _logout
from User.forms import AuthenticateForm, LoginForm, RegisterForm, ForgetPassForm, UserUpdateForm
from User.models import OTP, Address, User, OTPType
from User.utils import sending_email
from django.views.generic import DetailView


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        next = request.GET.get("next", )

        if next:
            return render(
                request,
                'User/login.html',
                {'login_form': login_form, 'next': next})
        else:
            return render(
                request,
                'User/login.html',
                {'login_form': login_form, })

    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            userpass = login_form.cleaned_data
            user = authenticate(
                request,
                username=userpass["username"],
                password=userpass["password"]
            )
            next = request.GET.get("next", )

            if user is not None:
                _login(request, user)
                if next:
                    return redirect(next)
                else:
                    return redirect('home')
            else:
                login_form.errors['user'] = 'اطلاعات اشتباه است '
                return render(
                    request,
                    'User/login.html',
                    {"login_form": login_form})
        else:
            login_form.errors['user'] = 'اطلاعات اشتباه است '
            return render(
                request,
                'User/login.html',
                {"login_form": login_form})


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(
            request,
            'User/registerr.html',
            {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            create_user, created = User.objects.get_or_create(email=email, is_email_verified=False)
            send_code = OTP.objects.create(user=create_user, type=OTPType.AUTHENTICATE)

            if sending_email('The code expires in 3 minutes', send_code.code, create_user.email):
                return redirect("user:authenticate")

            else:
                register_form.errors['email'] = 'error'
                return render(
                    request,
                    "User/registerr.html",
                    {"register_form": register_form})

        else:
            register_form.errors['email'] = 'ایمیل وجود دارد '
            return render(
                request,
                "User/registerr.html",
                {"register_form": register_form})


class AuthenticateView(View):
    def get(self, request):
        authenticate_form = AuthenticateForm()
        return render(
            request,
            "User/authenticate.html",
            {'authenticate_form': authenticate_form}
        )

    def post(self, request):
        authenticate_form = AuthenticateForm(request.POST)
        if authenticate_form.is_valid():
            code_obj = authenticate_form.cleaned_data.get("code")
            user = code_obj.user
            user.set_password(authenticate_form.cleaned_data.get("password"))
            user.is_email_verified = True
            user.save()
            code_obj.is_used = True
            code_obj.save()
            _login(request, user)
            return redirect('home')

        else:
            return render(
                request,
                "User/authenticate.html",
                {"authenticate_form": authenticate_form}
            )


class ForgetPasswordView(View):
    def get(self, request):
        forgetpass_form = ForgetPassForm()
        return render(
            request,
            "User/password.html",
            {'forgetpass_form': forgetpass_form}
        )

    def post(self, request):
        forgetpass_form = ForgetPassForm(request.POST)
        if forgetpass_form.is_valid():
            user = forgetpass_form.cleaned_data.get("email")
            code = OTP.objects.create(user=user, type=OTPType.FORGETPASSWORD)
            if sending_email('The code expires in 3 minutes', code.code, user.email):
                return redirect("user:authenticate")
            else:
                forgetpass_form.errors['pass'] = ' مشکلی در ارسال ایمیل به وجود امد لطفا دوباره تلاش کنید'
                return render(
                    request,
                    "User/password.html",
                    {"password_form": forgetpass_form}
                )

        else:
            forgetpass_form.errors['pass'] = 'ایمیل وجود ندارد '
            return render(
                request,
                "User/password.html",
                {"password_form": forgetpass_form}
            )


class ProfileView(DetailView):
    model = User
    template_name = "User/profile.html"
    context_object_name = "user_obj"
    pk_url_kwarg = "user_id"

    def get_context_data(self, **kwargs):
        add_user = ""
        context = super().get_context_data(**kwargs)
        object_user = self.get_object()
        profile_form = UserUpdateForm(instance=object_user)
        address_user = object_user.address.all()

        for elm in address_user:
            add_user = elm.add + "\n"

        context['add_user'] = add_user
        context['profile_form'] = profile_form
        return context

    def post(self, request, user_id):
        object_user = User.objects.get(id=user_id)
        profile_form = UserUpdateForm(request.POST, instance=object_user, files=request.FILES)
        if profile_form.is_valid():
            add = request.POST.get("address")
            obj_address = Address.objects.create(add=add)
            object_user.address.add(obj_address)
            object_user = profile_form.save(commit=False)
            object_user.save()
            return redirect(
                "user:profile",
                user_id=object_user.id
            )
        else:
            return redirect(
                "user:profile",
                kwargs={"profile_form": profile_form}
            )


def logout(request):
    _logout(request)
    return redirect('home')
