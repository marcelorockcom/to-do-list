import cx_Oracle

def conDB(nome, senha):
    arg = [
            nome + "/",
            senha + "@",
            "localhost:1521/XEPDB1"
        ]
    try:
        return cx_Oracle.connect(arg[0] + arg[1] + arg[2]), "conectado"
    except Exception as e:
        return "nao conectado"

def chkTable(con):
    try:
        cr = con.cursor()
        cr.execute("select * from list")
        cr.close()
    except cx_Oracle.DatabaseError as e:
        if(e.args[0].code == 942):
            cr = con.cursor()
            cr.execute('''CREATE TABLE 
                list(id number(10), nome varchar2(50), descricao varchar2(255), concluido char(1))''')
            cr.close()

def chkIdSeq(con):
    try:
        cr = con.cursor()
        cr.execute("select idTarefa.currval from dual")
        cr.close()
    except cx_Oracle.DatabaseError as e:
        if(e.args[0].code == 2289):
            cr = con.cursor()
            cr.execute('CREATE SEQUENCE idTarefa maxvalue 999')
            cr.close()

def checkId(con, idT):
    try:
        cursor = con.cursor()
        chkId = cursor.execute(f'select id from list where id = {idT}')
        len(chkId.fetchone())
    except Exception as e:
        return "Erro"

def consultar(con):
    cursor = con.cursor()
    resultado = cursor.execute('SELECT * FROM list ORDER BY id')
    row = resultado.fetchall()
    if(len(row) > 0):
        for i in row:
            print("id:", i[0], "| Nome:", i[1], "| Descricao:", i[2], "| Concluido?", i[3])
        cursor.close()
    else:
        print("\nNão há taferas cadastradas\n")

def cadastrar(con, nomeT, descT):
    try:
        cursor = con.cursor()
        query = f"INSERT INTO list values(idTarefa.nextval, '{nomeT}', '{descT}', 'N')"
        cursor.execute(query)
        con.commit()
        cursor.close()
        print("Tarefa Cadastrado com sucesso")
    except Exception as e:
        print("Erro ao cadastrar tarefa ", e)

def editar(con, idT, nomeT, descT, concT):
    try:
        cursor = con.cursor()
        chkId = cursor.execute(f'select id from list where id = {idT}')
        len(chkId.fetchone())
        queryEd = f"UPDATE list set nome = '{nomeT}', descricao = '{descT}', concluido = '{concT}' where id = {idT}"
        edit = cursor.execute(queryEd)
        con.commit()
        cursor.close()
        print("Tarefa editada com sucesso")
    except Exception as e:
        print("Erro ao editar tarefa, verifique o ID")

def excluir(con, idT):
    try:
        cursor = con.cursor()
        chkId = cursor.execute(f'select id from list where id = {idT}')
        len(chkId.fetchone())
        query = f"DELETE from list where id = {idT}"
        cursor.execute(query)
        con.commit()
        print("Tarefa excluida com sucesso")
    except Exception as e:
        print("Erro ao excluir tarefa, verifique o ID")