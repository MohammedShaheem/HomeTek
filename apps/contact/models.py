from django.db import models

# Create your models here.

class ContactUs(models.Model):
    email  = models.EmailField()
    phone   = models.CharField(max_length=20, blank=True,null=True)
    address = models.CharField(max_length=150,null=True,blank=True)
    image = models.ImageField(upload_to='contact/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'ContactUs'
        ordering = ['-created_at']

    