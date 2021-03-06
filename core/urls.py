from django.urls import path
from core.views import (
    index,
    BusinessView,
    CommentCreateView,
CommentDeleteView,
    RegisterView,
    LoginView,
    LogoutView,
    ReviewCreateView
)

urlpatterns = [
    path('', index, name='home'),
    path('business/<int:pk>/review/create', ReviewCreateView.as_view(), name='review_create'),
    path('business/<int:pk>', BusinessView.as_view(), name='business_detail'),
    path('business/<int:pk>/comment/create', CommentCreateView.as_view(), name='comment_create'),
    path('business/<int:pk>/comment/delete', CommentDeleteView.as_view(), name='comment_delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
