from django.contrib import admin
from.models import Enquiry
from unfold.admin import ModelAdmin
# Register your models here.


class EnquiryAdmin(ModelAdmin):
    list_display = ['name','email','phone','submitted_at']
    list_filter = ['submitted_at']
    search_fields = ['name','email','message']
    # list_editable = ['is_read']
    readonly_fields =['name','email','phone','message','submitted_at']
    date_hierarchy = 'submitted_at'

admin.site.register(Enquiry,EnquiryAdmin)