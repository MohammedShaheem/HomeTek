from django.db import models

# Create your models here.

class SocialPlatform(models.TextChoices):
    INSTAGRAM = "instagram", "Instagram"
    FACEBOOK = "facebook", "Facebook"
    LINKEDIN = "linkedin", "LinkedIn"
    TIKTOK = "tiktok", "TikTok"
    YOUTUBE = "youtube", "YouTube"


class SocialProfile(models.Model):
    platform = models.CharField(
        max_length=20,
        choices=SocialPlatform.choices,
        unique=True,
    )

    handle = models.CharField(max_length=100)

    url = models.URLField(max_length=500)

    icon = models.CharField(
        max_length=50,
        blank=True,
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Social Profile"
        verbose_name_plural = "Social Profiles"

    