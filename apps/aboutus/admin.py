from django.contrib import admin
from .models import CompanyProfile,VisionMission

# Register your models here.

class CompanyProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Company details', {
            'fields': ('name', 'tagline', 'founded_year', 'hero_image')
        }),
        ('About text', {
            'fields': ('about_text',)
        }),
        ('Visibility', {
            'fields': ('is_active',)
        }),
    )

admin.site.register(CompanyProfile,CompanyProfileAdmin)

class VisionMissionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Vision', {
            'fields': ('vision_title', 'vision_text', 'vision_image')
        }),
        ('Mission', {
            'fields': ('mission_title', 'mission_text', 'mission_image')
        }),
        ('Visibility', {
            'fields': ('is_active',)
        }),
    )

admin.site.register(VisionMission,VisionMissionAdmin)