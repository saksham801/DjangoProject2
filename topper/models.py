from django.db import models

# Create your models here.

class topper(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    display = models.CharField(max_length=100)
    score = models.FloatField(default=0)  # Add score field

    def __str__(self):
        return self.name
