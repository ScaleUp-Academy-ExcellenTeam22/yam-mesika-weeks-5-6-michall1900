from typing import BinaryIO
import re


def find_encrypted_lines_generator(encrypted_binary_file: BinaryIO) -> str:
    """
    Generator that return all secrete lines in the encrypted file.
    The meaning of secrete line is a line within the file that contains only lowercase
    letters, ending with ! and whose length is >=5.
    :param encrypted_binary_file to find and decrypt secrete lines
    :return: secrete lines
    """
    for line in encrypted_binary_file:
        for match in re.findall("([a-z]{5}[a-z]*!)", line.decode(errors='ignore')):
            yield match


def main_encrypted_logo() -> None:
    with open("logo.jpg", 'rb') as my_file:
        [print(secrete_line) for secrete_line in find_encrypted_lines_generator(my_file)]


if __name__ == "__main__":
    main_encrypted_logo()
