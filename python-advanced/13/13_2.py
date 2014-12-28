import sqlite3
con = sqlite3.connect("test1.db",isolation_level=None)
#isolation_level = "None" sets autocommit on
cur = con.cursor()
cur.execute("create table if not exists person(name text,age integer,areaofinterest text, occupation text)")
cur.execute("insert into person values(?,?,?,?)",("Akash Sharma",32,"Music","Engineer"))
cur.execute("insert into person values(?,?,?,?)",("Anna Sara",27,"Dance","Dancer"))
cur.execute("insert into person values(?,?,?,?)",("Rimi Sharman",30,"Music","Teacher"))
cur.execute("insert into person values(?,?,?,?)",("Niki Sharma",25,"Travel","Engineer"))
cur.execute("insert into person values(?,?,?,?)",("Sharma Manohar",27,"Music","Doctor"))
cur.execute("insert into person values(?,?,?,?)",("Sam George",32,"Cooking","Engineer"))
sql="select * from person"
rows = cur.execute(sql)
print("All persons")
for row in rows:
	print(row)
#All persons whose last name is "Sharma"
sql="select * from person where name like '%Sharma'"
print("\nAll persons whose last name is 'Sharma'")
rows = cur.execute(sql)
for row in rows:
	print(row)
#Most common area of interest among all persons
sql = "select count(*),areaofinterest from person group by areaofinterest order by count(*) desc"
cur.execute(sql)
print("\nMost common area of interest")
print(cur.fetchone())
#Delete all entries having area of interest other than ( Music, Dance, Sports, Travel)
sql = "delete from person where areaofinterest not in ('Music','Dance','Sports','Travel')"
rows = cur.execute(sql)
print("\nRows after deleting")
sql="select * from person"
rows = cur.execute(sql)
for row in rows:
	print(row)

con.close()
