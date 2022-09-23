from django.db import models
from django.contrib.auth.models import User

 
    
class task(models.Model):
    unique_user = models.ForeignKey(User, on_delete=models.CASCADE)
    tasktitle = models.CharField(max_length=50)
    taskdesc = models.TextField()

    def __str__(self):
        return self.tasktitle
