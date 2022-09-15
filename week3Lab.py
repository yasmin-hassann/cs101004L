print("Welcome to Flarsheim Guesser!")
choice='y' #assign a variable 

while(choice == 'Y' or choice == 'y'):
    print("\nPlease think of a number between and including 1 and 100.")

    reminder_of_3=0
    reminder_of_5=0
    reminder_of_7=0

    reminder_of_3 = int(input("\nWhat is the remainder when your number is divided by 3 ?")) # getting a reminder from the user and assign a variable
    while(reminder_of_3 < 0 or reminder_of_3 >= 3): 
        if reminder_of_3 < 0 :
            print("The value entered must be 0 or greater") # execute this code as long as the expression is true
        elif reminder_of_3 >= 3 :
            print("The value entered must be less than 3")
        reminder_of_3 = int(input("What is the remainder when your number is divided by 3 ?"))

    reminder_of_5 = int(input("\nWhat is the remainder when your number is divided by 5 ?"))

    while(reminder_of_5 < 0 or reminder_of_5 >= 5):

        if reminder_of_5 < 0 :
            print("The value entered must be 0 or greater")
        elif reminder_of_5 >= 5 :
            print("The value entered must be less than 5")

        reminder_of_5 = int(input("What is the remainder when your number is divided by 5 ?"))

    reminder_of_7 = int(input("\nWhat is the remainder when your number is divided by 7 ?"))
    while(reminder_of_7 < 0 or reminder_of_7 >= 7 ):
        if reminder_of_7 < 0 :
            print("The value entered must be 0 or greater")
        elif reminder_of_7 >= 7 :
            print("The value entered must be less than 7")

        reminder_of_7 = int(input("What is the remainder when your number is divided by 7 ?"))


    for i in range(1,101): # in returns a boolean range  generates a sequence of number starting at 1, and ending 101
        if(i%3 == reminder_of_3 and i%5 == reminder_of_5 and i%7 == reminder_of_7):
            print("Your number was",i)
            print("How amazing is that?\n")


    choice=input("Do you want to play again? Y to continue,N to quit ==>")
    while(choice != 'Y' and choice != 'N' and choice != 'y' and choice != 'n' ):
        choice=input("Do you want to play again? Y to continue,N to quit ==>")


    





    

