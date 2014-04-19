from django.db import models

# Create your models here.

class Items(models.Model):
	name = models.CharField(max_length = 200)
	location = models.CharField(max_length = 500)
	stock = models.IntegerField()

	def __unicode__(self):
		return self.name