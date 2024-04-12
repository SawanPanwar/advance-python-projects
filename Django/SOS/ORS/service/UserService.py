from django.db import connection


class UserService:

    def nextPk(self):
        pk = 0
        with connection.cursor() as cursor:
            sql = "select max(id) from sos_user"
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        for d in result:
            pk = d[0]
        return pk + 1

    def add(self, f, l, e, p):
        sql = "insert into sos_user values((%s), (%s), (%s), (%s), (%s))"
        data = [UserService.nextPk(self), f, l, e, p]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
