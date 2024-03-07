import os

def get_file_extension(filename):
    _, extension = os.path.splitext(filename)
    if not extension:
        raise ValueError("No extension found for the file.")
    return extension

if __name__ == "__main__":
    filename = input("Enter the file name: ")
    try:
        print("File extension:", get_file_extension(filename))
    except ValueError as e:
        print("Error:", e)

