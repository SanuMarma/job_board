from django.db import models
from seeker.models import Seeker
from employer.models import Employer, Industry
from .constants import APPLICATION_STATUS
# Create your models here.


class Application(models.Model):
    seeker = models.ForeignKey(Seeker, on_delete = models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete = models.CASCADE)
    application_status = models.CharField(choices = APPLICATION_STATUS, max_length = 10, default = "Pending")
    job_title = models.OneToOneField(Industry, on_delete=models.CASCADE, null=True)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to="application/files/")
    cancel = models.BooleanField(default = False)
    
    def __str__(self):
        return f"Job : {self.job_title} , Seeker : {self.seeker.user.first_name}"