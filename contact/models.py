from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 30)
    company = models.CharField(max_length = 30, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length = 12)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contact"