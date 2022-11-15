
# Challenge 1
#https://juheck.gitbooks.io/course-hadoop-and-big-data/content/exercise-lambda-functions.html
# Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this:

#     Order Number    Book Title and Author              Quantity     Price per Item
#     34587           Learning Python, Mark Lutz             4          40.95
#     98762           Programming Python, Mark Lutz          5          56.80
#     77226           Head First Python, Paul Barry          3          32.95
#     88112           Einführung in Python3, Bernd Klein     3          24.99

#     In the Python shell, write a Python program that computes the sum of all products of the price per items and the quantity (price per item x quantity). To enter the Python shell, open the terminal and type python. Use map and reduce function to do so.
#     You can write the list with sublists like the following in the Python shell:

#     orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95],
#     ["98762", "Programming Python, Mark Lutz", 5, 56.80],
#     ["77226", "Head First Python, Paul Barry", 3, 32.95],
#     ["88112", "Einfuhrung in Python3, Bernd Klein", 3, 24.99]]

#     Write a Python program, which returns a list with 2-tuples. Each tuple consists of the order number and the product of the price per items and the quantity. The product should be increased by $10 if the value of the order is less than $100.00. Write a Python program using lambda and map.

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95],
    ["98762", "Programming Python, Mark Lutz", 5, 56.80],
    ["77226", "Head First Python, Paul Barry", 3, 32.95],
    ["88112", "Einfuhrung in Python3, Bernd Klein", 3, 24.99]]

print ("Total sales: ", sum(list(map(lambda row: row[2]*row[3], orders))))

print("Orders: ", [(order[2], order[3]) for order in orders])

print ("Orders, plus $10 if sold<$100: ", list(map(lambda row: (row[0], row[2]*(row[3]+10)) if row[2]*row[3] < 100 else (row[0], row[2]*row[3]), orders )))


#letters = list(map(lambda x: x, 'human'))
#print(letters)

#h_letters = [ letter for letter in 'human' ]
#print( h_letters)

#number_list = [ x for x in range(20) if x % 2 == 0]
#print(number_list)



# Challenge 2

# Given the spells and occurrence arrays as follow

# spells = ["protego", "accio", "expecto patronum", "legilimens"]
# occurrence = [1, 0, 2, 1]

# Write a Python program to concatenate "!!!" to each spell, and repeat that spell X times, where X is an element inside of the array occurrence, sharing the same index with the spell in the array spells. The final output is an array of spells, ending with "!!!" and occurring X-time

# spells = ["protego!!!", "", "expecto patronum!!! expecto patronum!!!", "legilimens!!!"]

# Your Python program must use lambda and map.

from itertools import starmap

spells = ["protego", "accio", "expecto patronum", "legilimens"]
occurrence = [1, 0, 2, 1]

def modifySpell(spell):
    return spell + "!!!"

print( list(starmap(lambda n, m: modifySpell(n) * m, zip(spells, occurrence)) ) )



# MAP FUNCTION:

# The map function has two arguments - a function and an iterable.
# Applies the function to each element of the iterable and returns a map object.
# The function can be a normal, built-in or anonymous function.
# List, sets, tuples, and other iterables can be used as the second argument of the map function.
# The returned map object can be easily converted into another iterable using built-in functions.

# Map functions as methods or built-in functions.
#     cities = ['madrid', 'munich', 'valencia']
#     cities_cap = list(map(lambda x:x.title(),cities))
#     #cities_cap = ['Madrid', 'Munich', 'Valencia']
#     elements = [1,2,3,4]
#     elements_str = list(map(str,elements))
#     #elements_str = ['1','2','3','4']

# Iterable as a dictionary:
#     elements = {'hidrogen':1, 'helium':2, 'carbon':6}
#     elements_upper = list(map(lambda x:x.title(),elements))
#     #elements_upper = ['Hidrogen','Helium','Carbon']

# Iterable as a list of tuples:
#     students = [('Amanda','161cm','51kg'), ('Patricia','165cm','61kg'), ('Marcos','191cm', '101kg')]
#     students_height = list(map(lambda x:x[1], students))
#     #list of strings
#     #students_height = ['161cm','165cm','191cm']
#     students_weight = list(map(lambda x:int(x[2][:-2]), students))
#     #list of numbers
#     #students_weight = [51, 61, 101]

# The map function returns a map object which is an iterator. The iterator can be easily transformed into a list, set, or tuple:
#     elements = [1,2,3,4]
#     elements_by2 = map(lambda x:x*2,elements)
#     print(type(elements_by2))
#     #<class 'map'>

#     elements_list = list(map(lambda x:x*2,elements))
#     print(type(elements_list))
#     #<class 'list'>
#     elements_set = set(map(lambda x:x*2,elements))
#     print(type(elements_set))
#     #<class 'set'>
#     elements_tuple = tuple(map(lambda x:x*2,elements))
#     print(type(elements_tuple))
#     #<class 'tuple'>
#https://levelup.gitconnected.com/using-the-map-function-in-python-f088fad8788d



# LIST COMPREHENSION:

# [expression for item in list]
# [letter for letter in 'human']

# For loop:
# h_letters = []
# for letter in 'human':
#     h_letters.append(letter)
# print(h_letters)
# #['h', 'u', 'm', 'a', 'n']

# List comprehension:
# h_letters = [ letter for letter in 'human' ]
# print( h_letters)
# #['h', 'u', 'm', 'a', 'n']

# Lambda:
# letters = list(map(lambda x: x, 'human'))
# print(letters)
# #['h','u','m','a','n']

# Conditionals:
# number_list = [x for x in range(20) if x % 2 == 0]
# print(number_list)
# #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested if:
# num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
# print(num_list)
# #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# If else:
# obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
# print(obj)
# #['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']

# Nested loops:
# transposed = []
# matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
# for i in range(len(matrix[0])):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)
# #[[1, 4], [2, 5], [3, 6], [4, 8]]

# matrix = [[1, 2], [3,4], [5,6], [7,8]]
# transpose = [[row[i] for row in matrix] for i in range(2)]
# print (transpose)
# #[[1, 3, 5, 7], [2, 4, 6, 8]]
#https://www.programiz.com/python-programming/list-comprehension



# LIST COMPREHENSION - GENERATOR VS ITERATOR:

# List comprehensions must be enclosed by square brackets [...]:
#     h = [x for x in results if x.get("ID")=="91149"]
# Using parenthesis (...) will create a generator expression:
#     h = (x for x in results if x.get("ID")=="91149")
# It is inefficient to read a whole list into memory when all you want is the first item that meets a condition. It is usually faster to use next and a generator expression:
#     h = next(x for x in results if x.get("ID")=="91149")
# Unlike list comprehension (which does it all at once), this solution will yield the items one at a time. It will stop once it finds an item that meets the condition. However, it will also raise a StopIteration error if it cannot find the item. To avoid this, give next a default value to return:
#     h = next((x for x in results if x.get("ID")=="91149"), None)
#https://stackoverflow.com/questions/21790459/bad-syntax-in-python-list-comprehension



# ENUMERATION:

# l = [1, 2, 3]
# for index, item in enumerate(l): 
#     print (index, ":", item)
# #0 : 1
# #1 : 2
# #2 : 3

# d = {'first':1, 'second':2, 'third':3}
# for index, (k, v) in enumerate(d.items()):
#     print (index, ":", k, v) 
# #0 : first 1
# #1 : second 2
# #2 : third 3



# NUMPY nditer():

# numpy.nditer(op, flags=None, op_flags=None, op_dtypes=None, order='K', casting='safe', op_axes=None, itershape=None, buffersize=0):
# numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
# numpy.ndarray(shape, dtype=float, buffer=None, offset=0, strides=None, order=None)

# for counter_variable in np.nditer(array):
#     print(counter_variable) 

# import numpy as np
# arr = np.arange(3)
# print (type(arr))
# print (arr.shape)
# for x in np.nditer(arr):
#     print(x) 
# #<class 'numpy.ndarray'>
# #(3,)
# #0
# #1
# #2

# 3-D array:
# import numpy as np
# arr = np.array([[[1, 2], [3, 4]], [[5, 6]]])
# for x in np.nditer(arr):
#     print(x)
# #1
# #2
# #3
# #4
# #5
# #6

# Iterate as string:
# import numpy as np
# arr = np.array([1, 2, 3])
# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#     print(x)
# #b'1'
# #b'2'
# #b'3'

# Iterate with different step size:
# import numpy as np
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for x in np.nditer(arr[:, ::2]):
#   print(x)
# #1
# #3
# #5
# #7
# https://numpy.org/doc/stable/reference/generated/numpy.nditer.html
# https://numpy.org/doc/stable/reference/generated/numpy.arange.html
# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html
# https://numpy.org/doc/stable/reference/arrays.nditer.html#arrays-nditer



# NUMPY ndenumberate():

# numpy.ndenumerate(arr)

# import numpy as np
# arr = np.array([1, 2, 3])
# for idx, x in np.ndenumerate(arr):
#     print(idx, x)
# #(0,) 1
# #(1,) 2
# #(2,) 3

# import numpy as np
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for idx, x in np.ndenumerate(arr):
#     print(idx, x)
# #(0, 0) 1
# #(0, 1) 2
# #(0, 2) 3
# #(0, 3) 4
# #(1, 0) 5
# #(1, 1) 6
# #(1, 2) 7
# #(1, 3) 8
# https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html


