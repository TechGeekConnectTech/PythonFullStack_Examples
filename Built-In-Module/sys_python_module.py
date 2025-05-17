import sys
'''
print("Print Python Version : ",sys.version)
print("SHow platform information",sys.platform)
print("Print path:",sys.path)
#sys.exit()
print("API Version:",sys.api_version)
'''
print(sys.argv[0])
for arg in sys.argv:
    if arg == "Ayush":
        print(f"{arg} :He is fresher")
    else:
        print(f"{arg} : Experience")
