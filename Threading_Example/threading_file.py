import threading
from time import sleep


def file_read_write(read_file_name,write_file_name,thread):
    try:
        with open(read_file_name,"r") as file_read:
            with open(write_file_name,"a") as file_write:
                read_text=file_read.readlines()
                for read in read_text:
                    sleep(1)
                    file_write.write(thread + "-" + read)

    except Exception as e:
        print("Error in Reading and Writting file : {0}".format(e))

if __name__ == '__main__':
    thread_list=[]
    for num in range(4):
        file_name="number"+str(num)+".txt"
        print(file_name)
        thread=threading.Thread(target=file_read_write,args=(str(file_name),"write_file.txt",str(num)))
        thread_list.append(thread)

    for num in thread_list:
        num.start()

    for num in thread_list:
        num.join()