
#Yasmin Hassan
#cs101

#function to print only the Transaction ID and Names
def id_name(user_input):
    
    try:
        fileName = open(user_input,'r')
        print('Reading data.....')
        readFile = fileName.readlines()
        print ("{:<8} {:<10} {:<10}".format('ID','FirstName','LastName'))
        for line in readFile:
            listWord = line.split(' ')
            name_of_the_ID = print("{:<8} {:<10} {:<10}".format(listWord[0],listWord[1],listWord[2]))
    except:
    
        print('Enter correct file name')



def file(user_input):
    try:
        fileName = open(user_input,'r')
        print('Reading data.....')
        print ("{:<8} {:<10} {:<10} {:<10} {:<10} {:<10}".format('ID','FirstName','LastName','Before','After','Saved'))
        readFile = fileName.readlines()
        for line in readFile:
            listWord = line.split(' ')
            float_Number = float(listWord[3])
            saved = round(float_Number*0.40,2)
            after =  float_Number - saved
            all = print ("{:<8} {:<10} {:<10} {:<10} {:<10.2f} {:<10.2f}".format(listWord[0],listWord[1],listWord[2],listWord[3],after,saved))
    except:
        print('Enter correct file name')
#infinite loops to print 
def main():
    
    while True:
        print('1-Print Transaction ID and username')
        print('2- Print username, total before and total after discount')
        print('3- Quit')
        option = input('Enter your choice ==> ')
        while option != '1' and option != '2' and option != '3':
            print('Enter valid option')
            option = input('Enter your choice ==> ')
            continue
        if option == '1':
            user_inputFile = input('Enter file name ==> ')
            while user_inputFile != 'input.txt':
                print('Enter correct file name')
                user_inputFile = input('Enter file name ==> ')
                continue
            id_name(user_inputFile)
        if option == '2':
            user_inputFile = input('Enter file name ==> ')
            while user_inputFile != 'input.txt':
                print('Enter correct file name')
                user_inputFile = input('Enter file name ==> ')
                continue
            file(user_inputFile)
        if option == '3':
            print('Have a great day')
            break
        require = input('Do you want to see more option Y/N: ')
        if require.upper() == 'Y':
            continue
        elif require.upper() == 'N':
            print('Have a great day')
            break
if __name__=='__main__':
    main()
