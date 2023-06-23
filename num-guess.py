import random
import math

lower = int(input("Lower bound : "))
upper = int(input("Upper bound : "))

randomNumber = random.randint(lower, upper)
chances = round(math.log(upper - lower + 1, 2))
print("You have only ",chances," chances to guess the integer!")

count = 0

while count < chances :
    count += 1
    
    userInput = int(input("Number : "))
    if( userInput < randomNumber ):
         print("Try Again! You guessed too small")
    elif( userInput > randomNumber ):
         print("Try Again! You guessed too high")
    elif( userInput == randomNumber ):
         print("Congratulations! , You did it in ",count," try!")
         count += 1
         break

if count == chances:
    print("The number is ", randomNumber)
    print("Better luck next time!")              
