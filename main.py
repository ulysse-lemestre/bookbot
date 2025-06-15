from stats import get_num_words, get_num_char_dic, get_char_count_list
import sys

def get_book_text(filepath):
    fileContent = ""
    with open(filepath) as f:
        fileContent = f.read()
    return fileContent

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        filePath = sys.argv[1]

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filePath}...")

        content = get_book_text(filePath)
        num_words = get_num_words(content)

        print("----------- Word Count ----------")
        print(f" Found {num_words} total words")

        num_char_dic = get_num_char_dic(content)
        num_char_list = get_char_count_list(num_char_dic)

        print("--------- Character Count -------")
        for i in num_char_list:
            if i["char"].isalpha():
                print(f"{i['char']}: {i['num']}")

        print("============= END ===============")



main()