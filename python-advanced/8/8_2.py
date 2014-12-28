from threading import *

def fun(a,lock):
	global tot_sum
	print("In thread ",current_thread().name)
	
	for i in a:
		lock.acquire()
		tot=tot_sum
		tot_sum=i+tot
		print("Partial Sum :",tot_sum)
		lock.release()
	
array=[1,2,3,4,5,6,7,8,9,10,11,12]
tot_sum=0
l=Lock()
	
t1=Thread(target=fun,args=(array[0:len(array)//4],l))
t2=Thread(target=fun,args=(array[len(array)//4:len(array)//2],l))
t3=Thread(target=fun,args=(array[len(array)//2:(3*len(array)//4)],l))
t4=Thread(target=fun,args=(array[(3*len(array)//4):],l))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print("Total Sum Of array : ",tot_sum)

