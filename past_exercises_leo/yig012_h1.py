#oppgave 1
'''I only import the one function from the math lib as it is the only one used in the exercise.
Since the question asked me to use pi as the function name i rename pi to pii'''
from math import pi as pii


def pi(d : int = -1) -> float or str:
    """rounds pi to the number of decimals given in the argument. Pi from math is given with 15 decimals, thus the function returns pii with 15 decimals
    and a mesage telling the user about the error.

    Args:
        d (int, optional): Number of decimals. Defaults to -1, -1 is outside the range of possible decimals, however it could be anything.

    Returns:
        float or str: Using this method makes digits after 15 decimals unknown, hence a costum error message.
    """
    if d == -1:
        return round(pii,2)
    elif d >= 0 and d<16:
        return round(pii, d)
    elif d > 15:
        return str(pii) + f' {d} is {d-15} to many decimals'

#function call for all conditions
print(pi())
print(pi(5))
print(pi(20))




#oppgave 2

def temk(t : float, c : str = 'c') -> str:
    """Function that takes degrees and unit and converts it to the opposite. if units left empty it defaults to celcius.

    Args:
        t (float): degrees, as float not int incase we wanna convert all numbers
        c (str, optional): The type, Celcius or fahrenheit. Defaults to 'c'.

    Returns:
        str: degrees (t) converted, rounded to two decimals + their respective sign, as the same datatype
    """
    if c in 'Cc': # I could've done: 'c == 'c' or c == 'C':', but it is longer.
        t = t*1.8+32
        return str(round(t, 2)) + u"\N{degree fahrenheit}"
    elif c in 'Ff':
        t = (t-32)*5/9
        return str(round(t, 2)) + u"\N{degree celsius}"

#function calls for all conditions
print(temk(2000))
print(temk(2.5, 'C'))
print(temk(0, 'c'))
print(temk(30, 'F'))
print(temk(0, 'f'))


#oppgave 3
from time import sleep
'''
i declare some global variables. The balance, an empty list to store the previous transactions, and the interest rate, which changes if the balance exceeds 1mil.
I add to the list when running relevant functions to keep track of the history for 3b. 
I use list.insert(0, elemt) so that every new element is at the start of the list. 
I could also use append and use -1 steps (list[::-1]) when using list slicing later on, however, I decided that this looked cleaner.

'''
saldo = 500
rentesats = 0.01
historikk = []

def inskudd(x : float = 0) -> float:
    """Deposits money in account after. 

    Args:
        x (float, optional): [The amount of money entered]. Defaults to 0.

    Returns:
        float: [The new account balance, also changes the interest rate if the balance exceeds 1mil]
    """
    global saldo
    global rentesats
    saldo += x
    historikk.insert(0, f'+ {x}')
    if saldo >= 1_000_000:
        print('Du får bonusrente!')
        rentesats = 0.02

def uttak(x : float = 0) -> float:
    """[Withdrawal from account]

    Args:
        x (float, optional): [removes amount of argument]. Defaults to 0.

    Returns:
        float: [new account balance given that the withdrawal does not exceed the total balance in the account in which case the function returns None with an error message. 
        Also, changes interest rate given that the new balance is less than 1mil]
    """
    global saldo
    global rentesats
    saldo1 = saldo
    if saldo - x < 0:
        print('overtrekk')
        return None
    saldo -= x
    historikk.insert(0, f'- {x}')
    if saldo < 1_000_000 and saldo1 >= 1_000_000:
        print('Du har nå ordinær rente!')
        rentesats = 0.01


def beregnRente() -> float:
    """[calculates the amount of interest that is gathered, and is stored as a global variable]

    Returns:
        float: [amount of interest]
    """
    global rente
    rente = saldo * rentesats
    print(rente)


def renteoppgjør() -> float:
    """[finds the balance + the interest rate after one period, if the balance is greater than 1m then interest rate is updated]
    """
    global rentesats
    global saldo
    saldo1 = saldo
    saldo = saldo + saldo * rentesats
    historikk.insert(0, f'+ {saldo * rentesats}')
    if saldo >= 1_000_000 and saldo1 < 1_000_000:
        print('Du får bonusrente!')
        rentesats = 0.02


def velg():
    """Makes a menu, imported time for this one because I made the function run in a loop and it felt weird when the function ran instantly after the input from the user.
    I did the loop to make it easy for you (Mr/Mrs seminar leader) to test even though it wasn't specifically asked for.
    My solution uses conditional execution where the input from the user runs one of the functions defined above. 
    The exeption is when the input is 5 and it runs a loop that prints the first three elements in the history list defined earlier, and since I used 
    list.insert instead of list.append I don't have to use negative steps.
    """
    sleep(0.5)
    print('''
-----------------------
1 - vis saldo
2 - inskudd
3 - uttak
4 - renteoppgjør
5 - historikk
-----------------------''')
    handling = int(input('velg handling: '))

    if handling == 1:
        print(saldo)
    elif handling == 2:    
        x = float(input('beløp: ')) 
        inskudd(x)
    elif handling == 3:    
        x = float(input('beløp: ')) 
        uttak(x)
    elif handling == 4:
        renteoppgjør()
    elif handling == 5:
        for i in historikk[:3]:
            print(i)

while True: 
    velg()
#^comment the lines above if you want to test my other functions!