from django.shortcuts import redirect, render
from django.urls import reverse

from .helpers import calculate_prize, generate_winning_numbers
from .models import BetSlip
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

@login_required
def enter_lottery(request):
    if request.method == 'POST':
        entries = []
        for i in range(1, 6):
            normal_numbers = request.POST.get(f'normal_numbers_{i}')
            star_numbers = request.POST.get(f'star_numbers_{i}')
            if normal_numbers and star_numbers:
                entries.append({
                    'normal_numbers': normal_numbers,
                    'star_numbers': star_numbers,
                })

        if not entries:
            return render(request, 'lottery/enter_lottery.html', {'error': 'Please fill at least one entry.'})

        for entry in entries:
            betslip = BetSlip(
                owner=request.user,
                normal_numbers=entry['normal_numbers'],
                star_numbers=entry['star_numbers'],
            )
            betslip.save()

        return redirect('view_lottery_results')
    else:
        return render(request, 'lottery/enter_lottery.html')

@login_required
def view_lottery_results(request):
    normal_numbers, star_numbers = generate_winning_numbers()
    # Filter entries belonging to the current user
    entries = BetSlip.objects.filter(owner=request.user)
    results = []

    for entry in entries:
        prize = calculate_prize(entry, (normal_numbers, star_numbers))
        results.append({'entry': entry, 'prize': prize})

    return render(request, 'lottery/view_lottery_results.html', {'results': results, 'normal_numbers': normal_numbers, 'star_numbers': star_numbers})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('enter_lottery')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect(reverse('login'))