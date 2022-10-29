def matching(file_MD5, MD5_database_path="MD5_database.txt"):
    with open(MD5_database_path, "a+") as fd:
        fd.seek(0)
        res = fd.readlines()
        fd.close()
    if len(res) == 0:
        return 2  # empty file
    elif file_MD5 + "\n" not in res:
        return 3  # no data
    else:
        return 1  # is a virus


if "__main__" == __name__:
    new_MD5_scanner = matching("b2aa70a4933a9a8ca974fdf9e762e084")
    print(new_MD5_scanner)
