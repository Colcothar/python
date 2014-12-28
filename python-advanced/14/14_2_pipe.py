from multiprocessing import *
import os
import time
def child(c):
	
	print("Process Started and Process Id : ",os.getpid())
	time.sleep(5)	
	c.send("Hai This is message from child process")
	print(c.recv())
	c.close()

p,c=Pipe()
child_process=Process(target=child,args=(c,))
child_process.start()

print(p.recv())
time.sleep(5)	
p.send("This is message from Parent")	

child_process.join()
