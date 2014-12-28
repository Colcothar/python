t=[]
a=int(input("Enter the number of rows os pascal triangle:"))
for r in range(a):
	for c in range(r+1):
		if c==0:
			t.append([1])
		elif c==r:
			t[r].append(1)
		else:
			t[r].append(t[r-1][c] + t[r-1][c-1])
for r in t:
	n=len(r)
	s=int((50-5*n)/2)
	padding=" "*s
	formatting=" "
	for val in r:
		formatting +="%5d" %val
	print(padding+formatting)
