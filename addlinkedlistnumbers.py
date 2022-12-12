
import linkedlist_singly as ll

# Challenge 1

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contains a single digit. Add the two numbers and return them as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself. For example,

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807

def add_two_numbers(l1: ll.LinkedList, l2: ll.LinkedList) -> ll.LinkedList:

    l3 = ll.LinkedList()
    sum_value = 0
    carry_value = 0

    l1_current = l1.head
    l2_current = l2.head

    while l1_current is not None or l2_current is not None:
        # At the start of each iteration, the sum is any carry value from the last iteration
        sum_value = carry_value

        # Add values from both linked list. Advance pointers.
        if l1_current is not None:
            sum_value += l1_current.value
            l1_current = l1_current.next
        if l2_current is not None:
            sum_value += l2_current.value
            l2_current = l2_current.next

        # Summed digit is modulus 10
        node_value = sum_value % 10
        # Carry digit is quotient 10
        carry_value = sum_value // 10

        # Summed digit is added to result list
        l3.add_node(node_value)
    
    # Any carry after having iterated over l1 and l2 is added to result list
    if carry_value > 0:
        l3.add_node(carry_value)

    return l3

if __name__ == '__main__':

    my_l1 = ll.LinkedList([2, 4, 3])
    my_l2 = ll.LinkedList([5, 6, 4])
    my_l3 = add_two_numbers(my_l1, my_l2)
    print(my_l3)
