_letter = "letter"
_count = "count"
_book_path = "books/frankenstein.txt"

def get_book_content_from(path):
    with open(path) as file:
        return file.read()
    
def split_text_from(content):
    return content.split()

def get_word_count_from(content):
    return len(split_text_from(content))

def get_letter_counts_from(content):
    letter_counts = {}

    for letter in content:
        letter = letter.lower()
        if (letter_counts.get(letter) == None):
            letter_counts[letter] = 1
        
        letter_counts[letter] += 1

    return letter_counts

def count_key(dict):
    return dict[_count]

def dict_to_list(dict, sort = False):
    letter_list = []

    for key in dict:
        if key.isalpha():
            letter_list.append({_letter: key, _count: dict[key]})
    
    if (not sort):
        return letter_list

    letter_list.sort(reverse=True, key=count_key)
    return letter_list

def generate_report():
    content = get_book_content_from(_book_path)
    word_count = get_word_count_from(content)
    letter_list = dict_to_list(
        get_letter_counts_from(content),
        True
    )

    print(f"--- Begin Report of {_book_path} ---")
    print(f"{word_count} words found in the document \n\n")

    for entry in letter_list:
        print(f"The '{entry[_letter]}' character was found {entry[_count]} times") 

    print("--- End Report ---")   

def main():
    generate_report()
   
main()