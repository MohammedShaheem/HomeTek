from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name        = models.CharField(max_length=100)
    slug        = models.SlugField(unique=True, blank=True)
    image       = models.ImageField(upload_to='categories/', blank=True)
    description = models.TextField(blank=True)
    is_active   = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories'
    )
    name     = models.CharField(max_length=100)
    slug     = models.SlugField(blank=True)

    class Meta:
        verbose_name_plural = 'Sub-categories'
        ordering = ['name']
        unique_together = ('category', 'slug')

    def __str__(self):
        return f'{self.category.name} → {self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Collection(models.Model):
    name        = models.CharField(max_length=150)
    slug        = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    image       = models.ImageField(upload_to='collections/', blank=True)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    category    = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='products'
    )
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='products'
    )
    collection  = models.ForeignKey(
        Collection, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='products'
    )
    name             = models.CharField(max_length=200)
    slug             = models.SlugField(unique=True, blank=True)
    description      = models.TextField()
    material         = models.CharField(max_length=150, blank=True)
    sizes_available  = models.CharField(max_length=200, blank=True)
    colors_available = models.CharField(max_length=200, blank=True)
    care_instructions = models.TextField(blank=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_primary_image(self):
        primary = self.images.filter(is_primary=True).first()
        return primary or self.images.first()


class ProductImage(models.Model):
    product    = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images'
    )
    image      = models.ImageField(upload_to='products/')
    is_primary = models.BooleanField(default=False)


    class Meta:
        ordering = ['-is_primary']

    def __str__(self):
        return f'{self.product.name} — image'