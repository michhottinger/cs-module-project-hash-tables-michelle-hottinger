class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Initiate our array with empty values.
        self.capacity = capacity
        self.storage = [none] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash_value = 5381
    
        for char in key:
            hash_value = ((hash_value << 5)+hash_value) + char
        return hash_value


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    
    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
#         * Find the index in the hash table for the key
# * Search the list at that index for the key
# * If it exists:
#   * Return the value
# * Else it doesn't exist:
#   * Return `None`
        
        # Your code here
        index = self.hash_index(key)
        head = self.storage[index]
        entry = HashTableEntry(key, value)
        
        self.storage[index] = entry
        entry.next = head
        
        
        # Get the index into "data" to store "v"
# 	    i = get_index(k)

# 	    # Store v there
# 	    data[i] = v
        
  
        
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
#         find index
#         search through index
#         find value with key
#         change pointers to next value
       
        index = self.hash_index(key)
        entry = self.storage[index]
        previous = None
        
        while entry != None:
            if entry.key == key:
                previous.next = entry.next #nothing is pointing to entry now
                return
            previous = entry
            entry = entry.next
        print("Key not found")
                
            
    

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        i = get_index(k)

	    return data[i]
    

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        
        
#notes from class
#super simple linked list: next pointer sets to next node (11) --> (22) --> None head is a
class Node:#HashTableEntry
    def_init_(self, value):
        self.value = value
        self.next = None
        
class LinkedList:#hash_table class
    def __init__(self):
        self.head = None
    
    def find(self, value):#start at head of list and walk along next pointers to find value then return it
        cur = self.head
        
        while cur is not None:
            if cur.value ==value:
                return cur
            
            cur = cur.next#bumps current pointer from one node down to the next node
            
        return None #we didn't find the value
    #the above pattern repeats all over linked list node
    
    def insert_at_head(self, value):
        n =Node(value)
        n.next = self.head
        self.head = n
        
        
        
    def delete(self, value):
        cur = self.head
        #special case of deleting the head
        if cur.value == value:
            self.head = self.head.next
            cur.next = None
            return cur
        
        #general case
        prev = cur
        cur = cur.next
        
        while cur is not None:
            if cur.value = value:
                prev.next = cur.next
                cur.next = None
                return cur
            else:
                prev = prev.next
                cur = cur.next #move prev and cur to next postions
                
        return None
        
a = Node(11)
b = Node(22)

a.next = b

#load factor
#the number of records in teh hash table vs. the number of slots in the array

data = [None] * 16
put("1", 99)
put("2", 99)

#load factor = 2 / 16 #num of items we put into table devided by size of array
#store the count of items in the hash, and keep it below .7 load factor





if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
