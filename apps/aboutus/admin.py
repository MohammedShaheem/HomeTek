from django.contrib import admin
from .models import CompanyProfile,VisionMission,WhyChooseUs
from unfold.admin import ModelAdmin
# Register your models here.

class CompanyProfileAdmin(ModelAdmin):
    fieldsets = (
        ('Company details', {
            'fields': ('name', 'tagline', 'founded_year', 'hero_image','cover_image')
        }),
        ('About text', {
            'fields': ('about_text',)
        }),
        ('Visibility', {
            'fields': ('is_active',)
        }),
    )

admin.site.register(CompanyProfile,CompanyProfileAdmin)

class VisionMissionAdmin(ModelAdmin):
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

class WhyChooseUsAdmin(ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'icon')
    search_fields = ('title', 'description')
    ordering = ('order', 'id')

    fieldsets = (
        (None, {
            'fields': ('title', 'icon', 'description')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )
admin.site.register(WhyChooseUs,WhyChooseUsAdmin)