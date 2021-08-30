from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    link = models.URLField()
    release_date = models.DateField()

    def __str__(self):
        return self.title

