from django.db import models

# Create your models here.
class Thoughts(models.Model):
    thought = models.TextField(max_length=100)
    thoughttype = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.thought + " by " + self.author
    