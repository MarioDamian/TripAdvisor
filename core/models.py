from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"

class City(models.Model):
    name = models.CharField(max_length=1000)
    population = models.PositiveIntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"

class Comment(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='businesses')
    text = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} created by {}".format(self.text, self.user.username, self.created_at)
