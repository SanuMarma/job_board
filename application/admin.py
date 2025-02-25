from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'seeker_name', 'employer_name', 'application_status', 'cancel']
    def seeker_name(self,obj):
        return obj.seeker.user.first_name
    
    def employer_name(self,obj):
        return obj.employer.user.first_name
    
    def job_title(self,obj):
        return obj.job_title
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.application_status in ["Rejected", "Accepted"]:
            email_subject = "New Job Application"
            email_body = render_to_string('apply_email.html', {'user' : obj.seeker.user, 'job' : obj.job_title, 'application_status': obj.application_status}, )
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.seeker.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
    
            
admin.site.register(models.Application, ApplicationAdmin)