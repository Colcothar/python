l=eval(input("Enter list of tuples.."))
s=list((filter(lambda x:not(x[0]%x[1]!=0),l)))
print(s)
