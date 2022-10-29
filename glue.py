"""
Provide Core Data Swap Service
THE MOST IMPORTANT FILE IN SAFEDOT
"""
import get_file_MD5
import local_scanning_system
import web_scanning_system
import add_MD5
import folder_scanning_system
import os


class main_scanner:
    def __init__(self, path, flag):
        self.path = path
        self.flag = flag
        if self.flag == "F":
            self.path = folder_scanning_system.get_all_files(self.path, [])
    def __iter__(self):
        return self        
    def __next__(self):
        if self.flag != 1:
            if self.flag == "SF":
                file_MD5 = get_file_MD5.MD5(self.path)
                self.path = self.path[1:]
                self.flag = 1
                return data_processing_unit(file_MD5, self.path)
            else:
                for x in self.path:
                    file_MD5 = get_file_MD5.MD5(x)
                    self.path = self.path[1:]
                    return data_processing_unit(file_MD5, x)
                raise StopIteration
        else:
            raise StopIteration


def data_processing_unit(file_MD5, path):
    res = start_scanning(file_MD5)
    if res == 1:
        add_MD5.start_adding(file_MD5)
        return "{}是病毒!".format(path)
    elif res == "local":
        return "{}是病毒!".format(path)
    elif res == 2:
        return "{}不是病毒!".format(path)
    else:
        return "没有关于{}的数据!".format(path)


def start_scanning(file_MD5):
    if local_scanning_system.matching(file_MD5) != 1:  # empty file or no data
        new_scanner = web_scanning_system.scanner(file_MD5)
        res_dasheng = new_scanner.dasheng_sandbox()
        if res_dasheng == 3:  # no data
            res_threat_book = 3
            #res_threat_book = new_scanner.threat_book()
            if res_threat_book == 3:  # no data
                res_virus_total = new_scanner.virus_total()
                if res_virus_total == 3:  # no data
                    return 3  # no data
                else:
                    if res_virus_total == 2:
                        return 2  # not a virus
                    else:
                        return 1  # is a virus
            else:
                if res_threat_book == 2:
                    return 2  # not a virus
                else:
                    return 1  # is a virus
        else:
            if res_dasheng == 2:
                return 2  # not a virus
            else:
                return 1  # is a virus
    else:
        return "local"


if "__main__" == __name__:
    import check_file_exist

    
    new_scanner = main_scanner("/Users/liyiran/Desktop/code/SafeDotCyberSecurity/glue.py", check_file_exist.start_checking("/Users/liyiran/Desktop/code/SafeDotCyberSecurity/glue.py"))
    iter_scanner = iter(new_scanner)
    for x in iter_scanner:
        print(x)
