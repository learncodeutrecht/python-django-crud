from django.db import models

# Create your models here.
class Task(models.Model):
	title = models.TextField(max_length=100)
	description = models.TextField(max_length=200)
	date = models.DateField(auto_now_add=True)
	deadline = models.DateField()
	urgent = models.BooleanField()
	important = models.BooleanField()

	def __str__(self):
		return self.task + " by " + self.author
    
