"""Cup of join
Receives from user lists and separator, return the lists into one,
separate them with the wanted separator (or '-' if separator doesn't receive)
and print the list.
"""

from typing import Any


def join(sep: Any() = '-', *tuple_of_lists: tuple) -> list or None:
    """Receives tuple of lists, join them into one list and put the
    separator character to separate them.
    If there is no lists, the function return None.
    If there is no separate character, the function put '-' between lists.
    :param tuple_of_lists: list of lists to join them into one
    :param sep: separate character that will separate inside the new list
                between each two different lists.
    :return: new list after join and separate lists.
    """
    # If lists is empty
    if len(tuple_of_lists) == 0:
        return None
    result_list = []
    for i, lst in enumerate(tuple_of_lists):
        # After the first list, we put separate character.
        if i > 0:
            result_list.append(sep)
        result_list += lst
    return result_list


def main_cup_of_join():
    lists = []
    temp_str = input("Enter A list. To finish, just press enter: ")
    while len(temp_str):
        lists.append(temp_str.split())
        temp_str = input("Enter A list. To finish, just press enter: ")
    separator = input("Enter A separator. If you don't want, just press enter: ")
    if len(separator):
        print(join(*lists, sep=separator))
    else:
        print(join(*lists))


if __name__ == "__main__":
    main_cup_of_join()
