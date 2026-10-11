import random

def play():
    player = input("what's your choice? 'r' for rock ,'s' for scissor, 'p' for paper: ")
    computer = random.choice(['r', 's', 'p'])

    if player == computer: # r>s, s>p, p>r
        return "draw"

    if is_win(player, computer):
        return "you won!"

    return "you lost!"

def is_win(player, opponent): # return true if player wins and false if loose!

    if(player == "r" and opponent == "s")\
         or (player == "r" and opponent == "p") \
        or (player == "p" and opponent == "r"):
        return True
    return False

print((play())) 
    

    