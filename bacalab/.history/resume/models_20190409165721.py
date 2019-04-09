from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)
    companyURL = models.URLField
    description = models.TextField()
    startYear = models.CharField(max_length=4)
    endYear = models.CharField(max_length=4)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})    
