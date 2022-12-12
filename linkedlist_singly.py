
class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return f"{self.value}"

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if not values is None:
            self.add_multiple_nodes(values)
            
    def __str__(self):
        return ' -> '.join([f"{node}" for node in self])
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
            
    @property
    def values(self) -> []:
        return [node.value for node in self]
    
    def add_node(self, value) -> Node:
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def add_multiple_nodes(self, values) -> Node:
        for value in values:
            self.add_node(value)
        return self.tail
            
    # def add_node_as_head(self, value):
    #     if self.head is None:
    #         self.tail = self.head = Node(value)
    #     else:
    #         self.head = Node(value, self.head)
    #     return self.head

    def delete_node(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                # move prev & current pointers
                prev = current
                current = current.next
            # nothing to delete
            if current == None:                
                return
            # hop prev.next across the node to be deleted onto current.next pointer
            prev.next = current.next
            # delete node
            current = None 

    def insert_node(self, node, pos):
            count = 0
            current = self.head
            if pos == 0:
                node.next = self.head
                self.head = node
            while current:
                if count+1 == pos:
                    node.next = current.next
                    current.next = node
                    return
                else:
                    count += 1
                    current = current.next


if __name__ == '__main__':

    # Example of singly Linked List with insert and print methods
    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    print (f"Adding nodes 1 to 3: {ll}")
    ll.add_multiple_nodes([5, 5, 6, 7])
    print (f"Adding list of nodes [5, 5, 6, 7]: {ll}")
    ll.delete_node(5)
    print (f"Delete node 5: {ll}")
    ll.insert_node(Node(4), 3)
    print (f"Insert node 4: {ll}")
    ll.insert_node(Node(8), 7)
    print (f"Insert node 8: {ll}")
    ll.insert_node(Node(0), 0)
    print (f"Insert node 0: {ll}")

    print (f"Here is my linked list: {ll}")

