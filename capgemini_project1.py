import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(player, computer):
    if player == computer:
        return 'tie'
    wins = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    if wins[player] == computer:
        return 'player'
    return 'computer'

def play_game():
    player_score = 0
    computer_score = 0
    rounds = 0

    print('Welcome to Rock Paper Scissors!')
    print('Type rock, paper, or scissors (or quit to exit)')
    print('-' * 42)

    while True:
        player = input('Your choice: ').lower().strip()

        if player == 'quit':
            break

        if player not in ['rock', 'paper', 'scissors']:
            print('Invalid choice! Try again.')
            continue

        computer = get_computer_choice()
        print('Computer chose:', computer)

        result = get_winner(player, computer)
        rounds += 1

        if result == 'tie':
            print('Result: It is a Tie!')
        elif result == 'player':
            print('Result: You Win!')
            player_score += 1
        else:
            print('Result: Computer Wins!')
            computer_score += 1

        print('Score -> You:', player_score, '| Computer:', computer_score)
        print('-' * 42)

    print('Game Over! Total Rounds:', rounds)
    print('Final -> You:', player_score, '| Computer:', computer_score)

play_game()