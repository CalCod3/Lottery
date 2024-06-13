from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BetSlip(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    normal_numbers = models.TextField()
    star_numbers = models.TextField()
    date = models.DateTimeField(auto_now_add= True, editable= False)
    
    def __str__(self):
            return f"Lottery Entry - {self.owner.username}"
        
