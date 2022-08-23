from django.db import models

# Create your models here.

class Link(models.Model):
    long_url=models.CharField(max_length=300)
    short_url=models.CharField(max_length=15)


    def __str__(self):
        return self.short_url
