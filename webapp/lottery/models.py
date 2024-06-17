from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Draw(models.Model):
    draw_date = models.DateTimeField(auto_now_add=True)
    normal_numbers = models.CharField(max_length=50)
    star_numbers = models.CharField(max_length=50)

class BetSlip(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    normal_numbers = models.TextField()
    star_numbers = models.TextField()
    date = models.DateTimeField(auto_now_add= True, editable= False)
    draw = models.ForeignKey(Draw, on_delete=models.CASCADE)
    prize = models.CharField(max_length=50, default="No Prize")
    
    def __str__(self):
            return f"Lottery Entry - {self.owner.username}"
