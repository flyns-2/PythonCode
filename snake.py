#numbers = [10,5,8,2,1]

#print ("la premiere liste", numbers)

#numbers[0] = 111
#print ("new list", numbers)

#numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
#print("New list contents:", numbers)  # Printi

# print ("a",numbers[len(numbers)//2])

# print (numbers[-1:])

liste = [8,10,6,2,4] # list a trié

for i in range(len(liste) -1): # ici on parcout tous la liste jusqu'à 
    print ( "a",i)
    if liste[i] > liste[i + 1]: # comparaison 
        liste[i], liste[i +1] = liste[i+1], liste[i]
print (liste)



my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
 
while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)

"""
my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
"""
#my_list[start:end]
WHITE_PAWN = "-"
row = []
for i in range (8):
    row.append(WHITE_PAWN)

print (row)


test = [WHITE_PAWN for i in range(8)]
print (test)


two = [2 ** i for i in range (8)]
print (two)


board = []
EMPTY = "/"
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

print (board)



temps = [[0.0 for h in range (24)] for d in range (31)]

total = 0.0
for day in temps :
    total += day[11] #ici a chaque fois que c'est 11 on additionne la temp
average = total / 31
print (average)



hightest = -100.0
for day in temps : #retourne la liste des 31 listes de 24 heures
    for temp in day:# rentre dans la liste des 24 heures et affiche le total des heures
        if temp > hightest:
            hightest = temp

print ("a",hightest)


hot_days = 0
for day in temps :
    if day[11] > 20.0:
        hot_days += 1
print (hot_days, "days were hot")


rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# rooms[0][0][0] nous permets de trouver un élément dedans
# rooms[1][3][5] trouve le batiment 1 etage 3 chambre 5
rooms [1][9][13] = True

vacancy =0
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

# print (rooms)

cubed = [num ** 3 for num in range(5)]
print (cubed)  # retourne 0,1,8,27,64

 
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print (table)
print (table[0][0])
print (table[0][3])

# Cube - a three-dimensional array (3x3x3)
 
cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],
 
        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],
 
        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'a']]]
print ("a")

print (cube)
print (cube[0][0][0])
print (cube[2][2][2])
z = 10
y = 0
x = y < z and z > y or y > z and z < y

print (x)
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)
my_list = [3, 1, -2]
print(my_list[my_list[-1]])


my_list = [1, 2, 3, 4]
print(my_list[-3:-2])


nums = [1, 2, 3]
vals = nums
del vals[1:2]


print (nums,'a', vals)


my_list = [1, 2, 3]
for v in range(len(my_list)):
    print ("v",v)
    my_list.insert(1, my_list[v])
print(my_list)





def boring_function():
    print("'Boredom Mode' ON.")
    return 123
 
print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")
print (boring_function())


def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    res = 28
    l1 =[4,6,9,11]
    if month == 2 and is_year_leap(year) == True:
        res = 29
    elif month in l1 :
        res = 30
    elif month not in l1 and month != 2:
        res = 31
    return res


def is_prime (num):
    res = True
    for i in range (2,num):
        if num % i == 0:
            res = False
    return res







my_list = [1,2,4,4,1,4,2,6,2,9]

l2 =  []

for i in my_list:
    if i not in l2:
        l2.append(i)

print (l2)


colors = (("green", "#008000"), ("blue", "#0000FF"))

colors = (("green", "#008000"), ("blue", "#0000FF"))

# Initialisation du dictionnaire vide
colors_dictionary = {}

# Boucle for pour remplir le dictionnaire
for color_name, color_code in colors:
    colors_dictionary[color_name] = color_code

print(colors_dictionary)

dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    # Insert your code here.
    print (k[0])
def func_1(a):
    return a ** a

def fun(x):
    global y
    y = x * x
    return y


fun(2)
print(y)

def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]

print(v)

tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)



