#implementation of a linked list
#further explanation in the README file


class Node:   #The objects will be the nodes that go into the list
  
    def __init__(self, data): 
        self.data = data  
        self.next = None  
  
class LinkedList:   #this class contains the methods to insert, remove, traverse or sort the list 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    def printList(self): # This function prints contents of linked list 
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next
  
  

if __name__=='__main__': 
  
    llist = LinkedList() 
  
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 
  
    llist.head.next = second; # Link first node with second 
    second.next = third; # Link second node with the third node 
  
    llist.printList() 
