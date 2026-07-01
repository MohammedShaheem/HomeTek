from django.db import models

# Create your models here.

class Enquiry(models.Model):
    name         = models.CharField(max_length=100)
    email        = models.EmailField()
    phone        = models.CharField(max_length=20, blank=True)
    message      = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Enquiries'
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} — {self.submitted_at.strftime('%d %b %Y')}"