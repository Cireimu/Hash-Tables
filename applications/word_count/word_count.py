# I know there's a flaw in this answer
# but this is my first pass so yeah...


def word_count(s):
    # add an extra space at the end of the string
    # this is so that it will do the final call via isspace() to add to cache
    s += ' '

    # initialize the cache
    cache = {}

    # initialize an empty string
    new_word = ''

    # goes through every character/space and checks if it's an alphenumeric
    # if so then add that into the "new_word" lowercased
    # if it's a space then check if "new_word" exists in the cache
    # if so then just add another "tick" to the value
    # if not then create a new key value pair
    # reset new_word
    # repeat
    for c in s:
        if c.isalnum() or c == "'":
            new_word += c.lower()
        if c.isspace():
            if cache.get(new_word):
                cache[new_word] += 1
            elif new_word != '':
                cache[new_word] = 1
            new_word = ''

    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat.  And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
