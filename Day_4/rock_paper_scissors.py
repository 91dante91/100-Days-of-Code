import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

figures = [rock, paper, scissors]
random_figure = random.randint(0, len(figures) - 1)
computer = figures[random_figure]

while True:
    correct_number = False
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if player_choice > len(figures) or player_choice < 0:
        print("You entered an incorrect number")
    else:
        correct_number = True

    if correct_number:
        player = figures[player_choice]
        print(player)
        print("Computer choose:\n", computer)

        if player == rock and computer == scissors:
            print("You win!")
        elif player == scissors and computer == paper:
            print("You win!")
        elif player == paper and computer == rock:
            print("You win!")
        elif player == computer:
            print("It's a draw")
        else:
            print("You lose")
        break
