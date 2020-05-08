def no_dups(s):
    # Implement me.
    cache = {}

    if len(s) < 1:
        return ''

    for w in s.split():
        if cache.get(w):
            pass

        else:
            cache[w] = None
    return ' '.join(cache.keys())


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
