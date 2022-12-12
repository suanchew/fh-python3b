# Node class of a singly linked list
class Node:

    # constructor
    def __init__(self, data = None, next = None): 

        self.data = data
        self.next = next

    # print method for linked list
    # def printNode(self):
    #     if (self.data):
    #         print(self.data)

    def __str__(self):

        if (self.data):
            return f"{self.data}"
        else:
            return None
    # def __str__(self):
    #     return f"{self.first_name} {self.last_name} is {self.age}."


# Linked List class with a single head node
class LinkedList:

    def __init__(self):  

        self.head = None
    
    # insert method for Linked List
    def addNodeLL(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for linked list
    def printLL(self):
        current = self.head
        while (current):
            # current.printNode()
            print(current)
            current = current.next

# Example of singly Linked List with insert and print methods
ll = LinkedList()
ll.addNodeLL(1)
ll.addNodeLL(2)
ll.addNodeLL(3)
ll.printLL()
