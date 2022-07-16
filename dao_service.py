import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="thesis_bank"
)


def search_by_id(thesis_id):
    cursor = mydb.cursor()
    sql = "SELECT * FROM thesis WHERE id = %d"
    cursor.execute(sql, thesis_id)
    return cursor.fetchall()
