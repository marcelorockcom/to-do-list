import getpass
import db
import time

print("======================================")
print("||            TO-DO-LIST            ||")
print("======================================")

nome = input("\nDigite nome usuário: ")
senha = getpass.getpass("Digite a senha: ")

def menu(con):
    menuOp = [
        '\n---------------------------------',
        '1 - Consultar',
        '2 - Cadastrar',
        '3 - Editar',
        '4 - Excluir',
        '0 - Sair']
    db.chkTable(con)
    db.chkIdSeq(con)
    for i in menuOp:
        print(i)
    esc = input("Digite o numero da opção deseja: ")
    if(esc == "1" or esc == "2" or esc == "3" or esc == "4" or esc == "0"):
        match esc:
            case "1":
                db.consultar(con)
                menu(con)
            case "2":
                nomeT = input("\nDigite o nome da tarefa: ")
                descT = input("Digite a descrição da tarefa: ")
                if(con != "" and nomeT != "" and descT != ""):
                    db.cadastrar(con, nomeT, descT)
                    menu(con)
                else:
                    print("****** Nome ou descrição não pode ser vazio ******\n")
                    menu(con)
            case "3":
                idT = input("\nDigite o ID da tarefa: ")
                if(db.checkId(con, idT) != "Erro"):
                    nomeT = input("Digite o nome da tarefa: ")
                    descT = input("Digite a descrição da tarefa: ")
                    concT = input("Tarefa concluida?(S/N) ")
                    if(con != "" and idT != "" and nomeT != "" and descT != ""):
                        if(concT == "S" or concT == "N"):
                            db.editar(con, idT,nomeT, descT, concT)
                            menu(con)                
                        else:
                            print("****** Por favor preencha apens S ou N ******")
                            menu(con)
                    else:
                        print("****** Todos os compos devem ser preenchidos******\n")
                        menu(con)
                else:
                    print("****** ID invalido ****** ")
                    menu(con)
            case "4":
                idT = input("\nDigite o ID da tarefa: ")
                if(db.checkId(con, idT) != "Erro"):
                    db.excluir(con, idT)
                    menu(con) 
                else:
                    print("****** ID invalido ****** ")
                    menu(con)
            case "0":
                print("\n****** ATÉ MAIS! ******\n")
                con.close()
                time.sleep(2)
    else:
        print("****** Opção inválida ******")
        menu(con)
                   
def conectar(nome, senha):
    if(nome != "" and senha != ""): 
        con = db.conDB(nome, senha)
        if(con[1] == "conectado"):
            menu(con[0])
        else:
            print("****** Erro ao conectar, verifique usuário e senha ******\n")
            nome = input("Digite nome usuário: ")
            senha = getpass.getpass("Digite a senha: ")
            conectar(nome, senha)
    else:
        print("****** Nome ou senha não pode ser vazia ******\n")
        nome = input("Digite nome usuário: ")
        senha = getpass.getpass("Digite a senha: ")
        conectar(nome, senha)
    
conectar(nome, senha)




