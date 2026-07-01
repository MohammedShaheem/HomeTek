from django.contrib import admin
from django.utils.html import format_html
from .models import Product,Category
# Register your models here.



"""class controls how the category model will appear in the admin interface
list display -> columns shows on the list page
prepopulated_fields -> autofill with name"""
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','product_count','preview_image','is_active']
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name']


    def product_count(self,obj):
        return obj.products.count()
    
    def preview_image(self,obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:40px;border-radius:4px"/>',
                obj.image.url
            )
        return '—'
    
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'preview_image','name','category',
        'material','is_active','created_at'
    ]
    list_filter      = ['category', 'is_active']
    search_fields    = ['name', 'description', 'material']
    prepopulated_fields = {'slug': ('name',)}
    list_editable    = ['is_active']
    list_per_page    = 20
    readonly_fields  = ['created_at', 'preview_image']

    fieldsets = (
        ('Basic info', {
            'fields':('category','name','slug','is_Active')
        }),
        ('Images',{
            'fields':('image','preview_image')
        }),
        ('Product details', {
            'fields':('description','material','sizes_available')
        }),
        ('Meta',{
            'fields':('created_at',)
        }),
    )

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:60px;border-radius:6px"/>',
                obj.image.url
            )
        return '—'
    
admin.site.register(Product,ProductAdmin)
