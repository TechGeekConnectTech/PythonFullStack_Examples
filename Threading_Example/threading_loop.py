import threading
import time

def show_details(message):
    print("Child Thread Name : {} \n".format(message))



if __name__ == "__main__":
    threads=[]
    number_of_thread=100
    for thread in range(number_of_thread):
        t=threading.Thread(target=show_details,args=("This is Threading Example {}".format(thread),))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()