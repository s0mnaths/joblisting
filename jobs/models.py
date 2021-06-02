from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=250)
    logo_url = models.CharField(max_length=500)

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField()
    link = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
