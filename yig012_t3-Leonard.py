#oppgave 1

#The bool value of the first condition is false, the second one is flase
#I wrote a quick program that can check the bool for different values of x and y
x = 9 
y = 66

one = x != 7 and y <=50
two = (x > 7 or y > 50) and (x > y or y<100)

print(f'condition one: {one}, condtion two: {two}')

#oppgave 1b
#write the equivalent of the first expression in other syntax 
not (x == 7) and y <51

#oppgave 2

age = int(input('What is your age? '))
time_in_town = int(input('How long have you lived in Tulleby? '))

governer = age >= 30 and time_in_town >= 9
cityc = age >= 25 and time_in_town >= 5

if governer:
    print('you can become the governer or be in the city council')

elif cityc:
    if (30 - age) > (9 - time_in_town):
        print('you can become a council member', f'Try again in {30-age} years to become governor', sep='\n')

    elif (9 - time_in_town) > (30 - age):
        print('you can become a council member', f'Try again in {9-time_in_town} years to become governor', sep='\n')

else:
    if (25 - age) > (5 - time_in_town):
        print(f'you are not qualified try again in', 25-age, 'years')
    elif (25 - age) > (5 - time_in_town):
        print(f'you are not qualified try again in', 5-time_in_town, 'years')

#oppgave 3

x=int(input('number:'))

if x>5:
    if x<10 :
        print('6,7,8 eller 9')
    if x>=10:
        print('minst 10')
elif x <= 5:
    print('max 5')


x = '6, 7, 8, or 9' if x < 10