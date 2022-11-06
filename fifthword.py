# Challenge 1

# The code below assigns the 5th letter of each word in food to the new list fifth. However, the code currently produces errors. Insert a try/except clause that will allow the code to run and produce of list of the 5th letter in each word. If the word is not long enough, it should not print anything out. Note: The pass statement is a null operation; nothing will happen when it executes.

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []
for x in food:
    try:
        if len(x) < 5:
            raise Exception("{} is too short".format(x))
        fifth.append(x[4])
    except Exception as e:
        pass
print("The fifth list is {}".format(fifth))

# Challenge 2

# Add exception handling to the get_value() function so that it, if an IndexError exception occurs because the specified index does not exist, the function returns the keyword None. Do not handle any other types of exceptions.

def get_value(data_list, index):
    try:
        return data_list[index]
    except IndexError as e:
        return None

# Sample list data
data_list = ['a', 'b', 'c']
index = 3
print(get_value(data_list, index))


