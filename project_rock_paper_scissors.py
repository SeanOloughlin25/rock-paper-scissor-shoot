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

game_play_options = [rock, paper, scissors]
my_choice = int(input("Choose 0 for rock, 1 for paper, or 2 for scissors: "))
opponent_choice = random.randint(0,2)



print(f"{game_play_options[my_choice]}")
print(f"{game_play_options[opponent_choice]}")

if my_choice == 0:
    if opponent_choice == 0:
        print("draw")
    elif opponent_choice == 1:
        print("you lose")
    else:
        print("You win")
if my_choice == 1:
    if opponent_choice == 0:
        print("You Win")
    elif opponent_choice == 1:
        print("draw")
    else: 
        print("You lose")
if my_choice == 2:
    if opponent_choice == 0:
        print("You Lose")
    elif opponent_choice == 1:
        print("You Win")
    else:
        print("Draw")

    

