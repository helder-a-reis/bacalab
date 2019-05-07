from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    projectKey = models.CharField(max_length=20)
    teaser = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})