import os


def get_all_files(path, file_list):
    for x in os.listdir(path):
        final_path = os.path.join(path, x)
        if x[0] == ".":
            continue
        elif os.path.isdir(final_path):
            get_all_files(final_path, file_list)
        else:
            file_list.append(final_path)
    return file_list

if "__main__" == __name__:
    print(get_all_files("/Users/liyiran/Desktop", []))
