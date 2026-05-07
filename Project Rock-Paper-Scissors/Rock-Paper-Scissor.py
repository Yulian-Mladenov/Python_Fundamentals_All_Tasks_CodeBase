player_points_counter = 0
computer_points_counter = 0
number_of_rounds = 0

while True:
    import random

    player_input = input("Choose [r]ock, [p]aper, [s]cissors: ")
    number_of_rounds += 1

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
        while True:
            if player_input != 'r' and player_input != 's' and player_input != 'p':
                player_input = input("Your input is wrong! Please choose again only one of the next symbols: [r]ock, [p]aper, [s]cissors: ")
            else:
                player_move = player_input
                break

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
        print("\033[30;42mYou win!\033[0m")
        print(f"The computer chose: {computer_move}")
        print(f'Your points are: {player_points_counter}')
        print(f'The points of the computer are: {computer_points_counter}')
        print(f'The number of rounds are: {number_of_rounds}')
    elif player_move == computer_move:
        print("\033[30;43mDraw!\033[0m")
        print(f"The computer chose: {computer_move}")
        print(f'Your points are: {player_points_counter}')
        print(f'The points of the computer are: {computer_points_counter}')
        print(f'The number of rounds are: {number_of_rounds}')
    else:
        computer_points_counter += 1
        print("\033[30;41mYou lose!\033[0m")
        print(f"The computer chose: {computer_move}")
        print(f'Your points are: {player_points_counter}')
        print(f'The points of the computer are: {computer_points_counter}')
        print(f'The number of rounds are: {number_of_rounds}')

    while True:
        play_again = input("Play again? [yes/no]: ")
        if play_again == 'yes':
            break
        elif play_again == 'no':
            print('Thank you for playing!')
            print(f'Your points are: {player_points_counter}')
            print(f'The points of the computer are: {computer_points_counter}')
            print(f'The number of rounds are: {number_of_rounds}')
            raise SystemExit()
        else:
            print("Your input is wrong. If You want to play again, please write 'yes' or 'no'")

