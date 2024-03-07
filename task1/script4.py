def count_character_occurrences(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    occurrences = count_character_occurrences(input_str)
    for char, count in occurrences.items():
        print(f"{char}: {count}")

