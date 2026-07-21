from django.contrib import admin
from.models import ContactUs
from unfold.admin import ModelAdmin
# Register your models here.


class ContactAdmin(ModelAdmin):
    list_display = ['email','phone','address','created_at','image']
    list_filter = ['created_at']
    search_fields = ['email']
    
    

admin.site.register(ContactUs,ContactAdmin)