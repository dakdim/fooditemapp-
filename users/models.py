from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    # auta auta user ko auta auta profile huncha jo chai one to one connected huncha
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
    

