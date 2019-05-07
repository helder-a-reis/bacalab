from django.db import models

class Project(models.Model):
    projectKey = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    teaser = models.TextField(max_length=200)
    thumb = models.ImageField(default='project.png', upload_to='project_thumbs')
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

class Ilustration(models.Model):
    picture = models.ImageField(default=None, upload_to='project_images')
    caption = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        name = self.project.title + "/" + self.caption
        return name
