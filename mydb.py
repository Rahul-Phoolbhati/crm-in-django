import mysql.connector

dataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root123"
)


#prepare acursor object

cursorObject=dataBase.cursor()

#craete a db

cursorObject.execute("CREATE DATABASE my_django_projet")
print("All Done")