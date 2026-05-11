from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Company(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='company_profile')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='company/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    JOB_TYPE = (
        ('fulltime', 'Full-time'),
        ('parttime', 'Part-time'),
        ('remote', 'Remote'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)
    about_company = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    salary = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='jobs/', null=True, blank=True) 
    def get_salary_display(self):
        if self.salary:
            return f"{self.salary:,} VND"
        return "Negotiable"

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class JobImage(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='job_images/')

    def __str__(self):
        return f"Image - {self.job.title}"