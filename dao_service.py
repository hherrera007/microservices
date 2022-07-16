import mysql.connector


def search_by_id(thesis_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="thesis_bank"
    )
    cursor = mydb.cursor(buffered=True, dictionary=True)
    sql = "SELECT id, title, status FROM thesis where id = %s"
    cursor.execute(sql, (thesis_id,))
    row = cursor.fetchone()
    id_ = -1
    title = ''
    status = ''
    print(row)
    if row is not None:
        id_, title, status = row['id'], row['title'], row['status']
    cursor.close()
    mydb.close()
    return id_, title, status
