#Yasmin Hassan


# define class house
class House:
    def __init__(self,year,initial_price,location=None,current_value=0):
        self.year=year
        self.initial_price=initial_price
        self.location=location
        self.current_value=current_value
    def calculate_value(self,current_year):
        age=current_year-self.year
        self.current_value=int(self.initial_price*((1+0.08)**age))
        
    def __str__(self):
        print("-"*17)
        print("House Information:")
        print("\tYear Built: ",self.year)
        print("\tPurchase Price: ",self.initial_price)
        print("\tCurrent value of House: ",self.current_value)
        print("\tLocation: ",self.location)
        print("-"*17)
    def Money_earned(self):
        print("\n"*3)
        print("Total value you will earn :")
        print(self.current_value-self.initial_price)
        print("-"*17)

       
while(True):
    print("Welcome to our house calculation app")
    while(True):
        year=int(input("Enter House model year: "))
        if(year<0 or year==0):
            print("Enter a valid year")
        else:
            break
    while(True):
        initial_price=int(input("Price of the House: "))
        if(initial_price<=0):
            print("Enter a valid price")
        else:
            break
    while(True):
        current_year=int(input("Current year: "))
        if(current_year<=year):
            print("Enter a valid year")
        else:
            break
    location=input("Enter your house location: ")
    obj=House(year,initial_price,location)
    obj.calculate_value(current_year)
    obj.__str__()
    obj.Money_earned()

    repeat=input("Do you want to check price of another house?Y/N : ")
    if(repeat=="Y"):
        continue
    else:
        break
