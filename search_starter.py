import os
import time
import psutil

imlogin = "imlogin.exe"

for i in range(1000):
    os.startfile(r"C:\IM\Search\S4.exe")
    processes = []
    for process in psutil.process_iter():
        processes.append(process.name())
    if imlogin in processes:
            print('yes')
            break
    time.sleep(1.5)
    os.system(r'taskkill /IM S4.exe')
