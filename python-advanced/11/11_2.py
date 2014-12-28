import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
l=[]

#The following has to be read from keyboard
while(1):
	a=int(input("Enter 1 To enter the input 2 Stop giving input"))
	if(a==1):
		n=input("Enter the name : ")
		d=input("Enter Date of birth in this format yyyy-mm-dd :")
		s=(n,d)
		l.append(s)
	elif(a==2):
		break
'''n1="abc"
dob1="1981-04-23"
n2="def"
dob2="1955-01-20"
n3="xyz"
dob3="1975-04-05"
n4="ddd"
dob4="1982-12-01"
L = [(n1,dob1),(n2,dob2),(n3,dob3),(n4,dob4)]
'''
cur.execute("create table if not exists stud_data(name text,dob date)")

#Use executemany to store 4 records
cur.executemany("insert into stud_data values(?,date(?))",l)

print("All records")
sql="select * from stud_data"
rows = cur.execute(sql)
for row in rows:
	print(row)

#Name and age of person in years
sql = "select name,(julianday('now')-julianday(dob))/365 from stud_data"

rows = cur.execute(sql)
print("\nName and age of person in years")
for row in rows:
	print(row[0],int(row[1]))
	
#All persons whose birthday falls in the month '04'
m='04';
sql = "select name,dob from stud_data where ?=strftime('%m',dob)"
rows = cur.execute(sql,(m,))
print("\nAll persons whose birthday falls in the month '04'")
for row in rows:
	print(row[0],row[1])

con.commit()
con.close()
