def process_integer_list(integer_list):
    unique_numbers = list(set(integer_list))
    number_tuple = tuple(unique_numbers)
    min_number = min(unique_numbers)
    max_number = max(unique_numbers)
    return number_tuple, min_number, max_number

if __name__ == "__main__":
    integers = [int(x) for x in input("Enter integers separated by space: ").split()]
    result_tuple, min_num, max_num = process_integer_list(integers)
    print("Unique numbers tuple:", result_tuple)
    print("Minimum number:", min_num)
    print("Maximum number:", max_num)

