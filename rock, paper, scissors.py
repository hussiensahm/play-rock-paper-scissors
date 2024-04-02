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

# Write your code below this line 👇
play = [rock, paper, scissors]
# Huomen Playing
choice1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("your play is :\n"+play[choice1])
# Mashien Playing

choice2 = random.randint(0, 2)
print("Computer playing is :\n" + play[choice2])

if choice1 == 0 and choice2 == 2:
    print("you win")
elif choice2 == 0 and choice1 == 2:
    print("you less")
elif choice1 > choice2:
    print("you win")
elif choice1 == choice2:
    print("you equle")
else:
    print("you less")
