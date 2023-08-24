import random
import time
import os

#This program is designed for a boss fight I am doing, The X's mark spots of dark energy which hurt the player, the O's are spots of healing energy wich heal the player and the U's are unstable ground in which the players could fall. Each turn the game state changes randmoly.


# Function to generate random positions
def generate_positions(num, width, height):
    return [{'x': random.randint(0, width - 1), 'y': random.randint(0, height - 1)} for _ in range(num)]

# Function to print the grid
def print_grid(width, height, players, enemies, uncommons):
    for y in range(height):
        for x in range(width):
            is_player = any(player['x'] == x and player['y'] == y for player in players)
            is_enemy = any(enemy['x'] == x and enemy['y'] == y for enemy in enemies)
            is_uncommon = any(uncommon['x'] == x and uncommon['y'] == y for uncommon in uncommons)
            
            if is_player:
                print('X', end=' ')
            elif is_enemy:
                print('O', end=' ')
            elif is_uncommon:
                print('U', end=' ')
            else:
                print('.', end=' ')
        print()

# Main loop
while True:
    # Get grid dimensions from the player
    grid_width = int(input("Enter the width of the game board: "))
    grid_height = int(input("Enter the height of the game board: "))
    
    total_grid_size = grid_width * grid_height
    
    # Calculate the number of characters based on grid size
    num_players = max(1, int(total_grid_size * 0.02))  # 2% of grid size
    num_enemies = max(1, int(total_grid_size * 0.01))  # 1% of grid size
    num_uncommons = max(0, int(total_grid_size * 0.005))  # 0.5% of grid size
    
    players = generate_positions(num_players, grid_width, grid_height)
    enemies = generate_positions(num_enemies, grid_width, grid_height)
    uncommons = generate_positions(num_uncommons, grid_width, grid_height)
    
    # Loop for interacting with the game board
    while True:
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print_grid(grid_width, grid_height, players, enemies, uncommons)
        print("\nPress Enter to update the game board or press 'q' to change dimensions.")
        
        choice = input()
        if choice == '':
            # Generate random positions for X, O, and U characters
            players = generate_positions(num_players, grid_width, grid_height)
            enemies = generate_positions(num_enemies, grid_width, grid_height)
            uncommons = generate_positions(num_uncommons, grid_width, grid_height)
        elif choice.lower() == 'q':
            break
