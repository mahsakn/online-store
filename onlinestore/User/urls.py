
from django.urls import path
from . import views
from .views import AuthenticateView, LoginView, RegisterView,ForgetPasswordView,ProfileView, logout


app_name = "User"
urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('authenticate/', AuthenticateView.as_view(), name="authenticate"),
    path('forgetpassword/',ForgetPasswordView.as_view(), name="forget_password"),
    path('profile/<int:user_id>/',ProfileView.as_view(), name="profile"),
    path('logout/', logout, name="logout"),
]
