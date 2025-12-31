def get_num_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letter_count_dict = dict()
    for unit in text:
        if unit.lower() in letter_count_dict:
            letter_count_dict[unit.lower()] += 1
        else:
            letter_count_dict[unit.lower()] = 1
    return letter_count_dict

def report(dict_of_letters):
    list_of_dicts = []
    for letter, num in dict_of_letters.items():
        if letter.isalpha():
            letter_dict = {"char": letter, "num": num}   
            list_of_dicts.append(letter_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
 
def sort_on(count):
    return count["num"]