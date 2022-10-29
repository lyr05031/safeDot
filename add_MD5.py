def start_adding(file_MD5, MD5_database_path="MD5_database.txt"):
    with open(MD5_database_path, "a+") as fd:
        fd.write(file_MD5)
        fd.write("\n")
        fd.close()


if "__main__" == __name__:
    import get_file_MD5

    MD5 = get_file_MD5.MD5("96x (2022-02-08)/0b1034f063627ffa381f0fa2351e2656948870d197c6a06897e9d5827c5d6b24.exe")
    start_adding(MD5)
