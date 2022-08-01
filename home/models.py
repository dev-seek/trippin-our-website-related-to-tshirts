from django.db import models

# Create your models here.
# below is written manually
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self): 
        return self.name