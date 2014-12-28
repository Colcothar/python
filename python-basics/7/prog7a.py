import pymysql
con=pymysql.connect()
cur=con.cursor()	
val=input("Enter a month to check : ")
cur.execute('use test')
cur.execute('select name from details where month(dob)= %s'%val)
print('name')
rows=cur.fetchall()
for row in rows:
        for val in row:
                print(val,end='\t')
        print()
con.commit()
cur.close()
con.close()
