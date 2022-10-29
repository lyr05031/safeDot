from tkinter import filedialog
import tkinter
import glue
import check_file_exist
import threading
import file_monitoring_system

root = tkinter.Tk()


#日常扫描
def scan_add(path: str):
    existence: str = check_file_exist.start_checking(path)
    if existence != "NSF":
        new_scanner: object = glue.main_scanner(path, existence)
        new_scanner = iter(new_scanner)
        for x in new_scanner:
            print(x)
    else:
        print("无此文件")


#文件监控
def monitoring(path: str):
    new_monitor: object = file_monitoring_system.file_monitor(path)
    for x in iter(new_monitor):
        if x != 0 and x != []:
            for y in x:
                scan_add(y)


#开线程，1是日常扫描，2是文件监控
def start_new_thread(path, flag):
    if flag == 1:
        threading.Thread(target=scan_add, args=(path, )).start()
    else:
        threading.Thread(target=monitoring, args=(path, )).start()    

if __name__ == "__main__":
    while True:
        choice = int(input("1.扫描, 2.文件夹监控, 3.退出\n"))
        if choice == 1:
            start_new_thread(filedialog.askopenfilename(), 1)
        elif choice == 2:
            start_new_thread(filedialog.askdirectory(), 2)
        elif choice == 3:
            break 
        