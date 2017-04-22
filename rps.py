# Rock Paper Scissors

from random import randint

name = input("What is your name? ")
print("\nHello %s! Welcome to the Rock, Paper, Scissors's game. \nRemember the rules: rock beats scissors; paper beats rock; scissors beats paper. \nYou have to accumulate three points to win the game. Let's play!" % (name))
player_score = 0
comp_score = 0  

while True:
    list_choise = ["rock", "paper", "scissors"]
    player_choise = input("\n%s, do you want to choose rock, paper or scissors? " % (name)).lower()
    comp_choise = list_choise[randint(0,2)]
    
    if player_choise == comp_choise:
        print("    It's a tie! \n    Score: %s %s : %s Computer" % (name, player_score, comp_score))
    elif player_choise == "rock":
        if comp_choise == "scissors":
            player_score += 1
            print("    Your rock beats computer's scissors! \n    Score: %s %s : %s Computer" % (name, player_score, comp_score))         
        else:
            comp_score += 1
            print("    Computer´s paper beats your rock! \n    Score: %s %s : %s Computer" % (name, player_score, comp_score))
    elif player_choise == "scissors":
        if comp_choise == "paper":
            player_score += 1
            print("    Your scissors beats computer's paper! \n    Score: %s %s : %s Computer" % (name, player_score, comp_score))            
        else:
            comp_score += 1
            print("    Computer´s rock beats your scissors! \n    Score: %s %s : %s Computer" % (name, player_score, comp_score))            
    elif player_choise == "paper":
        if comp_choise == "rock":
            player_score += 1
            print("    Your paper beats computer's rock! \n    Score: %s %s : %s Computer" % (name, player_score, comp_score))           
        else:
            comp_score += 1
            print("    Computer´s scissors beats your paper! \n    Score: %s %s : %s Computer" % (name, player_score, comp_score))
    else:
        print("    Invalid input! You have not entered rock, paper or scissors, try again. \n    Score: %s %s : %s Computer" % (name, player_score, comp_score))
    if player_score == 3 or comp_score == 3:
        print("\nTotal score: %s %s : %s Computer" % (name, player_score, comp_score))
        if player_score > comp_score:
            print("Congratulations %s! You win!" % (name))
        else:
            print("You lose %s, don't worry, try it again." % (name))
        if input("\nRepeat the program? (Y/N)").strip().upper() != 'Y':
            break
        else:
            player_score = 0
            comp_score = 0
            print("Let's get started again, %s!" % (name))
            continue
    



