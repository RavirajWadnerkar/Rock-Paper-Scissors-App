def print_hand(hand, player_name):
    print(player_name + ' picked: ' + hand)

print('Starting the Rock Paper Scissors game!')

# Get input, and then assign it to the player_name variable
player_name = input('Please enter your name: ')
# Add a second argument to print_hand
print_hand('Rock' , player_name)