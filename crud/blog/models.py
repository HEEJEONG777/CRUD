from django.db import models

# Create your models here.
class Post(models.Model):
    def __str__(self):
        return self.title
        
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

class Human(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    food = models.TextField()