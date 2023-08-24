import random
import time
import os

# Function to generate random positions
def generate_positions(num, width, height):
    return [{'x': random.randint(0, width - 1), 'y': random.randint(0, height - 1)} for _ in range(num)]

# Function to print the grid
def print_grid(width, height, players, enemies, uncommons, special_char):
    print("  " + " ".join([chr(65 + x) for x in range(width)]))  # Print letter labels
    for y in range(height):
        print(str(y + 1).rjust(2) + " ", end="")
        for x in range(width):
            is_player = any(player['x'] == x and player['y'] == y for player in players)
            is_enemy = any(enemy['x'] == x and enemy['y'] == y for enemy in enemies)
            is_uncommon = any(uncommon['x'] == x and uncommon['y'] == y for uncommon in uncommons)
            is_special = special_char['x'] == x and special_char['y'] == y
            
            if is_player:
                print('X', end=' ')
            elif is_enemy:
                print('O', end=' ')
            elif is_uncommon:
                print('U', end=' ')
            elif is_special:
                print('B', end=' ')
            else:
                print('.', end=' ')
        print()

    print("\nCharacter Locations:")
    print("X:", ", ".join([chr(65 + player['x']) + str(player['y'] + 1) for player in players]))
    print("O:", ", ".join([chr(65 + enemy['x']) + str(enemy['y'] + 1) for enemy in enemies]))
    print("U:", ", ".join([chr(65 + uncommon['x']) + str(uncommon['y'] + 1) for uncommon in uncommons]))
    print("B:", chr(65 + special_char['x']) + str(special_char['y'] + 1))

# Main loop
while True:
    # Get grid dimensions from the player
    grid_width = int(input("Enter the width of the game board: "))
    grid_height = int(input("Enter the height of the game board: "))
    
    total_grid_size = grid_width * grid_height
    
    # Calculate the number of characters based on grid size
    num_players = max(1, int(total_grid_size * 0.02))  # 2% of grid size
    num_enemies = max(1, int(total_grid_size * 0.01))  # 1% of grid size
    num_uncommons = max(0, int(total_grid_size * 0.01))  # 1% of grid size
    
    players = generate_positions(num_players, grid_width, grid_height)
    enemies = generate_positions(num_enemies, grid_width, grid_height)
    uncommons = generate_positions(num_uncommons, grid_width, grid_height)
    
    # Initialize the special character 'B'
    special_char = {'x': grid_width // 2, 'y': 0}
    
    # Loop for interacting with the game board
    while True:
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print_grid(grid_width, grid_height, players, enemies, uncommons, special_char)
        
        print("\nPress Enter to update the game board, press 'j' to jump 'B', or press 'q' to change dimensions.")
        
         # Check if 'B' landed on the same tile as 'U', 'O', or 'X'
        overlapped_character = None
        overlapped_type = ''
        
        for uncommon in uncommons:
            if uncommon['x'] == special_char['x'] and uncommon['y'] == special_char['y']:
                overlapped_character = uncommon
                overlapped_type = 'U'
                break
        
        if not overlapped_character:
            for enemy in enemies:
                if enemy['x'] == special_char['x'] and enemy['y'] == special_char['y']:
                    overlapped_character = enemy
                    overlapped_type = 'O'
                    break
        
        if not overlapped_character:
            for player in players:
                if player['x'] == special_char['x'] and player['y'] == special_char['y']:
                    overlapped_character = player
                    overlapped_type = 'X'
                    break
        
        if overlapped_character:
            print(f"'{overlapped_type}' character landed on 'B' at", chr(65 + special_char['x']) + str(special_char['y'] + 1))
        
        choice = input()
        if choice == '':
            # Generate random positions for X, O, and U characters
            players = generate_positions(num_players, grid_width, grid_height)
            enemies = generate_positions(num_enemies, grid_width, grid_height)
            uncommons = generate_positions(num_uncommons, grid_width, grid_height)
        elif choice.lower() == 'j':
            # Move the special character 'B' randomly within 30ft
            special_char['x'] = random.randint(max(0, special_char['x'] - 3), min(grid_width - 1, special_char['x'] + 3))
            special_char['y'] = random.randint(max(0, special_char['y'] - 3), min(grid_height - 1, special_char['y'] + 3))
            
            # Randomly update the rest of the board
            players = generate_positions(num_players, grid_width, grid_height)
            enemies = generate_positions(num_enemies, grid_width, grid_height)
            uncommons = generate_positions(num_uncommons, grid_width, grid_height)
        elif choice.lower() == 'q':
            break
