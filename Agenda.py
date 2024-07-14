
def menu () :
    voltaTudo = 's'
    while voltaTudo=='s' :

        opcao= input('''     =============================
            AGENDA DA SORTE
                            
        [1]CADASTRAR CONTATO         
        [2]LISTAR CONTATO          
        [3]DELETAR CONTATO          
        [4]BUSCAR CONTATO PELO NOME
        [5]SAIR DA AGENDA        
        ==============================            
        ESCOLHA UMA OPÇÃO: ''')
        if opcao =="1":
            cadastrarContato()
        elif opcao =="2":
            listarContato()
        elif opcao =="3":
            deletarContato()
        elif opcao =="4":
            buscarContato()
        else:
            sair()
        voltaTudo=input(f'Deseja voltar ao menu prinipal ? (s/n) ').lower()
        

def cadastrarContato():
    idContato = input("ESCOLHA UM ID PARA O CONTATO: ")
    nome = input("ESCREVA O NOME DO CONTATO: ")
    tel = input("ESCREVA O TELEFONE DO CONTATO: ")
    email = input("ESCREVA O EMAIL DO CONTATO: ")
    try:
        agenda = open("agenda.txt","a")
        dados = f'{idContato};{nome};{tel};{email} \n'
        agenda.write(dados)
        agenda.close()
        print("CONTATO GRAVADO COM SUCESSO!!!!!")
    except:
        print("ERRO NA GRAVAÇÃO DE CONTATO")




def listarContato():
    agenda = open("agenda.txt","r")
    for contato in agenda:
        print(contato)
    agenda.close

def deletarContato():
    nomeDeletado = input(f'Digite o nome que quer deletar: ')
    agenda = open("agenda.txt","r")
    aux = []
    aux2= []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
       if nomeDeletado not in aux[i]:
           aux2.append(aux[i])
    agenda = open("agenda.txt","w")
    for i in aux2:
      agenda.write(i)
      print(f'Contato deletado com sucesso!!!')       


def buscarContato():
    nome = input(f'Digitar nome para busca: ')
    agenda = open("agenda.txt","r")
    for contato in agenda:
        if nome in contato.split(";") [1]:
            print(contato)
    agenda.close()

def sair():
    print(f'Até breve!')
    exit()


def main():
    menu()

main()




