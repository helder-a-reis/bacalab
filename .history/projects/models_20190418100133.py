from django.db import models

class Project(models.Model):
    projectKey = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    teaser = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    thumb = models.ImageField(null=True)
    
    def __str__(self):
        return self.title

    