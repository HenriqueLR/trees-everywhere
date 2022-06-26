from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import register

urlpatterns=[
    path('sign_in/',LoginView.as_view(template_name='accounts/auth/login.html', redirect_authenticated_user=True), name='login'),
    path('sign_out/',LogoutView.as_view(next_page=reverse_lazy('accounts:login')),name='logout'),
    path('register/', register, name='register'),
]
