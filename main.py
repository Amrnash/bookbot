def main():
    text = get_book_text("books/frankenstein.txt")
    print(get_char_freq(text))


def chars_dict_to

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_freq(text):
    dic = {}
    words = text.split()
    for word in words:
        lower_word = word.lower()
        if lower_word in dic:
            dic[lower_word] += 1
        else:
            dic[lower_word] = 1
    return dic
main()