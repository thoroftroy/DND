import random
import time

def roll_dice(num_dice, sides):
    rolls = []
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, sides)
        rolls.append(roll)
        time.sleep(0.05)  # Add a 0.1-second delay
        print(f"Roll: {roll}")
        total += roll
    print(f"Total: {total}")

def bad_weighted_dice(num_dice, sides):
    rolls = []
    total = 0
    for _ in range(num_dice):
        # Weighted towards lower values (e.g., more 1s)
        roll = random.choices(range(1, sides+1), weights=[5]*(sides//2) + [1]*(sides//2))[0]
        rolls.append(roll)
        time.sleep(0.05)  # Add a 0.1-second delay
        print(f"Roll: {roll}")
        total += roll
    print(f"Total: {total}")

def good_weighted_dice(num_dice, sides):
    rolls = []
    total = 0
    for _ in range(num_dice):
        # Weighted towards higher values (e.g., more 8s)
        roll = random.choices(range(1, sides+1), weights=[1]*(sides//2) + [5]*(sides//2))[0]
        rolls.append(roll)
        time.sleep(0.05)  # Add a 0.1-second delay
        print(f"Roll: {roll}")
        total += roll
    print(f"Total: {total}")

while True:
    input_str = input("Enter the dice roll (e.g., '3d8' or 'q' to quit: ")
    
    if input_str.lower() == 'q':
        break
    
    if input_str == "d4":
        print("Rolled: ",random.randint(1,4))
    elif input_str == "d6":
        print("Rolled: ",random.randint(1,6))
    elif input_str == "d8":
        print("Rolled: ",random.randint(1,8))
    elif input_str == "d10":
        print("Rolled: ",random.randint(1,10))
    elif input_str == "d12":
        print("Rolled: ",random.randint(1,12))
    elif input_str == "d20":
        print("Rolled: ",random.randint(1,20))
    else:
        input_parts = input_str.lower().split()  # Convert to lowercase
        
        if len(input_parts) == 2 and input_parts[0] == 'bad' or input_parts[0] == 'good':
            num_dice, sides = map(int, input_parts[1].split('d'))
        else:
            num_dice, sides = map(int, input_str.split('d'))
            
        if input_parts[0] == 'bad':
            bad_weighted_dice(num_dice, sides)
        elif input_parts[0] == 'good':
            good_weighted_dice(num_dice, sides)
        else:
            roll_dice(num_dice, sides)
