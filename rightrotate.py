


# Challenge 1

# Given an array, rotate the array to the right by k steps, where k is non-negative. For example,

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

import numpy as np
import unicodedata

inArray = np.array([1,2,3,4,5,6,7])

keepGoing = True
while keepGoing:
    userInput = unicodedata.normalize("NFKD", input("No of steps to right rotate? (1-{}) ".format(len(inArray))).casefold()) 
    k = int(userInput)

    if userInput in ["", "n"]:
        keepGoing = False
    if not k in range(0,8):
        keepGoing = False

    resultArray = np.concatenate((inArray[-k:], inArray[:-k]),)
    print (resultArray)

#if __name__ == '__main__':
 
