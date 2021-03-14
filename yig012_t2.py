#Oppgave 1

from math import pi #imports pi from the math library, since its the only thing I'll use in this exercise it felt redundant to import the whole library
radius = float(input('Radius: ')) #promts the user to enter a radius
area = round((radius**2)*pi, 3) #defines a variable as the area, and rounds it to 3 decimals 
print(area)

#oppgave 2

sentance = input('sentance: ') #prompts user to enter a sentance
guess = int(input('Guess: ')) #prompts the user to guess the length of his sentance, and converts it to the data-type int
sentance = sentance.replace(' ', '') #removes whitespace (' ') so that the length does not include it (len('hej jeg er glad') -> 12 (not 15), could also be done with commas etc
#Line 12 is not a part of the exercise but I felt it made sense so why not :D
print(f"That's {len(sentance) == guess}!!") #prints a f-string with a bool, hence True or False
#Personally I would've solved this using conditional execution btw

#oppgave 3

from random import randint #Same logic as in 1
number = input('Give me a number: ') #Prompts user to enter a number (this is already a string)
rnumber= str(randint(1, 10)) #new variable is a random number between 1-10 (has to be a string so that 1+2 = 12 (see line 20))
answer = int(number+rnumber)/int(number) #finds the answer of the sum of the two strings given above divided by the old number (convertet to ints (answer is float))
print(number+rnumber, '/', number,' = ', answer, sep='') #print, removed whitespace beacuase that's what it looked like in the exercise