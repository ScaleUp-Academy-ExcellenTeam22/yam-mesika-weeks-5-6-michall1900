"""Cup of join
Receives from user lists and separator, return the lists into one,
separate them with the wanted separator (or '-' if separator doesn't receive)
and print the list.
"""

from functools import reduce


def join(*tuple_of_lists: tuple, sep: str = '-') -> list or None:
    """Receives tuple of lists, join them into one list and put the
    separator character to separate between them.
    If there is no lists, the function return None.
    If there is no separate character, the function put '-' between lists.
    I used this website:
    https://stackoverflow.com/questions/24116865/how-to-join-list-of-lists-with-separator-in-python
    :param tuple_of_lists: tuple of lists to join them into one
    :param sep: separate character to separate between each two different lists.
    :return: new list after join and separate lists.
    """
    # If lists is empty
    if len(tuple_of_lists) == 0:
        return None
    return list(reduce(lambda lst1, lst2: lst1 + [sep] + lst2, tuple_of_lists))


def main_cup_of_join():
    # Yam Mesika tests
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1]))
    print(join())

    # User choose lists
    lists = []
    temp_str = input("Enter A list. To finish, just press enter: ")
    while len(temp_str):
        lists.append(temp_str.split())
        temp_str = input("Enter A list. To finish, just press enter: ")
    separator = input("Enter A separator. If you don't want, just press enter: ")
    if len(separator) != 0:
        print(join(*lists, sep=separator))
    else:
        print(join(*lists))


if __name__ == "__main__":
    main_cup_of_join()
