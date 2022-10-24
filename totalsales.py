

# Total Sales

# Design a program that asks the user to enter a store’s sales for each day of the week. The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.

salesOfWeek = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}

for day in salesOfWeek.keys():
    dailySale = float(input("Enter sale for {}: ".format(day)))
    print("Entered ${:,.2f}".format(dailySale))
    salesOfWeek[day] = dailySale
print("Daily sales this week: ")
print(salesOfWeek)
sumWeekSales = sum(list(salesOfWeek.values()))
print("Total sales this week: ${:,.2f}".format(sumWeekSales))

listSales = []
weeklySales = 0
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    dailySale = float(input("Enter sale for {}: ".format(day)))
    print("Entered ${:,.2f}".format(dailySale))
    listSales.append(dailySale)
for amount in listSales:
    weeklySales += amount
print("Total sales this week = ${:,.2f}".format(weeklySales))



