import mysql.connector
conn = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
inp = input("Input your search: ")
cursor = conn.cursor()
query = cursor.execute("select * from Dictionary where Expression = '%s' " % inp)
print(query)
result = cursor.fetchall()
for i in result:
    print(i)