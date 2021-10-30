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

game_choices = [rock, paper, scissors]
user_input = int(input("Make your choose: Rock, Paper or Scissors, type 0,1 or 2: \n"))
invalid = True
while invalid:
    if user_input >= 3 or user_input < 0:
        print("You have entered a invalid number. Try again!!")
        user_input = int(input("Make your choose: Rock, Paper or Scissors, type 0,1 or 2: \n"))
    else:
        invalid = False
computers_choice = game_choices[random.randint(0, 2)]
user_choice = game_choices[user_input]

print(f"You chose: {user_choice} The computer chose: {computers_choice}")

if user_choice != computers_choice:
    if user_choice == paper and computers_choice == rock:
        print("You win!")
    elif user_choice == rock and computers_choice == scissors:
        print("You win!")
    elif user_choice == scissors and computers_choice == paper:
        print("You win!")
    else:
        print("You lose!")
else:
    print("Its a draw")
