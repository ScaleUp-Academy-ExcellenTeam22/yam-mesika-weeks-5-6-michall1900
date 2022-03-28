from functools import reduce


def join(*tuple_of_lists: list, sep: str = '-') -> list:
    """
    Receives tuple of lists, join them into one list, and put the
    separator character to separate between them.
    If there are no lists, the function returns an empty one.
    If there is no separate character, the function put '-' between lists.
    I used this website:
    https://stackoverflow.com/questions/24116865/how-to-join-list-of-lists-with-separator-in-python
    :param tuple_of_lists: Tuple of lists to join them into one.
    :param sep: Separate character to separate between every two different lists.
    :return: New list after join and separate lists.
    """
    return reduce(lambda lst1, lst2: lst1 + ([sep] if len(lst1) != 0 else []) + lst2, tuple_of_lists, [])


def main_cup_of_join() -> None:
    """
    Using join function to add between lists, separate them with wanted character and prints result.
    :return: None.
    """
    # Yam Mesika tests
    (lambda lists: [print(join(*lists)), print(join(*lists, sep='@'))])([[1, 2], [8], [9, 5, 6]])
    print(join([1]))
    print(join())


if __name__ == "__main__":
    main_cup_of_join()
