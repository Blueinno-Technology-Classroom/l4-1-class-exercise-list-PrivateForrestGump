##################################################
'''
Q1: 
'''

# TODO: Write your code here
empty_list = [ ]
ea = ['It', 'was', 'a', 'stormy', 'night']
##################################################
'''
Q2:
'''

# TODO: Write your code here
ea = ['It', 'was', 'a', 'stormy', 'night']

ea.insert(3, 'dark')
ea.insert(4, 'and')

print(ea)
##################################################
'''
Q3:
'''

# TODO: Write your code here

ea[1] = 'IS'

print(ea)
##################################################
'''
Q4:
'''

# TODO: Write your code here
del ea[2]
del ea[2]
del ea[2]

removal = []

for word in ea:
    if ('a' in word):
        removal.append(word)

print(ea)
##################################################
'''
Q5:
'''

# TODO: Write your code here
e = []

for i in range(0,19,2):
    print(i)
    e.append(i)

print(e)
##################################################
'''
Q6:
'''

# TODO: Write your code here
def fill(list, x):
    print(len(list)) #amount of things in list

    for i in range(len(list)):
        list[i] = x

    return list

    
my_list = [42, -7, 3, 0, 15]
my_list = fill(my_list, 2)

print(my_list)
# --> [2, 2, 2, 2, 2]
##################################################
