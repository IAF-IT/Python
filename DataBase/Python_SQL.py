import pypyodbc

mySQLserver = "DESKTOP-LM9GKVJ\SQLEXPRESS"
myDatabase = "pubs"

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mySQLserver + ';'
                              'Database=' + myDatabase + ';')

cursor = connection.cursor()
mySQLquery = ("""
                 SELECT au_lname, au_fname, city
                 FROM dbo.authors
                 WHERE city = 'Oakland'
""")

cursor.execute(mySQLquery)
results = cursor.fetchall()

for row in results:
    lname = row[0]
    fname = row[1]
    city = row[2]
    print("author name: " + str(lname) + " " + str(fname)  + " from " + str(city))

connection.close()