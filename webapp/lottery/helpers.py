import random

def generate_winning_numbers():
    normal_numbers = sorted(random.sample(range(1, 51), 5))
    star_numbers = sorted(random.sample(range(1, 13), 2))
    return normal_numbers, star_numbers

def calculate_prize(entry, winning_numbers):
    normal_numbers = [int(num) for num in entry.normal_numbers.split(',')]
    star_numbers = [int(num) for num in entry.star_numbers.split(',')]
    
    normal_matches = len(set(normal_numbers) & set(winning_numbers[0]))
    star_matches = len(set(star_numbers) & set(winning_numbers[1]))

    if normal_matches == 5 and star_matches == 2:
        return "Jackpot Prize"
    elif normal_matches == 5:
        return "Normal Prize 1"
    elif normal_matches == 4 and star_matches == 2:
        return "Normal Prize 2"
    elif normal_matches == 4 and star_matches == 1:
        return "Normal Prize 3"
    elif normal_matches == 4:
        return "Normal Prize 4"
    elif normal_matches == 3 and star_matches == 2:
        return "Normal Prize 5"
    elif normal_matches == 3 and star_matches == 1:
        return "Normal Prize 6"
    elif normal_matches == 3:
        return "Normal Prize 7"
    elif normal_matches == 2 and star_matches == 2:
        return "Normal Prize 8"
    elif normal_matches == 2 or star_matches == 2:
        return "Normal Prize 9"
    else:
        return "No Prize"

