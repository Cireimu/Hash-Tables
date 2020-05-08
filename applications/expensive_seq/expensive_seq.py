# initialize the dict
seq_dict = dict()


def expensive_seq(x, y, z):
    seq_item = f'{x},{y},{z}'

    # if this sequence item exists in seq_dict
    # then just return that seq_dictd item
    if seq_dict.get(seq_item):
        return seq_dict[seq_item]
    # check to see if the value of x is less than or equal to
    # if so then just return y + z
    if x <= 0:
        return y + z

    # just setting up the calls for human readability
    an1 = expensive_seq(x-1, y+1, z)
    an2 = expensive_seq(x-2, y+2, z*2)
    an3 = expensive_seq(x-3, y+3, z*3)
    an4 = an1 + an2 + an3

    # stores the value of the final answer in the seq_dict
    # returns the answer
    seq_dict[seq_item] = an4
    return an4


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
