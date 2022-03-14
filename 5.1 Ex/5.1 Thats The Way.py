import os
FILES_PREFIX = "deep"


def find_files_at_path_with_wanted_prefix(path='.', prefix=FILES_PREFIX):
    """
    The function receives path to search in and prefix to search files with that prefix.
    The function return list of files name's that starting with thw wanted prefix.
    Note: I searched and find the solution at this link:
    https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python

    @param path: String, for search at wanted path.
    @param prefix: String, for search files with that prefix
    @return: List of files name's that their prefix is as wanted that existing in wanted path.
    """
    files_list_with_wanted_suffix = [file for file in os.listdir(path) if file.startswith(prefix)]
    return files_list_with_wanted_suffix


wanted_path = input("Please Enter wanted path: ")
files_list = find_files_at_path_with_wanted_prefix(path=wanted_path)
print("The list is:")
for file_name in files_list:
    print(file_name)
