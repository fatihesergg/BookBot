def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        words = return_words(file_content)
        unique_words = return_chars(words)
        print("--- Begin report of books/frankenstein.txt ---\n")
        print(f"{len(words)} words found in document\n\n\n")
        for w in unique_words.keys():
            print(f"The {w} appears {unique_words[w]} times")

def return_words(content):
    words = content.split()
    return words

def return_chars(words):
    char_list =  {}
    for w in words:
            for c in w.lower():
                if c not in char_list:
                    char_list[c] = 1
                else:
                    char_list[c] += 1
    return char_list
main()
