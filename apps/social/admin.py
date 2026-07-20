from django.contrib import admin
from .models import SocialProfile
from django.utils.html import format_html
from unfold.admin import ModelAdmin
# Register your models here.

class SocialProfileAdmin(ModelAdmin):
    list_display = ['platform','url','is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:40px;border-radius:4px"/>',
                obj.image.url
            )
        return '—'

admin.site.register(SocialProfile,SocialProfileAdmin)

