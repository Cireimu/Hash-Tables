hash_table_size = 8
hash_table = [None] * hash_table_size


def my_hash(s):
    str_bytes = s.encode()

    total = 0
    for b in str_bytes:
        total += b
    return total


def hash_index(s):
    h = my_hash(s)

    return h % hash_table_size


def put(key, value):
    # get index into the hash table list
    index = hash_index(key)
    hash_table[index] = value


def get(key):
    index = hash_index(key)
    return hash_table[index]


def delete(key):
    index = hash_index(key)
    hash_table[index] = None


if __name__ == "__main__":
    # print(hash_index("Hello"))
    # print(hash_index("Ethan"))
    # print(hash_index("cats"))
    # print(hash_index("beej"))

    put("Hello", 37)
    put("foobar", 128)
    put("cats", "dogs")
    print(hash_table)
    delete("Hello")
    print(get("foobar"))
    print(get("ethan"))
