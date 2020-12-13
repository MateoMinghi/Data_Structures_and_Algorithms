#more info on hash tables in README file 
#the equivalent to a hash table in python is the dictionary

dictionary = { 'Food': 'Pizza',
               'Dessert': 'Ice Cream'} 

print(dictionary)



#program to implement a hash function

#create the class
class HashTable(object):
    def __init__(self): #initialize instance
        self.table = [None]*10000

    #this function calculates the hash value by using the built-in method ord() 
    #adding a numeric values to a character. Multiplies that by 100 and adds the ord() value of the second character in the string 
    def calculate_hash_value(self, string): 
        value = ord(string[0])*100 + ord(string[1])
        return value

if __name__ == '__main__':
  hash_table = HashTable()
  print(hash_table.calculate_hash_value('Pizza'))

