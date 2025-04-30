def main():
    import sys
    if len(sys.argv) != 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    from stats import get_book_text    
    from stats import word_count
    from stats import char_count
    from stats import charsort
    sorted_chars = charsort()
    file_contents = get_book_text(sys.argv[1])
    total_words = word_count(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char_data in sorted_chars:
        char = char_data["char"]
        count = char_data["num"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

