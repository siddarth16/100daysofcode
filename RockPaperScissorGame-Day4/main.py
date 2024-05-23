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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

program_choice = random.randint(0,2)

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose:")
if program_choice == 0:
    print(rock)
elif program_choice == 1:
    print(paper)
else:
    print(scissors)

if user_choice == 0 and program_choice == 2:
    print("You win!")
elif user_choice == 0 and program_choice == 1:
    print("You lose!")
elif user_choice == 0 and program_choice == 0:
    print("Draw!")
elif user_choice == 1 and program_choice == 0:
    print("You win!")
elif user_choice == 1 and program_choice == 2:
    print("You lose!")
elif user_choice == 1 and program_choice == 1:
    print("Draw!")
elif user_choice == 2 and program_choice == 1:
    print("You win!")
elif user_choice == 2 and program_choice == 0:
    print("You lose!")
elif user_choice == 2 and program_choice == 2:
    print("Draw!")
