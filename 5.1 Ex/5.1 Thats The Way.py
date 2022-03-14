"""Searching at given path files with given prefix, create a list of files name's
and print it.
"""

from os import listdir


def find_files_with_prefix(path: str, prefix: str) -> list:
    """ Receives path to search in and prefix to search files with that prefix.
    Return list of files name's that starting with the wanted prefix.
    Note: I searched and find the solution at this link:
    https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python

    @param path: For search at wanted path.
    @param prefix: For search files with that prefix
    @return: List of files name's that their prefix is as wanted that existing in wanted path.
    """
    return [file for file in listdir(path) if file.startswith(prefix)]


def send_specific_data() -> list:
    r"""Send wanted path and prefix to find_files_with_prefix function.
    @return:  List of files name's with prefix deep inside "yam mesika\ ... \images" directory.
    """
    return find_files_with_prefix(path=r".\yam mesika\Notebooks\week05\images", prefix="deep")


def main_that_is_the_way():
    files_list = send_specific_data()
    print("Files name's are:")
    [print(file_name) for file_name in files_list]


if __name__ == "__main__":
    main_that_is_the_way()
