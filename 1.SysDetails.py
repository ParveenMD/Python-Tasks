print("MD Parveen")
import os
import psutil
from datetime import datetime
import shutil
print(".........................up time..............................")
now = datetime.now()
up_time = now.strftime("%H:%M:%S")
print("up Time =", up_time)
print(".........................CPU utilization........................")
print(psutil.cpu_freq())
while True:
    cpu = psutil.cpu_percent(interval=1)
    print(cpu)
    if cpu > 10:
        print("Reached the limit")
        break
print(".............................Disk utilization..........................")
path = "/Users/Administrator.DEMO/Documents"
stat = shutil.disk_usage(path)
print("Disk usage statistics:")
print(stat)
print("..................................Memory utilization........................")
pid = os.getpid ()
py = psutil.Process (pid)
memoryUse = py.memory_info () [0]/2.**30
print ('memory use:', memoryUse)