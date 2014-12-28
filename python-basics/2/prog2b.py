import sqlite3
con=sqlite3.connect('test.db')
cur=con.cursor()	
name=input("Enter name : ")
dob=input("Enter dob(yyyy,mm,dd) : ")
#cur.execute('use test')
cur.execute('''insert into details values (%s,%s)''' % (name,dob))
cur.execute('select * from details')
rows=cur.fetchall()
for row in rows:
	print(row)
con.commit()
cur.close()
con.close()
