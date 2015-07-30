from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
