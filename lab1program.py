#yasmin Hassan
#cs101
#due sep 11 

print("***APPLE PIE INGRIDIENTS***")
number_pies = int(input("How many pies do you need ==> "))
print()
print("For", number_pies,'pie(s) you will need:')
print()

pie_crust = 0
pie_apples = 0
pie_sugar = 0
pie_flour = 0
pie_cinnamon = 0
pie_salt = 0
pie_nutmeg = 0
pie_juices = 0



for x in range(number_pies):
    pie_crust += 1
    pie_apples += 6
    pie_sugar += 0.75
    pie_flour += 2
    pie_cinnamon += 0.75
    pie_salt += 0.25
    pie_nutmeg += 0.125
    pie_juices += 1

print(f"{pie_crust} pie crust(s)")
print(f"{pie_apples} Apples")
print(f"{pie_sugar} cups of sugar")
print(f"{pie_flour} Tablespoon of Flour")
print(f"{pie_cinnamon} Teaspoon of Cinnamon")
print(f"{pie_salt} Teaspoon of Salt")
print(f"{pie_nutmeg} Teaspoon of Nutmeg")
print(f"{pie_juices} Tablespoon of Lemon Juices")
