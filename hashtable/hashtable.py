class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, storage):
        self.storage = [None] * storage
        self.capacity = len(self.storage)
        self.load = 0

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = hash*33 + ord(x)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        self.load += 1

        load_fact = self.load / self.capacity
        # check to see if the indice we are trying to insert our node into is empty
        # if not then just insert our key value pair as a new node
        if node is None:
            self.storage[index] = HashTableEntry(key, value)
            if load_fact > .70:
                self.resize(self.capacity * 2)
            return

        # if the there is already a node (key value pair)
        # run some more checks
        elif node is not None:
            # if the key of the node we're trying to insert doesn't match any of the keys
            # of the nodes in that indice
            if node.key != key:

                # loops until there are no more nodes to loop through to check
                while node.next is not None:
                    # if the key doesn't match the key of the current node we're looking at
                    # then move on to the next node
                    if node.key != key:
                        node = node.next
                    else:
                        # if it does match then we will just insert the value,
                        # which replaces the old one for that key
                        node.value = value
                if node.key == key:
                    node.value = value
                else:
                    node.next = HashTableEntry(key, value)
                    if load_fact > .70:
                        self.resize(self.capacity * 2)
                    return
            else:
                node.value = value

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """

        index = self.hash_index(key)
        node = self.storage[index]
        self.load -= 1
        load_fact = self.load / self.capacity
        if node.key == key:
            self.storage[index] = node.next
            node.next = None
            if load_fact < .2:
                self.resize(self.capacity // 2)
            return
        while node.next is not None:
            if node.next.key == key:
                del_node = node.next
                node.next = del_node.next
                del_node.next = None
                if load_fact < .25:
                    self.resize(self.capacity // 2)
            else:
                node = node.next
        return print("Could not find the requested key")

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        if node is not None:
            # loop until there are no more nodes
            while node.next is not None:
                # if the node with the key is found
                # return the value within that node
                # if not then move on to the next node
                if node.key == key:
                    return node.value
                else:
                    node = node.next
            # if the key and the node key match
            # return the node value
            if node.key == key:
                return node.value
            else:
                return None
        else:
            return None

    def resize(self, new_cap=None):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """
        if not new_cap:
            return
        double_hash = HashTable(new_cap)
        for i in self.storage:
            node = i
            while node:
                double_hash.put(node.key, node.value)
                node = node.next
        self.capacity = new_cap
        self.load = double_hash.load
        self.storage = double_hash.storage
        del double_hash


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("----")
    # ht.delete("line_3")
    print("delete")
    print("----")

    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
