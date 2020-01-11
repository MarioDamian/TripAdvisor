from django.urls import path
from core.views import (
    index,
    RegisterView,
    LoginView,
    LogoutView
)

urlpatterns = [
    path('', index, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]