from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)
    companyURL = models.CharField()
    startYear = models.CharField(max_length=4)
    endYear = models.CharField(max_length=4)
    description = models.TextField()

    def __str__(self):
        return (self.title + ', ' + self.companyName)
