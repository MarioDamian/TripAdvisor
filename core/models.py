from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class MyUser(User):
    pass


class Business(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='businesses')
    image = models.ImageField(upload_to='images/business')
    stars = models.PositiveIntegerField()
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=4096)


class Review(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')