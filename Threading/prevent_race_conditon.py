import threading
import time
import random

def read_write(read_file,write_file,thread,lock):
    with lock:
        with open(read_file,"r") as read_file1:
                with open(write_file,"a") as write_file1:
                    read_lines=read_file1.readlines()
                    for line in read_lines:
                        time.sleep(0.1)
                        write_file1.write("Thread -" + str(thread) + "----" + line)

if __name__ == '__main__':
    thread_list=[]
    for num in range(3):
        lock = threading.Lock()
        read_file_name="read"+str(num)+".txt"
        t = threading.Thread(target=read_write, args=(read_file_name, "write.txt", str(num),lock))
        thread_list.append(t)

    for thread in thread_list:
        thread.start()

    for thread1 in thread_list:
        thread1.join(1000)
