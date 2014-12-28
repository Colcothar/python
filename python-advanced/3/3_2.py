import sqlite3
con = sqlite3.connect("test2.db")
cur = con.cursor()


cur.execute("drop table department")


cur.execute("create table department(id integer primary key,name text)")
cur.execute("insert into department values(1,'automation')")
cur.execute("insert into department values(2,'finance')")
cur.execute("insert into department values(3,'engg')")


cur.execute("drop table employee")


cur.execute("create table employee(id integer primary key,name text,age integer,salary real,deptid integer,foreign key(deptid) references department(id))")
cur.execute("insert into employee values(1,'abc',30,20500.5,2)")
cur.execute("insert into employee values(2,'bcd',25,25000.0,1)")
cur.execute("insert into employee values(3,'aad',20,20000.0,2)")
cur.execute("insert into employee values(4,'cad',22,27000.0,3)")
cur.execute("insert into employee values(5,'cae',22,27000.0,1)")
cur.execute("insert into employee values(6,'bgh',45,45000.0,2)")
cur.execute("insert into employee values(7,'xyx',33,35000.0,3)")
print("All department records")
sql="select * from department"
rows = cur.execute(sql)
for row in rows:
	print(row)
print("\nAll employee records")
sql="select * from employee"
rows = cur.execute(sql)
for row in rows:
	print(row)
#Youngest employee from each department
sql = "select min(age),name from employee group by deptid"
rows = cur.execute(sql)
print("\nYoungest employee from each department")
for row in rows:
	print(row)
#Department name and total number of employees in that department
sql = "select dep.name,count(*) from department as dep,employee where dep.id = deptid group by deptid"
rows = cur.execute(sql)
print("\nDepartment name and total number of employees in that department")
for row in rows:
	print(row)
#Department name with the highest paid employee (display employee name also)
sql="select max(salary),dept.name,e.name from employee as e,department as dept \
		where dept.id = deptid \
		group by deptid \
		order by salary desc"
cur.execute(sql)
print("\nDepartment name with the highest paid employee")
print(cur.fetchone())

con.commit()
con.close()
