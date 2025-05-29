from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    image_url = models.URLField()






    def __str__(self):
        return self.course_name


class Home_Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()

    def __str__(self):
        return self.course_name