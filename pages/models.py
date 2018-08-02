from django.db import models

# Create your models here.
class page(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	last_update = models.DateTimeField(auto_now_add=True)

	def _str_(self):
		return self.title
