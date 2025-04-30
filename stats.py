import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(file_contents):
    words = file_contents.split()
    count = len(words)
    return count

def get_num_words():
    book_text = get_book_text(sys.argv[1])
    num = word_count(book_text)
    print(f"{num} words found in the document")

def char_count():
    book_text = get_book_text(sys.argv[1])
    chardic = {}
    for char in book_text:
        char = char.lower()
        if char in chardic:
            chardic[char] += 1
        else: chardic[char] = 1
    return chardic

def sort_on(charsort):
    return charsort["num"]

def charsort():
    chardic = char_count()
    charsort = []
    for x, y in chardic.items():
        newentry = {
	    "char": x,
	    "num": y
	}
        charsort.append(newentry)
    charsort.sort(reverse=True, key=sort_on)
    return charsort
