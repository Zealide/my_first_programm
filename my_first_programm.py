def calculator ():
    #Getting user input and naming variables
    calculation = input ("What basic operator do you want to use? (+, -, *, /)\n")
    first_Number = int(input ("What is the first number?\n"))
    second_Number = int(input ("What is the second number?\n"))

    #Acting on user Input with if and elif
    if calculation == "+":
        print (f"{first_Number} + {second_Number} =", first_Number + second_Number)

    elif calculation == "-":
        print (f"{first_Number} - {second_Number} =", first_Number - second_Number)

    elif calculation == "*":
        print (f"{first_Number} * {second_Number} =", first_Number * second_Number)

    elif calculation == "/":

        if second_Number == 0:
            print("You cant divide with Zero")
        else:
            print (f"{first_Number} / {second_Number} =", first_Number / second_Number)
    else:
        print("Please give next time a valid first input")

def guess_a_number():
    import random #Important. We can use random because of this

    def guess(x):
        random_number = random.randint(1, x) #Getting a random_number within a threshold
        guess = 0 #Set Border for random_number

        while guess != random_number: #loop
            guess = int(input (f"Guess a number between 1 and {x}\n")) #Getting the users guess
            if guess < random_number:
                print("Sorry, your guess is too low")
            elif guess > random_number:
                print('Sorry, your guess is too high')
        print(f'Your guess is right. The Number was {random_number}')

    guess(10) #Setting border for the highest number possible

#Getting the user to choose what they want to do
user_input = input("What do you wanna do? Use the calculator or play a game of guess a number? (c = calculator and g = guess a number)\n")

if user_input == "c":
    calculator()

elif user_input == "g":
    guess_a_number()