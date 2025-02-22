import threading
import time


def write_into_file(file_name, message,lock):
    lock.acquire()
    with open(file_name,"a") as file:
        file.write(message)
        time.sleep(2)
        file.close()
    lock.release()

if __name__ == "__main__":
    number_of_thread=100
    threads=[]
    lock=threading.Lock()
    for i in range(number_of_thread):
        thread=threading.Thread(target=write_into_file,args=("demo.txt","This is Number {} \n".format(i),lock))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()