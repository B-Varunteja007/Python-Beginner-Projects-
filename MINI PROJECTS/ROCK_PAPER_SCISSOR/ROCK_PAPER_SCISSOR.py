import random
def check_win(user,computer):
    if(user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='s'):
        return True
def rock_paper_scissors():
    player=input("ENTER YOUR CHOICE IN ROCK PAPER AND SCISSOR ")
    choices=['r','s','p']
    opponent=random.choice(choices)
    if player==opponent:
        return print(f"Its is a Tie! choice is {opponent}")
    if check_win(player, opponent):
        return print(f"Yay! you won! Choice is {opponent}")
    if check_win(player, opponent) != True:
        return print(f"You lost! Choice is {opponent}")
rock_paper_scissors()