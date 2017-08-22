from django.db import models
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    detail_time = models.CharField(max_length=20)
    content = models.TextField()
    url = models.URLField()
    source = models.CharField(max_length=50)
    web = models.CharField(max_length=50)
    logtime = models.CharField(max_length=30)
    def __str__(self):
        return self.title
