import psycopg2


#connection to "chinook" database
connection = psycopg2.connect(database="chinook")

#build cursor object of database
cursor = connection.cursor()

#Query 1 - fetch all records from * Artist * table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["AC/DC"])

#fetch all results
results = cursor.fetchall()

#fetch one result
# oneresult = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)
