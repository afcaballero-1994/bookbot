def get_num_words(text):
    list_words = text.split()
    return len(list_words)

def words_frequency(text):
    words = {}
    text = text.lower()

    for ch in text:
        if ch not in words:
            words[ch] = 1
        else:
            words[ch] += 1
    return words

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary_words):
    list_sorted_dict = []

    for ch, n in dictionary_words.items():
        if ch.isalpha():
            list_sorted_dict.append({"char": ch, "num": n})
    list_sorted_dict.sort(reverse=True, key=sort_on)
    return list_sorted_dict
