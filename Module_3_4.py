def single_root_words(root_word, *other_words):
    root_word = input("Enter your root word & press Enter button: ")
    other_words = tuple(input("Enter your list of several words spelled with space & press Enter button: ").split())
    same_words = []
    for i in range(len(other_words)):
        if other_words[i].lower() in root_word.lower() or root_word.lower() in other_words[i].lower():
            same_words.append(other_words[i])
    return same_words

result = print(single_root_words("",()))