 # conexão com banco de dados
import sqlite3 as sql

class transactionObjct():
    database = "clientes.db"
    conn = None
    cur = None

    connected = False

    def connect(self):
        transactionObjct.conn =sql.connect(transactionObjct.database)
        transactionObjct.cur = transactionObjct.conn.cursor()
        transactionObjct.connected = True

    def disconnect(self):
        transactionObjct.conn.close()
        transactionObjct.connected = False

    def execute(self, sql, parms = None):
        if transactionObjct.connected:
            if parms == None:
                transactionObjct.cur.execute(sql)
            else:
                transactionObjct.cur.execute(sql, parms)
            return True
        else:
            return False
    
    def fetchall(self):
        return transactionObjct.cur.fetchall()
    
    def persist(self):
        if transactionObjct.connected:
            transactionObjct.conn.commit()
            return True
        else:
            return False
        
    def initDB(self):
        trans = transactionObjct()
        trans.connect()

        trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        trans.persist()
        trans.disconnect()
    
    def insert(nome, sobrenome, email, cpf):
        trans= transactionObjct()
        trans.connect()
        trans.execute("INSERT INTO clientes VALUES(NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
        trans.persist()
        trans.disconnect()

    def view():
        trans = transactionObjct()
        trans.connect()
        trans.execute("SELECT * FROM clientes")
        rows = trans.fetchall()
        trans.disconnect()
        return rows

    def search(nome="", sobrenome="", email="", cpf=""):
        trans = transactionObjct()
        trans.connect()
        trans.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome, sobrenome, email,cpf))
        rows = trans.fetchall()
        trans.disconnect()
        return rows

    def delete(id):
        trans=transactionObjct
        trans.connect()
        trans.execute("DELETE FROM clientes WHERE id=?", (id,))
        trans.persiste()
        trans.disconnect()

    def update(id, nome, sobrenome, email, cpf):
        trans=transactionObjct()
        trans.connect()

        trans.execute("UPDATE clientes SET nome =?, sobrenome =?, email =?, cpf =?, WHERE id = ?", (nome, sobrenome, email, cpf, id))
        trans.persist()
        trans.disconnect()

    initDB()
    
