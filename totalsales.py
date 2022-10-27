

# # Total Sales

# # Design a program that asks the user to enter a store’s sales for each day of the week. The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.

# salesOfWeek = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}

# for day in salesOfWeek.keys():
#     dailySale = float(input("Enter sale for {}: ".format(day)))
#     print("Entered ${:,.2f}".format(dailySale))
#     salesOfWeek[day] = dailySale
# print("Daily sales this week: ")
# print(salesOfWeek)
# sumWeekSales = sum(list(salesOfWeek.values()))
# print("Total sales this week: ${:,.2f}".format(sumWeekSales))

# listSales = []
# weeklySales = 0
# for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
#     dailySale = float(input("Enter sale for {}: ".format(day)))
#     print("Entered ${:,.2f}".format(dailySale))
#     listSales.append(dailySale)
# for amount in listSales:
#     weeklySales += amount
# print("Total sales this week = ${:,.2f}".format(weeklySales))


# Capital Quiz

# Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values. (Use the Internet to get a list of the states and their capitals.) The program should then randomly quiz the user by displaying the name of a state and asking the user to enter that state’s capital. The program should keep a count of the number of correct and incorrect responses. (As an alternative to the U.S. states, the program can use the names of countries and their capitals.)

import random
from collections import Counter 
import unicodedata

statesCapitals={
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

guesses = Counter({'correct':0, 'incorrect':0})

#unicodedata.normalize("NFKD", text.casefold())

for state in random.sample(statesCapitals.keys(), 1):
    usersGuess = unicodedata.normalize("NFKD", input("What is the capital of {}? ".format(state)).casefold())
    print("You guessed: {}.".format(usersGuess))
    if usersGuess.casefold() == unicodedata.normalize("NFKD", state.casefold()):
        print("That is correct.")
        guesses['correct'] += 1
    else:
        print("That is incorrect.")
        guesses['incorrect'] += 1
        print("The capital of {} is {}.".format(state, statesCapitals[state]))




# >>> from letters import count_letters
# >>> letter_counter = count_letters("pyzen.txt")

# >>> for letter, count in letter_counter.items():
# ...     print(letter, "->", count)
# ...
# t -> 79
# h -> 31
# e -> 92
# z -> 1
#   ...
# k -> 2
# v -> 5
# w -> 4

# >>> for letter, count in letter_counter.most_common(5):
# ...     print(letter, "->", count)
# ...
# e -> 92
# t -> 79
# i -> 53
# a -> 53
# s -> 46

# c = Counter()
# for item in something:
#     if item.has_some_property:
#         c[item.property] += 1
#     elif item.has_some_other_property:
#         c[item.other_property] += 1
#     elif item.has_some.third_property:
#         c[item.third_property] += 1