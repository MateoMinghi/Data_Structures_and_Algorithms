#further explanation on queues in README file  
#python doesn't have built-in queues, but the can be implemented with lists or linked lists.
 
#implementation using lists

list_of_queue = [] #declare variable 'queue' which is a list that is then going to be filled in
 

list_of_queue.append('a')
list_of_queue.append('b')
list_of_queue.append('c')
 
print("initial list")
print(list_of_queue) #when we print it, we see elements inside a list
 
# Removing elements from the queue
print()
print(list_of_queue.pop())
print(list_of_queue.pop())
print(list_of_queue.pop()) #after dequeuing elements from the list, they get arranged in FIFO order



print() 
print("Queue after removing elements")
print(list_of_queue)
#if we print the list_of_queue after the elemnts have been dequeued, it must be empty
