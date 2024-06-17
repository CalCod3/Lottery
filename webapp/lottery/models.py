import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_next_friday():
    today = datetime.date.today()
    days_until_friday = (4 - today.weekday() + 7) % 7
    if days_until_friday == 0:  # If today is already Friday, move to next Friday
        days_until_friday = 7
    next_friday = today + datetime.timedelta(days=days_until_friday)
    return next_friday

class Draw(models.Model):
    draw_date = models.DateTimeField(default=get_next_friday)
    normal_numbers = models.CharField(max_length=50)
    star_numbers = models.CharField(max_length=50)

class BetSlip(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    normal_numbers = models.TextField()
    star_numbers = models.TextField()
    date = models.DateTimeField(auto_now_add= True, editable= False)
    draw = models.ForeignKey(Draw, on_delete=models.CASCADE, null=True, blank=True)
    prize = models.CharField(max_length=50, default="No Prize")
    
    def __str__(self):
            return f"Lottery Entry - {self.owner.username}"
