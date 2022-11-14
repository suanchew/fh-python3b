
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


