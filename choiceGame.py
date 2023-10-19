import random 
user_score=0 
computer_score=0
Total=0
game_choices=["rock","paper","scissors"]

while True:
    user_pick=input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_pick=="q":
        break
    if user_pick not in game_choices:
        continue
    random_number=random.randint(0,2)
    computer_pick=game_choices[random_number]

    if user_pick=="rock" and computer_pick=="paper":
        print("Yee! You won :)")
        user_score+=1
        Total+=1
    elif user_pick=="paper" and computer_pick=="rock":
        print("Yee! You won :)")
        user_score+=1
        Total+=1
    elif user_pick=="scissors" and computer_pick=="paper":
        print("Yee! You Won :)")
        user_score+=1
        Total+=1
    else:
        print("Computer Wins :(")
        Total+=1

print("Your Total Score out of ",Total , " is" , user_score)
    