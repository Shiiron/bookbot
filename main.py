# Main function to call for code execution
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report = book_report(book_path, text)
    print(report)

# @params text: string
# @return number of words in text
def get_num_words(text):
    words = text.split()
    return len(words)

# @params path : string
# @return file content
def get_book_text(path):
    with open(path) as f:
        return f.read()

# @params text : string
# @return Object {key => value} where key is the letter and value the number of letters in text
def get_letters(text):
    letters_array =  {}
    for l in text:
        letter = l.lower()
        if (letter in letters_array):
            letters_array[letter] += 1
        else:
            letters_array[letter] = 1

    return letters_array

def sort_num(obj):
    return obj["num"]

def sorted_letters(text):
    list_letter = []
    letters = get_letters(text)
    for l in letters:
        if (l.isalpha()):
            list_letter.append({"name": l, "num": letters[l]})
    list_letter.sort(reverse=True, key=sort_num)

    return list_letter

def book_report(book, text):
    words = get_num_words(text)
    letter_list = sorted_letters(text)
    print(f'--- Begin report of {book} ---')
    print(f'{words} words found in the document')
    print()
    for l in letter_list:
        print(f'The {l["name"]} character was found {l["num"]} times')
    print('--- End report ---')

main()