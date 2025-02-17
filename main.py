book = "books/frankenstein.txt"

def main():
    
    with open(book) as f:
        file_contents = f.read()
        print(f"--- Begin report of {book} ---")
        print(f"{word_count(file_contents)} words found in the document \n")
        letter_count(file_contents)
        print("--- End report ---")
        
def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def letter_count(file_contents):
    counts = {}
    
    for letter in file_contents:
        if letter.lower() not in counts:
            counts[f"{letter.lower()}"] = 1
        elif letter.lower() in counts:
            num = counts[letter.lower()]
            counts[letter.lower()] = num + 1

    for k in counts:
        if k.isalpha():
            print(f"The '{k}' character was found {counts[f"{k}"]} times")    
    
main()

