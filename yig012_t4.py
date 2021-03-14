
#oppgave 1
def fak(x : int) -> int:
    """[factorial]

    Args:
        x (int): [the number that is the factorial].

    Returns:
        int: [x!], if x<1 then return none
    """
    fak = 1
    if x < 1:
        return None
    for i in range (1, x+1):
        fak = fak*i
    return(fak)
#some function calls
print(fak(5))
print(fak(-5))

#method 2

def fac(x : int) -> int:
    fac = 1
    if x < 1:
        return None
    y = 1
    while y <= x:
        fac = y*fac
        y +=1
    return(fac)

#some function calls
print(fac(5))
print(fac(-5))

#I guess you can also do this using recurrsion, but the exercise didn't specifically ask for this so I didn't


#oppgave 2

class Monarc:
    def __init__(self, name, nation, year):
        self.name = name
        self.nation = nation
        self.year = year

    def write(self):
        """[prints the attributes of the object]
        """
        print(self.name, 'king of', self.nation, 'crowned in', self.year)

    def __repr__(self):
        """[makes the output of the object readable, could also use __repr__ to make it "unambigious".
        repr is more precise, however, str is more readable from what I understood
        and str is used for the end user. Hence I picked __str__ in this instance.]

        Returns:
            [type]: [str] [the info about the king]
        """
        return f'{self.name} king of {self.nation} crowned in {self.year}'

#made this unsorted to show that the program would sort this no matter how long the list was
list_of_kings = [
Monarc('Kong Haakon VII', 'Norway', 1905),
Monarc('Kong Harald V', 'Norway', 1991),
Monarc('Kong Olav V', 'Norway', 1957)
]

sortedlist = sorted(list_of_kings, key = lambda x: x.year)
print(*sortedlist, sep='\n')


#funccall of object, didn't want to make a list with variables that are objects because that'd be to much code
list_of_kings[0].write()

#task 2b
#Didn't really understand what the question was but I assume it refers to linked lists?
class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

#I create a linked list that lacks the functionality of inserting data at the tail since I will only need to insert at the head (also it's shorter ;) ), 
#since I have a list that has already sorted the kings in the right order
class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)
            itr = itr.next
            if itr is None:
                break
            llstr += ', Followed by: ' #the last three lines of this while loop are only here so that the output doesn't show how the last node points to None.
        print(llstr) #print of the string 

#create a linkedlist where each node is an element from the sorted list (backwards so that the head is the first king and the tail is the last one) and then print. If I was bothered to
#You can add as many objects as you want to [list_of_kings] since it impacts everything else
ll = Linkedlist()
for i in sortedlist[::-1]:
    ll.insert_at_start(i)
ll.print()

