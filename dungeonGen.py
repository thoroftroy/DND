import random
import time

# Function to convert an index to a letter
def get_coord(index):
    return chr(index + ord('A'))

# Function to write all the information to a file
def write_to_file(game_board, tile_coords, file_name):
    game_board_lines = [' '.join(row) for row in game_board]
    game_board_text = '\n'.join(game_board_lines)

    tile_coord_strings = print_tile_coords(game_board)  # Use the function to generate the formatted strings

    file_content = game_board_text + "\n\n" + tile_coord_strings

    with open(f"{file_name}.txt", "w") as f:
        f.write(file_content)

# Function to create an initial game board state
def create_initial_game_board(width, height):
    game_board = [['.' for _ in range(width)] for _ in range(height)]
    return game_board

# Function to randomly place 'R's around the game board
def place_random_Rs(game_board):
    width = len(game_board[0])
    height = len(game_board)
    num_Rs = int((width * height) / 40)  # Adjust the divisor for your preference

    for _ in range(num_Rs):
        x = random.randint(2, width - 3)
        y = random.randint(2, height - 3)
        game_board[y][x] = 'R'

# Function to calculate the box size based on proximity of 'R's
def calculate_box_size(x, y, width, height):
    min_distance = min(x, y, width - x - 1, height - y - 1)
    if min_distance <= 2:
        return random.choice([(2, 2), (2, 3), (3, 2)])
    else:
        return random.choice([(3, 3), (3, 4), (4, 3), (4, 4), (5, 6)])

# Function to add W boxes around each R
def add_w_boxes(game_board):
    width = len(game_board[0])
    height = len(game_board)

    for y in range(height):
        for x in range(width):
            if game_board[y][x] == 'R':
                box_width, box_height = calculate_box_size(x, y, width, height)

                for ny in range(max(0, y - (box_height // 2)), min(height, y + (box_height // 2) + 1)):
                    for nx in range(max(0, x - (box_width // 2)), min(width, x + (box_width // 2) + 1)):
                        if game_board[ny][nx] != 'R':
                            game_board[ny][nx] = 'W'
                for ny in range(max(0, y - (box_height // 2) + 1), min(height, y + (box_height // 2))):
                    for nx in range(max(0, x - (box_width // 2) + 1), min(width, x + (box_width // 2))):
                        if game_board[ny][nx] != 'R':
                            game_board[ny][nx] = '.'

# Function to convert 'R's to other room types
def convert_Rs_to_rooms(game_board):
    width = len(game_board[0])
    height = len(game_board)
    num_Rs = sum(row.count('R') for row in game_board)

    # Create a list of unique room types
    unique_rooms = ['E', 'B', 'S']
    random.shuffle(unique_rooms)

    # Choose 3 random R's for unique room types ('E', 'B', 'S')
    for room_type in unique_rooms:
        while True:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            if game_board[y][x] == 'R':
                game_board[y][x] = room_type
                break

    # Remaining count after placing unique room types
    num_remaining_Rs = num_Rs - len(unique_rooms)

    # Calculate the counts for each room type
    num_Ms = int(num_remaining_Rs * 0.85)
    num_Ts = num_remaining_Rs - num_Ms

    # Create the room types list for remaining R's
    room_types = ['M'] * num_Ms + ['T'] * num_Ts

    # Replace remaining R's with room types
    for y in range(height):
        for x in range(width):
            if game_board[y][x] == 'R':
                room_type = random.choice(room_types)
                game_board[y][x] = room_type
                room_types.remove(room_type)

def print_tile_coords(game_board):
    width = len(game_board[0])
    height = len(game_board)

    tile_coords = {'E': [], 'B': [], 'S': [], 'T': [], 'M': []}

    for y in range(height):
        for x in range(width):
            tile = game_board[y][x]
            if tile in tile_coords:
                tile_coords[tile].append(f"{get_coord(x)}{y + 1}")

    print("\nStart Room:")
    for coord in tile_coords['S']:
        print(coord)
        
    print("Exit:")
    for coord in tile_coords['E']:
        print(coord)

    print("Boss Room:")
    for coord in tile_coords['B']:
        print(coord)

    print("Treasure Rooms:")
    print(', '.join(tile_coords['T']))

    print("Monster Rooms:")
    print(', '.join(tile_coords['M']))
    
    tile_coord_strings = []

    tile_coord_strings.append("Start Room:")
    tile_coord_strings.extend(tile_coords['S'])

    tile_coord_strings.append("Exit:")
    tile_coord_strings.extend(tile_coords['E'])

    tile_coord_strings.append("Boss Room:")
    tile_coord_strings.extend(tile_coords['B'])

    tile_coord_strings.append("Treasure Rooms:")
    tile_coord_strings.append(', '.join(tile_coords['T']))

    tile_coord_strings.append("Monster Rooms:")
    tile_coord_strings.append(', '.join(tile_coords['M']))

    return '\n'.join(tile_coord_strings)
                
# Function to print the game board with coordinates
def print_game_board(game_board):
    width = len(game_board[0])
    height = len(game_board)

    print("  " + " ".join([chr(65 + x) for x in range(width)]))
    for y in range(height):
        print(str(y + 1).rjust(2) + " " + " ".join(game_board[y]))

# Main function
def main():
    tile_coords = {'E': [], 'B': [], 'S': [], 'T': [], 'M': []}  # Initialize tile_coords here
            
    width = int(input("Enter the width of the dungeon: "))
    height = int(input("Enter the height of the dungeon: "))

    game_board = create_initial_game_board(width, height)
    print_game_board(game_board)

    input("Press Enter to place 'R's on the game board...")
    place_random_Rs(game_board)
    print("\nGame board after placing 'R's:")
    print_game_board(game_board)

    input("\nPress Enter to add W boxes around the 'R's...")
    add_w_boxes(game_board)
    print("\nGame board after adding W boxes:")
    print_game_board(game_board)

    input("\nPress Enter to convert 'R's to other room types...")
    convert_Rs_to_rooms(game_board)
    print("\nGame board after converting 'R's to rooms:")
    print_game_board(game_board)

    print_tile_coords(game_board)
    
    # Ask if the user wants to write the board to a file
    write_file_choice = input("Do you want to write the board to a file? (y/n): ")
    if write_file_choice.lower() == 'y':
        file_name = input("Enter the file name: ")
        write_to_file(game_board, tile_coords, file_name)  # Pass tile_coords to the function
            
    # Ask if the user wants to create a new dungeon
    new_dungeon_choice = input("Do you want to create a new dungeon? (y/n): ")
    if new_dungeon_choice.lower() == 'y':
        main()
    else:
        print("Exiting the program.")

# Run the main function
if __name__ == "__main__":
    main()
