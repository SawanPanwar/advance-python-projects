from django.db import connection


class MarksheetService:

    def nextPk(self):
        pk = 0
        with connection.cursor() as cursor:
            sql = "select max(id) from sos_marksheet"
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        for d in result:
            pk = d[0]
        return pk + 1

    def add(self, data):
        r = data['rollNo']
        n = data['name']
        p = data['physics']
        c = data['chemistry']
        m = data['maths']
        sql = "insert into sos_marksheet values((%s), (%s), (%s), (%s), (%s), (%s))"
        data = [MarksheetService.nextPk(self), r, n, p, c, m]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def update(self, data):
        r = data['rollNo']
        n = data['name']
        p = data['physics']
        c = data['chemistry']
        m = data['maths']
        i = data['id']
        sql = "update sos_marksheet set rollNo = (%s), name = (%s), physics = (%s), chemistry = (%s), maths = (%s) where id = (%s)"
        data = [r, n, p, c, m, i]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def delete(self, id):
        sql = "delete from sos_marksheet where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def get(self, id):
        sql = "select * from sos_marksheet where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "rollNo", "name", "physics", "chemistry", "maths")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def search(self, params):
        name = params.get("name", "")
        pageNo = params.get("pageNo", 0)
        pageSize = params.get("pageSize", 0)
        sql = "select * from sos_marksheet where 1=1"
        if name != "":
            sql += " and name like '" + name + "%%' "
        if (pageNo > 0):
            pageNo = (pageNo - 1) * pageSize
            sql += " limit %s, %s"

        print("sql => ", sql)
        cursor = connection.cursor()
        cursor.execute(sql, [pageNo, pageSize])
        result = cursor.fetchall()
        columnName = ("id", "rollNo", "name", "physics", "chemistry", "maths")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res
