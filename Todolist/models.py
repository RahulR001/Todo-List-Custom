from django.db import models

# Create your models here.


class user(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password1 = models.CharField(max_length=20)
    password2  = models.CharField(max_length=20) 

    def __str__(self):
        return self.name
    
class task(models.Model):
    unique_user = models.ForeignKey(user, on_delete=models.CASCADE)
    tasktitle = models.CharField(max_length=50)
    taskdesc = models.TextField()

    def __str__(self):
        return self.tasktitle
