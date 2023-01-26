#Yasmin Hassan
#Program2
#created 09/24/22
#due date09/25/22




import random


print('Welcome To TWO TRUTH AND A LIE')

# dictionary of statements with the correct choice
questions = {
  'I enjoy coding': True,
  'I played on a soccer team': False,
  'I love spicy food': True,
}

#a variable to store the number of valid responses
right_answers = 0

# running a bolean expression
while True:
  
  print()
  print()
  
  # use a random dictionary key
  random_key = random.choice(list(questions.keys()))

  
  answer = questions[random_key]

  # displaying the question to the user
  print('Truth or Lie??')
  print(random_key)

 
  print()
  print()

  # displaying the choices iteratively
  while True:
    print('1- Truth')
    print('2- Lie')

    # taking the user input
    choice = int(input('choice >>> '))

    # if choice is valid then break
    if (choice == 1 or choice == 2):
      break

    # if invalid choice
    print()
    print()
    print('Invalid Input')
    print('Please Enter A Valid Choice')

  
  print()
  print()

  # validating answer
  if (choice == 1 and answer == True) or (choice == 2 and answer == False):
    right_answers += 1 # increment the answer count

    # printing result
    print('Correct!!')
    print('You got this one correct!')
  else:
    # if answer is wrong
    print('Incorrect!!')
    print(f'You got {right_answers} correct out of {right_answers + 1}') # shoing the total and correct answers

    # requesting the user's want to play once more
    play_again = input('Do you want to play again?! (Y/N)\n')

    # if play again is n then break, continue otherwise
    if play_again.lower() == 'n':
      break
