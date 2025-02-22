import threading
import time

def write_into_file(file_name,message,lock):
    lock.acquire()
    with open(file_name,"a") as file:
        time.sleep(2)
        file.write(message)
        file.close()
    lock.release()


if __name__ == "__main__":
    threads=[]
    lock=threading.Lock()
    for num in range(100):
        t=threading.Thread(target=write_into_file,args=("number.txt","\n This is number : {}".format(num),lock))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()