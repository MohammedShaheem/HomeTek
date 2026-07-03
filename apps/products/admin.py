from django.contrib import admin
from django.utils.html import format_html
from .models import Product,Category,SubCategory,Collection,ProductImage
# Register your models here.



class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1
    prepopulated_fields = {'slug': ('name',)}

"""class controls how the category model will appear in the admin interface
list display -> columns shows on the list page
prepopulated_fields -> autofill with name"""
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','product_count','preview_image','is_active']
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name']
    inlines = [SubCategoryInline]


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

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['preview_image', 'name', 'category', 'material', 'is_active', 'created_at']
    list_filter = ['category', 'is_active']
    search_fields = ['name', 'description', 'material']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active']
    list_per_page = 20
    readonly_fields = ['created_at', 'updated_at', 'preview_image']
    inlines = [ProductImageInline]

    fieldsets = (
        ('Basic info', {
            'fields': ('category', 'subcategory', 'collection', 'name', 'slug', 'is_active')
        }),
        ('Preview', {
            'fields': ('preview_image',)
        }),
        ('Product details', {
            'fields': ('description', 'material', 'sizes_available', 'colors_available', 'care_instructions')
        }),
        ('Meta', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def preview_image(self, obj):
        primary = obj.get_primary_image()
        if primary:
            return format_html('<img src="{}" style="height:60px;border-radius:6px"/>', primary.image.url)
        return '—'

admin.site.register(Product, ProductAdmin)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'product_count', 'preview_image', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

    def product_count(self, obj):
        return obj.products.count()

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:40px;border-radius:4px"/>',
                obj.image.url
            )
        return '—'

admin.site.register(Collection, CollectionAdmin)