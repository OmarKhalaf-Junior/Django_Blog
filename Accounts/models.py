from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    bio= models.TextField(null= True, blank= True)
    birth_date= models.DateField(null= True, blank= True)
    location= models.CharField(max_length= 150, null= True, blank= True)

    def __str__(self):
        return str(self.user)
