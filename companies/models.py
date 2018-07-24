from django.db import models

# Create your models here.
# Create your models here.
class Users(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=70,blank=True)
    name = models.CharField(max_length=25,unique=True)

    def __str__(self):
        return self.name