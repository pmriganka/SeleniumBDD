import mysql.connector


def createDbConnection():
    global mydb
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Highmyopia1@",
    database = "mysql"
)

def getMySqlQuery(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    for item in mycursor:
        print(item)


createDbConnection()
getMySqlQuery("select * from selenium")



