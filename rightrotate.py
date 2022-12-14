# pyenv versions
# pip install numpy

# Challenge 1

# Given an array, rotate the array to the right by k steps, where k is non-negative. For example,

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

print ("-----Challenge 1-----")
import numpy as np
import unicodedata

inArray = np.array([1,2,3,4,5,6,7])
print ("Array to rotate: {}".format(inArray))
if len(inArray) > 0:
    keepGoing = True
    while keepGoing:
        userInput = unicodedata.normalize("NFKD", input("No of steps to right rotate? 1-{} or e(xit): ".format(len(inArray))).casefold())

        if userInput in ["", "e"]:
            break

        k = int(userInput) % len(inArray)
        if not k in range(0,len(inArray)+1):
            break

        resultArray = np.concatenate((inArray[-k:], inArray[:-k]),)
        print ("Rotated array: {}".format(resultArray))
        resultArray = []



# Challenge 2

# Given an integer array arr that is guaranteed to have a peak value, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]. For examples,

# arr = [0,1,0] returns 1
# arr = [3,4,5,1] returns 2
# arr = [24,69,100,99,79,78,67,36,26,19] returns 2

# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# http://courses.csail.mit.edu/6.006/spring11/lectures/lec02.pdf

print ("-----Challenge 2-----")
# Recursive function to find the peak element in a list
def findPeakIndex(items, left=None, right=None):
 
    if left is None and right is None:
        left, right = 0, len(items) - 1
 
    # find the middle element. To avoid overflow, use mid = left + (right-left)//2
    mid = left + (right-left)//2

    # peak index is found if the middle element is greater than its neighbors
    if ((mid == 0 or items[mid-1] <= items[mid]) and
            (mid == len(items)-1 or items[mid+1] <= items[mid])):
        return mid
 
    # If the left neighbor of `mid` is greater than the middle element,
    # find the peak recursively in the left sublist
    if mid - 1 >= 0 and items[mid-1] > items[mid]:
        return findPeakIndex(items, left, mid-1)
 
    # If the right neighbor of `mid` is greater than the middle element,
    # find the peak recursively in the right sublist
    return findPeakIndex(items, mid+1, right)
 
items = [1,2, 3, 80, 90, 100, 20, 50, 60]
print ("Mountain array: {}".format(items))
if len(items) > 0:
    index = findPeakIndex(items)
print("The peak index: ", index)










# exit(0) exit(1):
# Any non-zero value is considered ???abnormal termination??? by shells. Most systems require it to be in the range 0???127. 
# https://docs.python.org/3/library/sys.html#sys.exit





# PYTHON SLICING:
# https://stackoverflow.com/questions/509211/understanding-slicing

# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array

# There is also the step value, which can be used with any of the above:

# a[start:stop:step] # start through not past stop, by step

# The key point to remember is that the :stop value represents the first value that is not in the selected slice. So, the difference between stop and start is the number of elements selected (if step is 1, the default).

# The other feature is that start or stop may be a negative number, which means it counts from the end of the array instead of the beginning. So:

# a[-1]    # last item in the array
# a[-2:]   # last two items in the array
# a[:-2]   # everything except the last two items

# Similarly, step may be a negative number:

# a[::-1]    # all items in the array, reversed
# a[1::-1]   # the first two items, reversed
# a[:-3:-1]  # the last two items, reversed
# a[-3::-1]  # everything except the last two items, reversed

# Explanation:
# a[:2:-1] does not specify a START, but specifies that you want to index in reverse and STOP at index 2 (not inclusive), so it will return all but the first three elements, in reverse order (i.e. a[-1], a[-2],...,a[3]). a[1::-1] specifies the START at index 1 (inclusive), does not specify a STOP, and specifies that you want to index in reverse, so it will return the first two entries in the list, in reverse order (i.e. a[1], a[0])

# Python is kind to the programmer if there are fewer items than you ask for. For example, if you ask for a[:-2] and a only contains one element, you get an empty list instead of an error. Sometimes you would prefer the error, so you have to be aware that this may happen.



# Relationship with the slice object:

# A slice object can represent a slicing operation, i.e.:

# a[start:stop:step]

# is equivalent to:

# a[slice(start, stop, step)]

# Slice objects also behave slightly differently depending on the number of arguments, similarly to range(), i.e. both slice(stop) and slice(start, stop[, step]) are supported. To skip specifying a given argument, one might use None, so that e.g. a[start:] is equivalent to a[slice(start, None)] or a[::-1] is equivalent to a[slice(None, None, -1)].

# While the :-based notation is very helpful for simple slicing, the explicit use of slice() objects simplifies the programmatic generation of slicing.




