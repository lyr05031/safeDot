import os


def start_checking(path):
    if os.path.isdir(path):
        return "F"  # folder
    elif os.path.isfile(path):
        return "SF"  # single file
    else:
        return "NSF"


if "__main__" == __name__:
    print(start_checking("/Users/liyiran/Desktop/code/SafeDotCyberSecurity/check_file_exist.py"))