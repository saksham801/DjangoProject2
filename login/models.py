from django.db import models

# Create your models here.
class login(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    phone_no = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
