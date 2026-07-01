from django.contrib import admin
from .models import SocialProfile
# Register your models here.

class SocialProfileAdmin(admin.ModelAdmin):
    list_display = ['platform','handle','url','is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']

admin.site.register(SocialProfile,SocialProfileAdmin)

