from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class CompanyProfile(models.Model):
    name = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='aboutus',blank=True,null=True)
    tagline = models.CharField(max_length=100,blank=True,null=True)
    about_text = models.TextField(blank=True,null=True)
    founded_year = models.PositiveIntegerField(blank=True,null=True)
    hero_image = models.ImageField(upload_to='aboutus',blank=True,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Company Profile'

    def __str__(self):
        return self.name
    
    def clean(self):
        if not self.pk and CompanyProfile.objects.exists():
            raise ValidationError('Only one Company Profile can exist. Edit the existing one.')
        
    def save(self,*args,**kwargs):
        self.full_clean()
        super().save(*args,**kwargs)

class VisionMission(models.Model):
    vision_title = models.CharField(max_length=200, default='Our Vision')
    vision_text = models.TextField(blank=True,null=True)
    mission_title = models.CharField(max_length=100,default='Our Mission')
    mission_text = models.TextField(blank=True,null=True)
    vision_image = models.ImageField(upload_to='aboutus/',blank=True,null=True)
    mission_image = models.ImageField(upload_to='aboutus/',blank=True,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Vision & Mission'
    
    def __str__(self):
        return 'Vision & Mission'
    
    def clean(self):
        if not self.pk and VisionMission.objects.exists():
            raise ValidationError('Only one Vision & Mission entry can exist. Edit the exisiting one.')
        
    
    def save(self,*args,**kwargs):
        self.full_clean()
        super().save(*args,**kwargs)
    
class WhyChooseUs(models.Model):
    ICON_CHOICES = [
        ('star', 'Star (OEM/ODM)'),
        ('globe', 'Globe (Markets)'),
        ('shield', 'Shield (Quality)'),
    ]
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='star',null=True,blank=True)
    title = models.CharField(max_length=150,null=True,blank=True)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Why Choose Us Card'
        verbose_name_plural = 'Why Choose Us Cards'
        ordering = ['order', 'id']

    def __str__(self):
        return self.title