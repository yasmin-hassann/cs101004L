
def displayMenu():
    while True:
        print("Enter your choice:")
        print("1 for Chipotle")
        print("2 for Q39")
        print("3 for Both restaurants")
        print("==>",end="")
        #read choice from the user 
        choice = int(input())
        #not a valid option 
        if not(choice>=1 and choice<=3):
            print("Enter a valid option")
        else: #valid option enter 
            return choice 
def chipotle():
    print("Chipotle Menu : ")
    print("1- Chicken burrito $7.95")
    print("2- Steak burrito bowl $ 9.30")
    print("3- Chicken Quesadilla $8.50")
    print("Enter 1/2/3 to add items to your order")    
    itemChoice = int(input())
    while True:
        print("Enter your quantity")
        quantity = int(input()) #read quantity
        if quantity>=1 and quantity<=3:
            
            break 
        else:
            print("Enter a valid quantity")
            
    if itemChoice==1:
        total=7.95*quantity
        print("You ordered option",choice, "with quantity",quantity)
        print("your total for now is",total)
    elif itemChoice==2:
        total=9.30*quantity
        print("You ordered option",choice, "with quantity",quantity)
        print("your total for now is",total)
    elif itemChoice==3:
        total=8.50*quantity
        print("You ordered option",choice, "with quantity",quantity)
        print("your total for now is",total)
        
    return total

    

def q39_menu():
    print("Q39 Menu: ")
    print("1- Wings $13.25 ")
    print("2- Burnt End Burger $ 16.50 ")
    print("3- Brisket $12.99 ")
    print("Enter 1/2/3 to add items to your order")    
    itemChoice = int(input())
    
    
    while True:
        
        
        print("Enter your quantity")
        quantity = int(input()) #read quantity
        if quantity>=1 and quantity<=3:
           
            break 
        else:
            print("Enter a valid quantity")

    if itemChoice==1:
        total=13.25*quantity
        print("You ordered option",choice, "with quantity",quantity)
        print("your total for now is",total)
    elif itemChoice==2:
        total=16.50*quantity
        print("You ordered option",choice, "with quantity",quantity)
        print("your total for now is",total)
        
    elif itemChoice==3:
        
        total=12.99*quantity
        print("You ordered option",choice, "with quantity",quantity)
        print("your total for now is",total)
        
    return total
    
        


    
def calculateDeliveryFee(total):
    
    
    if total<35:
        
        return 10
    elif total>35:
        return 0



#driver     
print("Welcome to 101 DELIVERY")
print("We deliver from any of these 2 restaurants")
print("1- Chipotle")
print("2- Q39")
print("3- Both restaurants")
choice = displayMenu()
if choice==1:
    total=chipotle()
    cont=input('\nDo you want to add anything else?N/Y:')
    if(cont=='y' or cont=='Y'):#when press n/N,check total
        chipotle()
    else:
        calculateDeliveryFee()
                
elif choice ==2:
    total = q39_menu()
    cont=input('\nDo you want to add anything else?N/Y:')
    if(cont=='y' or cont=='Y'):#when press n/N,check total
        chipotle()
    elif (cont == 'n' or cont =='N'):
       calculateDeliveryFee()
    else:
        print("wrong output,try again")
    cont=input('\nDo you want to add anything else?N/Y:')
           

elif choice == 3:
    print("***First store:***")
    chipotle()
    
    print("***Second store:***")
    q39_menu()
else:
    print("Enter a valid option")

      
   
deliverFee=calculateDeliveryFee()
print("Your total is $"+str(total)+" before tax and deliver fee")
Includingtax = deliverFee + total*0.043+total    
print("Your order total after tax and delivery fee is $",str(Includingtax))



            






























