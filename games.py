import random
print("----------------------------------------------------------------------------------------")
user_choice=int(input("Enter your choice : 0 for 'ROCK' , 1 for 'PAPER' & 2 for 'SCISSORS': \n"));

if(user_choice >= 3 or user_choice < 0):
    print("You entered an invalid number")
else:
 print("You chossed :")
 if(user_choice==0):
    print("ROCK")
 if(user_choice==1):
    print("PAPER")
 if(user_choice==2):
    print("SCISSORS")
 computer_choice= random.randint(0,2)
 print("Computer chossed :")
 if(computer_choice==0):
    print("ROCK")
 if(computer_choice==1):
    print("PAPER")
 if(computer_choice==2):
    print("SCISSORS")
 
 # Deciding who win and who losses
 if(user_choice == computer_choice):
    print(" Match Draw \n Try Again")
 elif computer_choice==0 and user_choice==2:
    print(" You Lossed \n Try Again")
 elif user_choice==0 and computer_choice==2:
    print(" Congratulation \n You Win")
 elif(user_choice<computer_choice):
    print(" You Lossed \n Try Again ")
 elif(user_choice>computer_choice):
    print(" Congratulation \n You Win")




