from django.db import models

# Create your models here.
class Thought(models.Model):
    title = models.TextField(max_length=60)
    thought = models.TextField()


    def __str__(self):
        return self.title
    