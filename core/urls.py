from django.urls import path
from core.views import (
    index,
    BusinessView,
    RegisterView,
    LoginView,
    LogoutView
)

urlpatterns = [
    path('', index, name='home'),
    path('business/<int:pk>', BusinessView.as_view(), name='business_view'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]