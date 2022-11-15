
# Challenge 1 - Total Sales

# Design a program that asks the user to enter a store’s sales for each day of the week. The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.

# Store sales in dictionary
# salesOfWeek = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}
# for day in salesOfWeek.keys():
#     dailySale = float(input("Enter sale for {}: ".format(day)))
#     print("Entered ${:,.2f}".format(dailySale))
#     salesOfWeek[day] = dailySale
# print("Daily sales this week: ")
# print(salesOfWeek)
# sumWeekSales = sum(list(salesOfWeek.values()))
# print("Total sales this week: ${:,.2f}".format(sumWeekSales))

# Store sales in list
listSales = []
weeklySales = 0
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    dailySale = float(input("Enter sale for {}: ".format(day)))
    print("Entered ${:,.2f}".format(dailySale))
    listSales.append(dailySale)
for amount in listSales:
    weeklySales += amount
print("Total sales this week = ${:,.2f}".format(weeklySales))



# Challenge 2 - Capital Quiz

# Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values. (Use the Internet to get a list of the states and their capitals.) The program should then randomly quiz the user by displaying the name of a state and asking the user to enter that state’s capital. The program should keep a count of the number of correct and incorrect responses. (As an alternative to the U.S. states, the program can use the names of countries and their capitals.)

import random
from collections import Counter 
import unicodedata

statesCapitals={
    'alabama':'montgomery',
    'alaska':'juneau',
    'arizona':'phoenix',
    'arkansas':'little rock',
    'california':'sacramento',
    'colorado':'denver',
    'connecticut':'hartford',
    'delaware':'dover',
    'florida':'tallahassee',
    'georgia':'atlanta',
    'hawaii':'honolulu',
    'idaho':'boise',
    'illinois':'springfield',
    'indiana':'indianapolis',
    'iowa':'des moines',
    'kansas':'topeka',
    'kentucky':'frankfort',
    'louisiana':'baton rouge',
    'maine':'augusta',
    'maryland':'annapolis',
    'massachusetts':'boston',
    'michigan':'lansing',
    'minnesota':'st. paul',
    'mississippi':'jackson',
    'missouri':'jefferson city',
    'montana':'helena',
    'nebraska':'lincoln',
    'nevada':'carson city',
    'new hampshire':'concord',
    'new jersey':'trenton',
    'new mexico':'santa fe',
    'new york':'albany',
    'north carolina':'raleigh',
    'north dakota':'bismarck',
    'ohio':'columbus',
    'oklahoma':'oklahoma city',
    'oregon':'salem',
    'pennsylvania':'harrisburg',
    'rhode island':'providence',
    'south carolina':'columbia',
    'south dakota':'pierre',
    'tennessee':'nashville',
    'texas':'austin',
    'utah':'salt lake city',
    'vermont':'montpelier',
    'virginia':'richmond',
    'washington':'olympia',
    'west virginia':'charleston',
    'wisconsin':'madison',
    'wyoming':'cheyenne'
}

guesses = Counter({'correct':0, 'incorrect':0})
keepGuessing = True
while keepGuessing:
    for k in random.sample(statesCapitals.keys(), 1):
        state = unicodedata.normalize("NFKD", k.casefold())

        capital = unicodedata.normalize("NFKD", statesCapitals[k].casefold())
        usersGuess = unicodedata.normalize("NFKD", input("What is the capital of {}? ".format(state)).casefold())
        print("You guessed: {}.".format(usersGuess))
        if usersGuess == capital:
            print("That is correct.")
            guesses['correct'] += 1
        else:
            print("That is incorrect.")
            guesses['incorrect'] += 1
            print("The capital of {} is {}.".format(state, capital))

    if unicodedata.normalize("NFKD", input("Keep guessing (y/n)? ").casefold()) == 'n':
        keepGuessing = False

print("You made {} correct, and {} incorrect guesses".format(guesses['correct'], guesses['incorrect']))





# REGULAR EXPRESSIONS:

# ([\w ]+)
# Replace with
# '$&'

# \n
# Replace with
# ,\n

# $1 = what was matched by the first group. $& = what was matched by the entire regex.
# $& is a backreference to the whole match, while $1 is a backreference to the submatch captured with capturing group 1.

# $&          Inserts the matched substring.
# $n or $nn   Where n or nn are decimal digits, inserts the nth parenthesized submatch string, provided the first argument was a RegExp object.
# https://www.regular-expressions.info/replacebackref.html

# alabama:montgomery
# alaska:juneau
# arizona:phoenix
# arkansas:little rock
# california:sacramento
# colorado:denver
# connecticut:hartford
# delaware:dover
# florida:tallahassee
# georgia:atlanta
# hawaii:honolulu
# idaho:boise
# illinois:springfield
# indiana:indianapolis
# iowa:des moines
# kansas:topeka
# kentucky:frankfort
# louisiana:baton rouge
# maine:augusta
# maryland:annapolis
# massachusetts:boston
# michigan:lansing
# minnesota:st. paul
# mississippi:jackson
# missouri:jefferson city
# montana:helena
# nebraska:lincoln
# nevada:carson city
# new hampshire:concord
# new jersey:trenton
# new mexico:santa fe
# new york:albany
# north carolina:raleigh
# north dakota:bismarck
# ohio:columbus
# oklahoma:oklahoma city
# oregon:salem
# pennsylvania:harrisburg
# rhode island:providence
# south carolina:columbia
# south dakota:pierre
# tennessee:nashville
# texas:austin
# utah:salt lake city
# vermont:montpelier
# virginia:richmond
# washington:olympia
# west virginia:charleston
# wisconsin:madison
# wyoming:cheyenne
