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

#Write your code below this line 👇
print("Welcome to Rock-Paper-Scissors.")
print("==================================")
user_choice = int(input('Type "1" for rock, "2" for paper or "3" for scissors: '))

choices = [rock, paper, scissors]
robot_choices = random.choice(choices)
print(f"\nComputer chose {robot_choices}")
print(f"\nYou chose {choices[int(user_choice)-1]}")

if (user_choice == 1 and robot_choices == rock):
  print("You tied!")
elif (user_choice == 1 and robot_choices == paper):
  print("Robot wins! Nice try")
elif (user_choice == 1 and robot_choices == scissors):
  print("You win!")
elif (user_choice == 2 and robot_choices == paper):
  print("You tied!")
elif (user_choice == 2 and robot_choices == scissors):
  print("Robot wins! Nice try")
elif (user_choice == 2 and robot_choices == rock):
  print("You win!")
elif (user_choice == 3 and robot_choices == scissors):
  print("You tied!")
elif (user_choice == 3 and robot_choices == rock):
  print("Robot wins! Nice try")
elif (user_choice == 3 and robot_choices == paper):
  print("You win!")
else:
  print("Invalid input.")