#coding=utf-8


import os
import time


os.system("./data_copy.sh")
time.sleep(60)

os.system("python3 MinIO_config_ip.py")
time.sleep(5)



