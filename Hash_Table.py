class HashTable:
    def __init__(self):
        # Initialize empty dictionary
        self.collection = {}

    def hash(self, key):
        # Sum of Unicode values of all characters
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hashed_key = self.hash(key)

        # If hash already exists, add to nested dictionary
        if hashed_key in self.collection:
            self.collection[hashed_key][key] = value
        else:
            # Create a new nested dictionary
            self.collection[hashed_key] = {key: value}

    def remove(self, key):
        hashed_key = self.hash(key)

        # Check if hash exists and key exists inside it
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]

                # Optional: remove empty dictionary
                if not self.collection[hashed_key]:
                    del self.collection[hashed_key]

    def lookup(self, key):
        hashed_key = self.hash(key)

        # Return value if exists, else None
        if hashed_key in self.collection:
            return self.collection[hashed_key].get(key, None)
        return None
    
hash_table = HashTable()

hash_table.add("apple", 10)
hash_table.add("banana", 20)
hash_table.add("orange", 30)

print("Apple:", hash_table.lookup("apple"))
print("Banana:", hash_table.lookup("banana"))
print("Orange:", hash_table.lookup("orange"))

hash_table.remove("banana")

print("\nAfter removing banana:")
print("Banana:", hash_table.lookup("banana"))

print("\nInternal Structure:")
print(hash_table.collection)