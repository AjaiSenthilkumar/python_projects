import random

def play():
    user = input('Enter your choice (r) for Rock, (s) Scissor, (p) Paper : ')
    computer = random.choice(['r', 's', 'p'])
    
    if user == computer:
        return 'It is a tie'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost'

def is_win(player, opponent):
    # Return True if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
          or (player == 'p' and opponent == 'r'):
        return True
    
play()
