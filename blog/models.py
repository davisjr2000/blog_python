from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
      return self.title
