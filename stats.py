def num_of_words(book):
    words = book.split()
    num_words = len(words)
    return num_words


def num_char(book):
    book = str.lower(book)
    count = {}
    for char in book:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count


def get_value(d):
    return list(d.values())[0]  
def sort_list(dict):
    sorted_list = []

    for char in dict:
        sorted_list.append ({char:dict[char]})

    sorted_list.sort(reverse=True, key=get_value)
    
    return sorted_list