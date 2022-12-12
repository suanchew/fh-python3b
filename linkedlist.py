# Node class of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insert method for Linked List
  def insertLL(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

# Example of singly Linked List with insert and print methods
ll = LinkedList()
ll.insertLL(1)
ll.insertLL(2)
ll.insertLL(3)
ll.printLL()