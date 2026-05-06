import random

player_input = input("Choose [r]ock, [p]aper, [s]cissors: ")

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
player_move = ''

if player_input == 'r':
    player_move = rock
elif player_input == 'p':
    player_move = paper
elif player_input == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid input. Try again...')
computer_random_number = random.randint(1, 3)

computer_move = ''

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

# switch cases
if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print('You win!')
elif player_move == computer_move:
    print('Draw!')
else:
    print('You lose!')
