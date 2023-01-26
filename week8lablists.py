# function to calculate the mean
def mean(a):

    if(len(a) == 0):

        return 0

    else:

        sum = 0.0

        for i in a:

            sum += i

        return sum/len(a)


# Function to calculate standard deviation

def std(mean, a):

    sqrt_sum = 0.0

    for i in a:

        sqrt_sum += (i - mean)**2

    return (sqrt_sum/len(a))**0.5

# Function to calculate weighted score

# Function to display result

def display(test, assignment):



# number of tests

    num_test = len(test)

# number of assignment

    num_assignment = len(assignment)

# weighted score

    weighted = 0.0

    print("Type       #     min      max         avg          std")

    print("====================================================== ")

    if(num_test == 0):

        test_min = "n/a"

        test_max = "n/a"

        test_avg = "n/a"

        test_std = "n/a"

        print("Tests       0      n/a     n/a       n/a       n/a")

    else:

        test_min = min(test)

        test_max = max(test)

        test_avg = mean(test)

        test_std = std(test_avg, test)

        weighted += test_avg*0.6

        print("Tests       %d      %.2f     %.2f    %.2f    %.2f"%(num_test, test_min, test_max, test_avg, test_std))


    if(num_assignment == 0):

        assignment_min = "n/a"

        assignment_max = "n/a"

        assignment_avg = "n/a"

        assignment_std = "n/a"

        print("Programs     0     dn/a    n/a     n/a     n/a")

    else:

        assignment_min = min(assignment)

        assignment_max = max(assignment)

        assignment_avg = mean(assignment)

        assignment_std = std(assignment_avg, assignment)

        weighted += assignment_avg*0.4

        print("Programs     %d    %.2f    %.2f    %.2f     %.2f"%(num_assignment, assignment_min, assignment_max, assignment_avg, assignment_std))

        print()
    print()

    print("The weighted scores is   %.2f"%(weighted))

# Main function

def main():

# list to store test scores

    test_scores = []

# list to strore assignment scores

    assignment_scores = []

# Loop will run until user quits

    while (True):


# printing menu

        print()

        print(" Grade Menu")

        print("1 - Add Test")

        print("2 - Remove Test")

        print("3 - Clear Tests")

        print("4 - Add Assignment")

        print("5 - Remove Assignment")

        print("6 - Clear Assignments")

        print("D - Display Scores")

        print("Q - Quit")

# getting user choice

        print()

        choice = (input("==> "))

        if (choice == '1'):
            
            print()

            temp = float(input("Enter the new Test score 0-100 ==> "))

# validating input

            while (temp < 0):

                temp = float(input("Enter the new Test score 0-100 ==> "))

            test_scores.append(temp)

        elif (choice == '2'):


            print()

            temp = float(input("Enter the Test to remove 0-100 ==> "))

            removed = False # to store status of remove

            for i in test_scores:


                if (i == temp):

                    test_scores.remove(temp)

                    removed = True

            if(removed == False):

                print("Could not find that score to remove")

        elif (choice == '3'):
             
                
                

            test_scores.clear()

        elif (choice == '4'):
                
            print()

            temp = float(input("Enter the new Assignment score 0-100 ==> "))

# validating input

            while (temp < 0):
                

                temp = float(input("Enter the new Assignment score 0-100 ==> "))

            assignment_scores.append(temp)

        elif (choice == '5'):

            print()

            temp = float(input("Enter the Assignment to remove 0-100 ==> "))

            removed = False # to store status of remove

            for i in assignment_scores:
                if (i == temp):
                    
                    assignment_scores.remove(temp)

                    removed = True

            if(removed == False):
                print("Could not find that score to remove")

        elif (choice == '6'):

            assignment_scores.clear()

        elif (choice == 'D' or choice == 'd'):

            display(test_scores, assignment_scores)

        elif (choice == 'Q' or choice == 'q'):

            break

        else:

            print("Please choose correct option.")



main()
