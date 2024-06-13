from django import forms
from .models import BetSlip

class LotteryEntryForm(forms.ModelForm):
    class Meta:
        model = BetSlip
        fields = ['normal_numbers', 'star_numbers']
