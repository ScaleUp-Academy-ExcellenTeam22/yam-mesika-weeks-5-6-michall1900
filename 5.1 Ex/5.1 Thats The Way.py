from functools import partial
from os import listdir


def find_files_with_wanted_prefix(path: str, prefix: str) -> list:
    """
    Receives path to search in and prefix to search files with that prefix.
    Return list of files name's that starting with the wanted prefix.
    Note: I searched and find the solution at this link:
    https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python

    @param path: For search at wanted path.
    @param prefix: For search files with that prefix.
    @return: List of files name's that their prefix is as wanted that existing in wanted path.
    """
    return [file for file in listdir(path) if file.startswith(prefix)]


def main_that_is_the_way() -> None:
    """
    Searching at the 'images' directory all files whose prefix is 'deep' and print them.
    :return: None.
    """
    find_deep_at_images = partial(find_files_with_wanted_prefix,
                                  path=r"..\..\yam mesika\Notebooks\week05\images", prefix="deep")
    files_list = find_deep_at_images()
    print("Files name's are:")
    for file_name in files_list:
        print(file_name)


if __name__ == "__main__":
    main_that_is_the_way()
