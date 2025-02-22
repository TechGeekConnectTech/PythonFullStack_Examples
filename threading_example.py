import threading
import time

def print_statement(name,*args):
    print(name,*args)
    time.sleep(10)
    print("\n Thread End", *args)

print_name="Treading start.."

thread1=threading.Thread(target=print_statement,args=(print_name,1))
thread2=threading.Thread(target=print_statement,args=(print_name,1,2))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Threading is completed")