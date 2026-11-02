class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

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

    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        # Sum the character codes, then wrap the total to a valid index.
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.data[index]

        # Empty slot: the new node becomes the head of the list.
        if current is None:
            self.data[index] = Node(key, Contact(key, value))
            return

        # Walk the list, updating in place if the name already exists.
        while True:
            if current.key == key:
                current.value.number = value
                return
            if current.next is None:
                break
            current = current.next

        # Collision with no matching name: append to the end of the list.
        current.next = Node(key, Contact(key, value))

    def search(self, key):
        current = self.data[self.hash_function(key)]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for index in range(self.size):
            current = self.data[index]

            if current is None:
                print(f"Index {index}: Empty")
                continue

            entries = ""
            while current is not None:
                entries += f"- {current.value} "
                current = current.next
            print(f"Index {index}: {entries}")

# Test your hash table implementation here.
if __name__ == "__main__":
    # Contact and Node
    contact_1 = Contact("Riley", "123-456-7890")
    print(contact_1)  # Riley: 123-456-7890

    node_1 = Node(contact_1.name, contact_1)
    print(node_1.key)  # Riley
    print(node_1.value)  # Riley: 123-456-7890
    print(node_1.next)  # None

    # Empty table
    table = HashTable(10)
    print()
    table.print_table()

    # Add some values
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    print()
    table.print_table()

    # Search for a value
    contact = table.search("John")
    print("\nSearch result:", contact)  # Search result: John: 909-876-1234

    # Edge Case #1 - Hash collisions ("Amy" and "May" are anagrams, so their ord() sums match)
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    print()
    table.print_table()

    # Edge Case #2 - Duplicate keys
    table.insert("Rebecca", "999-444-9999")  # Should update Rebecca's number
    print()
    table.print_table()

    # Edge Case #3 - Searching for a value not in the table
    print()
    print(table.search("Chris"))  # None
