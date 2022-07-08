import pymysql


class Database:
    def __init__(self):
        self.self = self

    def con(self):
        try:
            con = pymysql.connect(
                host='127.0.0.1',
                user="sammy",
                password="sammy",
                database="python",
                port=3306,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            return con
        except:
            return "ERROR"

    def insert(self, into, params, values):
        connection = Database.con(self)
        with connection.cursor() as cur:
            cur.execute("INSERT INTO `"+into+"` ("+params+") VALUES ("+values+");")
            connection.commit()
            connection.close()
            return True

    def get(self, table, where, received):
        connection = Database.con(self)
        with connection.cursor() as cur:
            query = "SELECT "+received+" FROM `"+table+"` WHERE "+where+";"
            cur.execute(query)
            row = cur.fetchone()
            connection.close()
            return row

    def get_all(self, table, received):
        connection = Database.con(self)
        with connection.cursor() as cur:
            query = "SELECT " + received + " FROM `" + table + "`;"
            cur.execute(query)
            rows = cur.fetchall()
            connection.close()
            return rows

    def get_all_where(self, table, where, received):
        connection = Database.con(self)
        with connection.cursor() as cur:
            query = "SELECT " + received + " FROM `" + table + "` WHERE "+ where +";"
            cur.execute(query)
            rows = cur.fetchall()
            connection.close()
            return rows

    def remove(self, table, where):
        connection = Database.con(self)
        with connection.cursor() as cur:
            query = "DELETE FROM `"+table+"` WHERE "+where+";"
            cur.execute(query)
            connection.commit()
            connection.close()
            return True

    def set(self, table, where, setted):
        connection = Database.con(self)
        with connection.cursor() as cur:
            query = "UPDATE `"+table+"` SET "+setted+" WHERE "+where+";"
            cur.execute(query)
            connection.commit()
            connection.close()
            return True