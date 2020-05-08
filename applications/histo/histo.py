def histo(str):

    ignored = r"[\'\!\?\"\&\.\:\;\,\-\+\=\/\\\[\]\{\}\(\)\*\^\&\|\]"

    histo_dict = {}

    lower_string = str.lower()

    for word in lower_string.split():
        for char in ignored:
            word = word.replace(char, "")

        if word != "" and word not in histo_dict:
            histo_dict[word] = 1

        elif word != "":
            histo_dict[word] += 1

    counted_items = histo_dict
    histo_dict = {}

    for word, count in counted_items.items():
        num = count

        if num not in histo_dict:
            histo_dict[num] = [word]
        else:
            histo_dict[num].append(word)

    counted_items = histo_dict
    histo_dict = {}

    for counted in sorted(counted_items.items(), reverse=True):
        histo_dict[counted[0]] = counted[1]

    for count, words in histo_dict.items():
        histo_dict[count] = sorted(words)
        for word in histo_dict[count]:
            tags = "#" * count
            print(f"{word}: {tags}")

    return histo_dict


with open("/Users/Ethan/Hash-Tables/applications/histo/robin.txt") as f:
    words = f.read()

histo(words)
