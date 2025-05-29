from django.db import models



# Create your models here.
class Course(models.Model):
    COURSE_TYPES = [
        ('MHT-CET', 'MHT-CET'),
        ('NEET', 'Neet'),
    ]
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    select_course_type = models.CharField(max_length=100, choices=COURSE_TYPES)
    image_url = models.URLField(null = True)

    def __str__(self):
        return self.course_name


class Toppers(models.Model):
    COURSE_TYPES = [
        ('MHT-CET', 'MHT-CET'),
        ('NEET', 'Neet'),
    ]
    topper_name = models.CharField(max_length=100)
    topper_course = models.CharField(max_length=100, choices=COURSE_TYPES)
    image_url = models.URLField(null = True)


    def __str__(self):
        return self.topper_name

class PopularCourse(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()

    def __str__(self):
        return self.course_name


class Newsettleer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()



    def __str__(self):
        return self.name
