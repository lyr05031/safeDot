import time
import folder_scanning_system
import check_file_exist


class file_monitor:
    def __init__(self, path):
        self.path = path
    def __iter__(self):
        return self
    def __next__(self):
        if check_file_exist.start_checking(self.path) != "NSF":
            files_before = folder_scanning_system.get_all_files(self.path, [])
        else:
            raise StopIteration
        time.sleep(0.1)
        if check_file_exist.start_checking(self.path) != "NSF":
            files_now = folder_scanning_system.get_all_files(self.path, [])
        else:
            raise StopIteration
        if files_before != files_now:
            changed_files = [x for x in files_now if x not in files_before]
            return changed_files
        else:
            return 0
        


if "__main__" == __name__:
    new_monitor = file_monitor("/Users/liyiran/Downloads/untitled folder")
    new_monitor = iter(new_monitor)
    for x in new_monitor:
        print(x)
