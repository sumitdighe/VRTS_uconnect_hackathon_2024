import os
import subprocess
import threading
import time


def run_script_in_terminal(script):
    os.system(f'start cmd.exe /k {script}')

script1 = "python test2.py"
script2 = "python ModelsForDisk.py"
script3 = "python ModelsForCpu.py"
script4 = "python FileChangeLog.py"

t1 = threading.Thread(target=run_script_in_terminal, args=(script1,))
t2 = threading.Thread(target=run_script_in_terminal, args=(script2,))
t3 = threading.Thread(target=run_script_in_terminal, args=(script3,))
t4 = threading.Thread(target=run_script_in_terminal, args=(script4,))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()


