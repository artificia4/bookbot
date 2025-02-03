def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    chars_dict = get_chars_dict(text)
    dict_list = get_alpha_characters_dict(chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()
        

def sort_on(dict):
    return dict["count"]


def get_alpha_characters_dict(chars_dict):
    dict_list = [{'char': key, 'count': value} for key, value in chars_dict.items()]
    dict_list.sort(reverse=True, key=sort_on)
    for entry in dict_list:
        if entry["char"].isalpha():
            print(f"The '{entry['char']}' character was found {entry['count']} times")
    print("--- End report ---")    

main()