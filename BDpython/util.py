import cx_Oracle
#esta variable tiene los atributos de conexion
CONN_INFO = {
    'host': 'localhost',
    'port': 1521,
    'user': 'dbquebin',
    'psw': '123456',
    'service': 'pdborcl.home'
}

#tiene la cadena de conexion
CONN_STR = '{user}/{psw}@{host}:{port}/{service}'.format(**CONN_INFO)


class util:
    def __init__(self):
        self.conn = cx_Oracle.connect(CONN_STR)
        self.connk = cx_Oracle.connect(CONN_STR)

    def query(self, query, params=None):
        cursor = self.conn.cursor()
        result = cursor.execute(query, params).fetchall()
        cursor.close()
        return result

    def query_otro(self, query, params):
        cursor = self.conn.cursor()
        result = cursor.execute(query, params)
        cursor.close()
        self.conn.commit()
        return result

    def query_otro2(self, query, params):
        cursor = self.connk.cursor()
        result = cursor.execute(query, params)
        cursor.close()
        self.connk.commit()
        return result

