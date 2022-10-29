import hashlib


def MD5(file_path):
    with open(file_path, "rb") as fd:
        res = fd.read()
        new_hash_scanner = hashlib.md5(res)
        file_MD5 = new_hash_scanner.hexdigest()
        return file_MD5
