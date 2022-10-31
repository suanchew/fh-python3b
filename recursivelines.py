
# Recursive Lines

# Write a recursive function that accepts an integer argument n. The function should display n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line showing 2 asterisks, up to the n-th line which shows n asterisks.

def asteris(n):
    if not n == 1:
        asteris(n-1)
    print("*" * n)
    
if __name__ == "__main__":
    howManyLines = input("How many lines would you like? ")
    asteris(int(howManyLines))

# from time import sleep
#  2
#  3print("This is my file to demonstrate best practices.")
#  4
#  5def process_data(data):
#  6    print("Beginning data processing...")
#  7    modified_data = data + " that has been modified"
#  8    sleep(3)
#  9    print("Data processing finished.")
# 10    return modified_data

# $ python3 best_practices.py
# This is my file to demonstrate best practices.

# >>> import best_practices
# This is my file to demonstrate best practices.

# Use if __name__ == "__main__" to Control the Execution of Your Code
# What if you want process_data() to execute when you run the script from the command line but not when the Python interpreter imports the file?

# You can use the if __name__ == "__main__" idiom to determine the execution context and conditionally run process_data() only when __name__ is equal to "__main__". Add the code below to the bottom of your best_practices.py file:

# if __name__ == "__main__":
# 12    data = "My data read from the Web"
# 13    print(data)
# 14    modified_data = process_data(data)
# 15    print(modified_data)

# In this code, you’ve added a conditional statement that checks the value of __name__. This conditional will evaluate to True when __name__ is equal to the string "__main__". Remember that the special value of "__main__" for the __name__ variable means the Python interpreter is executing your script and not importing it.

