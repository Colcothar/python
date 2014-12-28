n=int(input("enter the value of n"))
for i in range(n):
        value=1
        plist=[value]
        for j in range(i):
                value=value*(i-j)*1/(j+1)
                plist.append(int(value))
        print("{:^40s}".format(plist))
print ("done")

