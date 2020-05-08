import math
import random
import time

cache = {}


def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster

    # checks the cache for this item
    # if it's found then we just return that cache item
    # if not then we go through the rest of the function and cache the answer
    cache_item = f"{x},{y}"
    if cache.get(cache_item):
        return cache[cache_item]

    v = math.pow(x, y)

    v //= (x + y)

    v %= 982451653

    cache[cache_item] = v
    return v


start = time.time()

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')


end = time.time()
print(end - start)
