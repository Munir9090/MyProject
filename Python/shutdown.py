from logging import shutdown
import os

shutdown = input("Yakin Shutdown ? (y/t) : ")
if shutdown == 't':
    exit()
else:
    os.system("shutdown /s /t 1")
