from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)
    companyURL = models.URLField
    description = models.TextField()
    startYear = models.CharField(max_length=4)
    endYear = models.CharField(max_length=4)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})    
