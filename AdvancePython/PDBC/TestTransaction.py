import pymysql

connection = pymysql.connect(host='localhost', port=3307, user='root', password='root', db='advance_python')
connection.autocommit(False)
try:
    with connection.cursor() as cursor:
        sql = "insert into emp values((%s), (%s), (%s))"
        cursor.execute(sql, (24, 'a', 1500))
        cursor.execute(sql, (25, 'b', 1500))
        cursor.execute(sql, (26, 'c', 1500))
        cursor.execute(sql, (26, 'd', 1500))
    connection.commit()
    print("Data Inserted Successfully...!!!")
except:
    connection.rollback()
    print("Duplicate primary key")
finally:
    connection.close()
