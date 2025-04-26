import threading
import time
import random

lock=threading.Lock()
def write_data(thread_name):
    for i in range(5):
        time.sleep(0.1)
        with lock:
            print(f"Thread : {thread_name} Writing Data")

if __name__ == '__main__':
    thread_list=[]
    for num in range(3):
        t = threading.Thread(target=write_data, args=(str(num)))
        thread_list.append(t)

    for thread in thread_list:
        thread.start()

    for thread1 in thread_list:
        thread1.join(1000)

