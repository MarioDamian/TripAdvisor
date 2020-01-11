from django.contrib import admin
from . import models


class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'business')
    search_fields = ('user',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'country')
    search_fields = ('name',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Register your models here.
admin.site.register(models.Business, BusinessAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.Country, CountryAdmin)