

# Total Sales

# Design a program that asks the user to enter a store’s sales for each day of the week. The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.

#dayOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
salesOfWeek = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}

for day in salesOfWeek.keys():
    dailySale = float(input("Enter sale for {}: ".format(day)))
    salesOfWeek[day] = dailySale
    print("Entered ${:,.2f}".format(dailySale))

print("Sales of this week: ")
print(salesOfWeek)

