import pymysql

class userDB():
    def __init__(self):
        pass
    
    def insert(self, name: str, id: str, password: str, email: str):
        con = pymysql.connect(host='localhost', user='root', password='qwerasdf12', db='bss', charset='utf8')
        cur = con.cursor()
        idUniqueQuery = "select count(*) from user where id='" + id + "';"
        print('idUniqueQuery : ', idUniqueQuery) # debug
        cur.execute(idUniqueQuery)
        idUniqueQueryResult = cur.fetchall()[0][0]
        print('idUniqueQueryResult : ', idUniqueQueryResult) # debug
        if not idUniqueQueryResult:
            signUpQuery = "insert into user values ('" + name + "', '" + id + "', '" + password + "', '" + email + "');"
            print('signUpQuery : ', signUpQuery) # debug
            cur.execute(signUpQuery)
            signUpQueryResult = cur.fetchall()
            con.commit()
        cur.close()
        con.close()
    
    def getPassword(self, id: str):
        con = pymysql.connect(host='localhost', user='root', password='qwerasdf12', db='bss', charset='utf8')
        cur = con.cursor()
        getPasswordQuery = "select password from user where id='" + id + "';"
        print('getPasswordQuery : ', getPasswordQuery)
        cur.execute(getPasswordQuery)
        getPasswordResult = cur.fetchall()[0][0]
        print('getPasswordResult : ', getPasswordResult)
        return getPasswordResult