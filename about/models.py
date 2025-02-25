from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=20)
    designation = models.TextField()
    address = models.TextField()
    image = models.ImageField(upload_to="about/images/")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "About"