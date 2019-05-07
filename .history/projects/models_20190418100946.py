from django.db import models

class Project(models.Model):
    projectKey = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    teaser = models.CharField(max_length=200)
    thumb = models.ImageField(default='project.png')
    
    def __str__(self):
        return self.title

    