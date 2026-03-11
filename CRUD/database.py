 # conexão com banco de dados
import sqlite3 as sql

class transactionObject():
    database = "clientes.db"
    conn = None
    cur = None

    connected = False

    def connect(self):
        transactionObject.conn = sql.connect(transactionObject.database)
        transactionObject.cur = transactionObject.conn.cursor()
        transactionObject.connected = True

    def disconnect(self):
        transactionObject.conn.close()
        transactionObject.connected = False

    def execute(self, sql, parms = None):
        if transactionObject.connected:
            if parms == None:
                transactionObject.cur.execute(sql)
            else:
                transactionObject.cur.execute(sql, parms)
            return True
        else:
            return False
    
    def fetchall(self):
        return transactionObject.cur.fetchall()
    
    def persist(self):
        if transactionObject.connected:
            transactionObject.conn.commit()
            return True
        else:
            return False
        
    def initDB(self):
        trans = transactionObject()
        trans.connect()

        trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
        trans.persist()
        trans.disconnect()
    
    def insert(self, nome, sobrenome, email, cpf):
        trans = transactionObject()
        trans.connect()
        trans.execute("INSERT INTO clientes VALUES(NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
        trans.persist()
        trans.disconnect()

    def view(self):
        trans = transactionObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes")
        rows = trans.fetchall()
        trans.disconnect()
        return rows

    def search(self,nome="", sobrenome="", email="", cpf=""):
        trans = transactionObject()
        trans.connect()
        trans.execute("SELECT * FROM clientes WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome, sobrenome, email,cpf))
        rows = trans.fetchall()
        trans.disconnect()
        return rows

    def delete(self, id):
        trans = transactionObject()
        trans.connect()
        trans.execute("DELETE FROM clientes WHERE id=?", (id,))
        trans.persist()
        trans.disconnect()

    def update(self, id, nome, sobrenome, email, cpf):
        trans = transactionObject()
        trans.connect()

        trans.execute("UPDATE clientes SET nome =?, sobrenome =?, email =?, cpf =? WHERE id = ?", (nome, sobrenome, email, cpf, id))
        trans.persist()
        trans.disconnect()

db = transactionObject()
db.initDB()