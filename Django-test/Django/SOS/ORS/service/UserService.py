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

    def add(self, data):
        f = data['firstName']
        l = data['lastName']
        e = data['email']
        p = data['password']
        sql = "insert into sos_user values((%s), (%s), (%s), (%s), (%s))"
        data = [UserService.nextPk(self), f, l, e, p]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def update(self, data):
        f = data['firstName']
        l = data['lastName']
        e = data['email']
        p = data['password']
        i = data['id']
        sql = "update sos_user set firstName = (%s), lastName = (%s), email = (%s), password = (%s) where id = (%s)"
        data = [f, l, e, p, i]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def delete(self, id):
        sql = "delete from sos_user where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def auth(e, p):
        sql = "select * from sos_user where email = (%s) and password = (%s)"
        data = [e, p]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "email", "password")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def get(self, id):
        sql = "select * from sos_user where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "email", "password")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def search(self, params):
        fname = params.get("firstName", "")
        pageNo = params.get("pageNo", 0)
        pageSize = params.get("pageSize", 0)
        sql = "select * from sos_user where 1=1"
        if fname != "":
            sql += " and firstName like '" + fname + "%%' "
        if (pageNo > 0):
            pageNo = (pageNo - 1) * pageSize
            sql += " limit %s, %s"
        cursor = connection.cursor()
        cursor.execute(sql, [pageNo, pageSize])
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "email", "password")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res
