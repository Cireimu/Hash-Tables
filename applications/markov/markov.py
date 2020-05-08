import random

# Read in all the words in one go
with open("/Users/Ethan/Hash-Tables/applications/markov/input.txt", "r") as f:
    words = f.read()
    split_words = words.split()
    random_dict = {}
    for i, word in enumerate(split_words):
        # ends the for loop once it has gone through
        # all the words in the split words
        # checks to see if new word is already in list
        if i == len(split_words) - 1:
            break
        if random_dict.get(word):
            random_dict[word].append(split_words[i+1])
        else:
            random_dict[word] = [split_words[i+1]]

    # Checks to see if word starts uppercased
    # and makes sure that it doesn't end with .
    def is_start(word):
        if word[0].isupper() and word[len(word) - 1] != '.':
            return True

    start_words = [word for word in random_dict.keys() if is_start(word)]

    # checks to see if word ends with . or ! or ?
    def is_stop(word):
        end = word[-1:]
        if end == '.' or end == '!' or end == '?':
            return True

    # runs five times
    for ran_words in range(5):
        word = random.choice(start_words)

        while not is_stop(word):

            print(word, end=' ')

            word = random.choice(random_dict[word])

        print(word, '\n')
