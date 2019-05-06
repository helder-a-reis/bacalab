from django.db import models

class Job(models.Model):
    PROFESSIONAL = 'PROF'
    EDUCATION = 'EDU'
    JOB_TYPES = (
        (PROFESSIONAL, 'Professional'),
        (EDUCATION, 'Education'),
    )
    jobType = models.CharField(max_length=10, choices=JOB_TYPES, default=PROFESSIONAL)
    title = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)
    companyURL = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    startYear = models.CharField(max_length=4)
    endYear = models.CharField(max_length=4, blank=True)
    description = models.TextField()

    def __str__(self):
        return (self.title + ', ' + self.companyName)
