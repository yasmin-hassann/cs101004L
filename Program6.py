
#Yasmin Hassan
#cs101

class Store:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def display(self):
        print("User placed order from: ", self.name, "at address: ", self.location)


class Cart(Store):
    products = {
        "Milk": 2.50,
        "Bread": 1.98,
        "Egg": 0.70,
        "Flour": 1.18,
        "Oil": 4.00,
        "Cheese": 2.68
    }

    def __init__(self):
        self.cart = {}
        self.receipt = 0

    def add_item(self, item, quantity):
        if item not in self.cart:
            self.cart[item] = quantity
        else:
            self.cart[item] += quantity
        self.receipt += self.products[item] * (quantity)

    def remove_item(self, item, quantity):
        if item not in self.cart:
            print("Item not in cart.")
            return

        if self.cart[item] == quantity:
            del self.cart[item]
        elif self.cart[item] > quantity:
            self.cart[item] -= quantity
        else:
            print("Quantity not available.")
            return

        self.receipt -= self.products[item] * (quantity)

    def display(self):
        super().display()
        print("Order in cart is: ")
        for item, quantity in self.cart.items():

            print(item, "with quantity: ", quantity)
        print("Total receipt is $", round(self.receipt,1))
        


cart = Cart()
name = input("Good morning! Which store you want to use today?\n>>> ")
cart.set_name(name)
location = input("Which location you want to use?\n>>> ")
cart.set_location(location)

print("Products as follow:")
for product, price in cart.products.items():
    print(product, "$", price)

while True:
    try:

        item = input("Enter name of your product\n>>> ")
        quantity = int(input("Enter quantity\n>>> "))

        cart.add_item(item, quantity)
        cart.display()

        remove = input("Do you want to remove an item(Yes/No)\n")
        if remove.lower()=="yes":
            item = input("Enter name of your product(remove)\n>>> ")
            quantity = int(input("Enter quantity\n>>> "))
            cart.remove_item(item, quantity)
            #print("User placed order from {} at address: {}".format(cart.name, cart.location))
            cart.display()
        add_product = input("Do you want to add another product (yes/no)\n>>> ")
        if add_product.lower() == "yes":
            product_name = input("Enter name of your product\n>>> ")
            quantity = int(input("Enter quantity\n>>> "))

            cart.add_item(product_name, quantity)
            # Output the user's updated order
            #print("User placed order from :{} at address: {}".format(cart.name, cart.location))
            cart.display()
            remove = input("Do you want to remove an item(Yes/No)\n")
            if remove == "yes":
                continue
              
              
            else:
                
                add = input("Do you want to add another product (Yes/No)\n>>> ").lower()
                if add =="yes":
                    continue
                else:
                    break
              
              
            #add = input("Do you want to add another product (Yes/No)\n>>> ").lower()
            #if add== "no":
              #break
        else:
            break
    except ValueError:
        print("Invalid input. Please try again.")
    except KeyError:
        print("Invalid product name. Please try again.")
