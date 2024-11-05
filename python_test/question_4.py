import random

from janitor.plugincore.exceptions import ComputerJanitorException


def game_rounds():
    try:
        n = int(input("Enter the number of rounds: "))
        for i in range(1, n+1):
            player1 = input("Select Rock, Paper, or Scissor :").lower()
            computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
            print("player 1 selected: ", player1)
            print("computer selected: ", computer)

            if player1 == "rock" and computer == "paper":
                print("computer Won")
            elif player1 == "rock" and computer == "scissor":
                print("Player1 Won")
            elif player1 == "paper" and computer == "rock":
                print("Player1 Won")
            elif player1 == "paper" and computer == "scissor":
                print("Computer Won")
            elif player1 == "scissor" and computer == "rock":
                print("Computer Won")
            elif player1 == computer:
                print("Tie")
            else:
                print("Player 1 Won")
    except Exception as e:
        print('Something went wrong')
        print('Error reason: ', e)

game_rounds()

#Rules:
#Rock wins against scissors; paper wins against rock; and scissors wins against paper.
# If both players throw the same hand signal, it is considered a tie,
# and play resumes until there is a clear winner.

#Player1 Computer   winner
#rock     paper     Computer
#rock     scissor   Player1
#paper    rock      Player1
#paper    scissor   Computer
#scissor  rock      Computer
#scissor  paper     Player1