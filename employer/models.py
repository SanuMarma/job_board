from django.db import models
from django.contrib.auth.models import User
from .constants import JOB_TYPES, JOB_LEVELS, QUALIFICATION_TYPES, EXPERIENCE_TYPES

# Create your models here.
class Industry(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
        return self.name
    
class Location(models.Model):
    address = models.CharField("Address", max_length=250)
    slug = models.SlugField(max_length = 40)

    def __str__(self):
            return self.address

    
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    website = models.URLField("Link to website", max_length=250, blank=True)
    logo = models.ImageField(upload_to="employer/images/")
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, null=True)
    location =  models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    job_type = models.CharField(choices = JOB_TYPES, max_length = 30)
    job_level = models.CharField(choices = JOB_LEVELS, max_length = 30) 
    experience = models.CharField(choices = EXPERIENCE_TYPES, max_length = 30, null=True) 
    salary = models.CharField(max_length = 20) 
    updated = models.DateField()
    deadline = models.DateField()

    description = models.CharField(max_length = 1000, null=True)
    qualification = models.CharField(choices = QUALIFICATION_TYPES, max_length = 30, null=True)
    
    def __str__(self):
        return f"{self.industry} {self.industry}"
