""" The program open logo file in binary style.
The binary file is encrypted and there are some secret lines.
Secret lines are the once that end with !, their len is >=5 and
they include just lower letters.
The program find and print secrete lines.
"""
import typing


def is_encrypted_line(line: str) -> bool:
    """ Return if the line's len is bigger than / equal to 5 and ends with !.
    :param line: string with only lower letters beside the last one.
    :return: true if it is secret line or not.
    """
    if len(line) < 5 or not line.endswith('!'):
        return False
    return True


def find_encrypted_lines_generator(encrypted_binary_file: typing.BinaryIO) -> str:
    """generator that return all of the secrete lines.
    :param encrypted_binary_file to decrypt it with format described before
    :return: secrete lines
    """
    curr_word = ""
    byte = (encrypted_binary_file.read(1))
    while byte:
        curr_char = byte.decode(errors="ignore")
        curr_word += curr_char
        if not curr_char.islower():
            if is_encrypted_line(curr_word):
                yield curr_word
            curr_word = ""
        byte = (encrypted_binary_file.read(1))


def main_encrypted_logo():
    with open("logo.jpg", 'rb') as my_file:
        for line in find_encrypted_lines_generator(my_file):
            print(line)


if __name__ == "__main__":
    main_encrypted_logo()
