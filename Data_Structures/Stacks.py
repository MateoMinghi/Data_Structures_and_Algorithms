#more information on stacks in README file
#python doesn't have built-in stacks, but they can be implemented using lists or linked lists


#implementation using lists
#basically we declare a variable 'stack' which has a list to be completed with 'append' methods
list_of_stack = []
 
list_of_stack.append('a')
list_of_stack.append('b')
list_of_stack.append('c')
 
#this prints the stack in the form of a list after adding elements to it
print('Stack')
print(list_of_stack)
 
#then the method 'pop' is used to take the elements in LIFO  order
print()
print(list_of_stack.pop())
print(list_of_stack.pop())
print(list_of_stack.pop())
 
#after 'pop' methods, the stack must be empty. This is useful for algorithms like BFS
print()
print('Stack after elements are poped')
print(list_of_stack)




