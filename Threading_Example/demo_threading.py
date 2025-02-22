import threading
import time

def show_details(message):
    print("Child Thread Name : {} \n".format(message))



if __name__ == "__main__":
    t1=threading.Thread(target=show_details,args=("This is Threading Example 1",))
    t2 = threading.Thread(target=show_details, args=("This is Threading Example 2",))
    t3 = threading.Thread(target=show_details, args=("This is Threading Example 3",))
    t4 = threading.Thread(target=show_details, args=("This is Threading Example 4",))
    print("Main Thread Name : {} \n".format(threading.current_thread().name))
    print("Starting Thread \n")
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("Finishing Main Thread \n ")