try:
    for num in range(3):
        filename="read"+str(num)+".txt"
        with open(filename,"r") as read_file:
            with open("write.txt","a") as write_file:
                read_lines=read_file.readlines()
                for line in read_lines:
                    write_file.write(str(num) + "-" + line)

            write_file.close()
        read_file.close()

except Exception as e:
    print("Error in Reading and Writing file : {0}".format(e))
