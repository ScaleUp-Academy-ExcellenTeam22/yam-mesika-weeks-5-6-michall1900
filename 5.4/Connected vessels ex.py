
def generator_interleave(*iterables: list or str or tuple or dict or set):
    curr_index = 0
    is_return = True
    while is_return:
        is_return = False
        for item in iterables:
            if len(item) > curr_index:
                is_return = True
                yield item[curr_index]
        curr_index += 1


def interleave(*iterables: tuple) -> list:
    """Return a list of connected vessels (first cell of each iterable obj,
    then second and so on)
    :param iterables: iterables objects (list, tuple, string and so on)
    :return:
    """
    max_len = max(len(item) for item in iterables)
    res_list = []
    curr_len = 0
    while curr_len < max_len:
        res_list += [item[curr_len] for item in iterables if curr_len < len(item)]
        curr_len += 1
    return res_list


def main_connected_vessels():
    print(interleave('abc', [1, 2, 3], ('!', '@', '#'), {'hey': 'blue'}))
    print([ret_val for ret_val in generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))])


if __name__ == "__main__":
    main_connected_vessels()
