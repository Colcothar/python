from tkinter import *
top = Tk()
a=0
b=0
x=0
def print_contents() :
	#global x
	x=v.get()
	a=contents1.get()
	b=contents2.get()
	print("%s %s"%(a,b))
	
	if x==1:
		c=a+b
		print(c)
		contents3.set(c)
	elif x==2:
		c=a-b
		print(c)
		contents3.set(c)
	elif x==3:
		c=a*b
		print(c)
		contents3.set(c)
	elif x==4:
		c=a/b
		print(c)
		contents3.set(c)
v = IntVar()

rb1 = Radiobutton(text='add', value="1", variable=v, command=print_contents)
rb2 = Radiobutton(text='subtract', value="2", variable=v, command=print_contents)
rb3 = Radiobutton(text='multiply', value="3", variable=v, command=print_contents)
rb4 = Radiobutton(text='divide', value="4", variable=v, command=print_contents)
rb1.pack(anchor=W);
rb2.pack(anchor=W);
rb3.pack(anchor=W);
rb4.pack(anchor=W);



entry1 = Entry(top, width=50)
entry1.pack()

contents1 = IntVar()
contents1.set("")

entry1["textvariable"] = contents1




entry2 = Entry(top, width=50)
entry2.pack()

contents2 = IntVar()
contents2.set("")

entry2["textvariable"] = contents2




label = Label(top, text='Result:')
label.pack()



entry3=Entry(top, width=50)
entry3.pack()

contents3=IntVar()
contents3.set("")

entry3["textvariable"]= contents3



mainloop()
