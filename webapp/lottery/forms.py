from django import forms
from .models import BetSlip

class LotteryEntryForm(forms.ModelForm):
    class Meta:
        model = BetSlip
        fields = ['normal_numbers', 'star_numbers']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)