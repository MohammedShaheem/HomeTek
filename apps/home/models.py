from django.db import models
from django.utils.text import slugify

# Create your models here.

class BlogPost(models.Model):
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True, blank=True)
    cover_image = models.ImageField(upload_to='blog/')
    content     = models.TextField()               
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)