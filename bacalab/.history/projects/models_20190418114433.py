from django.db import models

class Project(models.Model):
    projectKey = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    teaser = models.TextField(max_length=200)
    thumb = models.ImageField(default='static/projects/project.png', upload_to='projects/static/projects')
    
    def __str__(self):
        return self.title

    