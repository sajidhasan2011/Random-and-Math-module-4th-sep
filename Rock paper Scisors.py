import random

option = ["Rock" , "Paper" ,"Scissors" ]

user_choice = input("Choose Rock ,Paper , Scissors ")

computer_choice = random.choice(option)

print("You chose:" , user_choice)
print("Computer chose :", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")

elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock smashes scissors")
    
elif user_choice == "Paper" and computer_choice =="Rock":
    print("Paper Cover rock ! You win")
    
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cuts papre ! You win !")
    
else:
    print("You Lose Noob")