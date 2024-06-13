from django.shortcuts import redirect, render
from . import models
from .forms import LotteryEntryForm
from .helpers import calculate_prize, generate_winning_numbers
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def enter_lottery(request):
    if request.method == 'POST':
        form = LotteryEntryForm(request.POST)
        if form.is_valid():
            # Extract selected numbers and stars from form data
            selected_numbers = [int(num) for num in request.POST.getlist('normal_numbers')]
            selected_stars = [int(star) for star in request.POST.getlist('star_numbers')]
            
            
            # Convert selected numbers and stars into strings
            numbers_str = ','.join(str(e) for e in selected_numbers)
            stars_str = ','.join(str(e) for e in selected_stars)
            
            # Create LotteryEntry instance and save to database
            entry = form.save(commit=False)
            entry.owner = request.user  # Assign the current logged-in user to the bet slip
            entry.normal_numbers = numbers_str
            entry.star_numbers = stars_str
            entry.save()
            
            return redirect('view_lottery_results')
    else:
        form = LotteryEntryForm()
    return render(request, 'lottery/enterlottery.html', {'form': form})


@login_required
def view_lottery_results(request):
    normal_numbers, star_numbers = generate_winning_numbers()
    entries = models.BetSlip.objects.all()
    results = []

    for entry in entries:
        prize = calculate_prize(entry, (normal_numbers, star_numbers))
        results.append({'entry': entry, 'prize': prize})

    return render(request, 'lottery/view_lottery_results.html', {'results': results, 'normal_numbers': normal_numbers, 'star_numbers': star_numbers})