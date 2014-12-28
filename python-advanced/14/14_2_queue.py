from multiprocessing import *
import os
import time
def child(q):
	
	print("Process Started and Process Id : ",os.getpid())
	time.sleep(5)	
	q.put("Hai This is message from child process")
	print(q.get())
	
if __name__=="__main__":
        queue=Queue()
        child_process=Process(target=child,args=(queue,))
        child_process.start()

        print(queue.get())
        time.sleep(5)	
        queue.put("This is message from Parent")

        child_process.join()


