def number_of_words(text):
    words = []
    words = text.split()
    num_words = len(words)
    return print(f"{num_words} words found in the document")

def symbol_breakdown(text):
    symbols = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in symbols:
            symbols[lower_char] = 1
        else:    
            symbols[lower_char] += 1
    return symbols

def sort_dictionaries(dict):
    list = []
    for symbol, number in dict.items():
        list.append({"char": symbol, "num": number})
    list.sort(reverse=True, key=lambda dict: dict["num"])
    return list