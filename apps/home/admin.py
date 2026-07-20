from django.contrib import admin
from .models import BlogPost
from unfold.admin import ModelAdmin
# Register your models here.

class BlogPostAdmin(ModelAdmin):
    list_display = ['title','created_at']
    list_filter = ['created_at']
    search_fields = ['title','content']
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'created_at'

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'cover_image')
        }),
        ('Content', {
            'fields': ('content',)
        }),
       
    )

admin.site.register(BlogPost,BlogPostAdmin)