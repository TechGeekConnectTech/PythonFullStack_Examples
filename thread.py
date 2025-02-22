import moduleos

import threading

def task1():
    print("Task 1 is assinged to Thread : {}".format(threading.current_thread().name))
    print("ID of Process Running Task1 : {}.".format(os.getpid()))

def task2():
    print("Task 2 is assinged to Thread : {}".format(threading.current_thread().name))
    print("ID of Process Running Task1 : {}.".format(os.getpid()))

if __name__ == "__main__":
    print("ID of Process running from Main Program : {}".format(os.getpid()))
    print("Main Thread Name : {}".format(threading.current_thread().name))

    t1=threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()