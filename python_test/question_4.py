import random

def game_rounds():
    try:
        Hassan_score = 0
        Computer_score = 0

        n = int(input("Enter the number of rounds: "))
        for i in range(1, n+1):
            Hassan = input("Select Rock, Paper, or Scissor: ").lower()
            Computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
            print("Hassan selected: ", Hassan)
            print("Computer selected: ", Computer)

            if Hassan == "rock" and Computer == "paper":
                print("Computer Won")
                Computer_score += 1
            elif Hassan == "paper" and Computer == "scissor":
                print("Computer Won")
                Computer_score += 1
            elif Hassan == "scissor" and Computer == "rock":
                print("Computer Won")
                Computer_score += 1
            elif Hassan == Computer:
                print("Tie")
            else:
                print("Hassan Won")
                Hassan_score += 1

        print(f"Hassan: {Hassan_score}")
        print(f"Computer: {Computer_score}")

        if Hassan_score > Computer_score:
            print("Hassan is the overall winner!")
        elif Computer_score > Hassan_score:
            print("Computer is the overall winner!")
        else:
            print("It's a tie!")

    except Exception as e:
        print('Something went wrong')
        print('Error reason: ', e)

game_rounds()

#Rules:
#Rock wins against scissors; paper wins against rock; and scissors wins against paper.
# If both players throw the same hand signal, it is considered a tie,
# and play resumes until there is a clear winner.

#Hassan Computer   winner
#rock     paper     Computer  (paper)
#rock     scissor   Hassan    (rock)
#paper    rock      Hassan    (paper)
#paper    scissor   Computer  (scissor)
#scissor  rock      Computer  (rock)
#scissor  paper     Hassan    (scissor)