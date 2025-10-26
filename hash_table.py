class Contact:  #Person's name and phone number 
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self,name:str,number:str):
        self.name=name
        self.number=number
    def __str__(self)->str:
        return f"{self.name}:{self.number}"
        

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self,size:int):
        self.size=size
        self.data=[None]*size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)#getting index of key
        current =  self.data[index] #linked list value(s)

        if self.data[index] is None: #If value is none
         self.data[index] = Node(key, value) #assign value(node) to the index
         return
        
        while current: # Iterate until you reach a value of None
            if current.key == key: # Check if it is a duplicate
                current.value = value
                return
            
            if current.next is None: 
                break  # Stop at last node

            current=current.next
        current.next=Node(key,value)

    def search(self, key):
        index = self.hash_function(key) #getting index of key
        current = self.data[index] #linked list value(s)

        while current:
            if current.key == key: #if the key in storage equals key
                return current.value #return the value
            current = current.next #point to the next
    
        return None #returns None when Key is not available
    
    def print_table(self):
        for i in range(self.size):
            current=self.data[i]
            if current is None:
                print(f'Index {i}: Empty')
               
            else:
                print(f'Index {i}:', end='') 
                while current:
                    print(f"-{current.key}:{current.value}",end='')#stay on same line,(end='')
                    current=current.next #move forward
                print()


    
                                 # Testing Implementations.  

contact_1 = Contact("Riley", "123-456-7890")
print(contact_1) # Riley: 123-456-7890 

table = HashTable(10) #an instance for the HashTable Class

table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")

table.print_table()

##Searching for a contact with name
contact = table.search("Rebecca") 
print("\nSearch result:", contact) 


                                         #Edge Cases
#Edge Case1- Testing collition, with same index
table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")  # May collide with Amy depending on hash function 
table.print_table()

#Edge Case2- Testing dupicates
table.insert("Rebecca", "999-444-9999")  # Should update Rebecca's number 
table.print_table()

#Edge Case3- Searching for a value not in the table
print(table.search("Eugene"))



#The goal of this project waas to design a simple harsh table that stores and retrieves contact information when called upon.
#To implement the harsh table, I created 3 main classes: Contact, Node and the HashTable.

#The Contact class represents a person's name and phone number. The name and phone are provided as a string to the contructor(__init__)
#  and the __str()__ method returns the contact’s information in the format “[CONTACT_NAME]: [CONTACT_NUMBER]” .

#The Node class acts a single building block of the harsh table and each holds a key(name), a  value(phone number) and a pointer to the next node.
#The HashTable class has four methods: 
# -hash_function(key) method which converts a string key into an array index,
# -insert(key) method which inserts a new contact into the hash table,
# -search(key) method which searches for a contact by name,
# -print_table() method which prints the structure of the hash table .

# A hash table was used for this project because it allows fast lookups,i.e., it provides a faster way of checking the contents of a list compared
# to the traditional loop method. And it handles it duplicates(inputs with the same hash) by adding the new insertion to the same index as the 
# exisiting key and value. An engineer might choose hash table over tree or list if he or she wants search through something quickly.