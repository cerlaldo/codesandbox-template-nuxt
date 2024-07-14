# Crie um dicionário para armazenar os contatos
agenda_contatos = {}

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    endereco = input("Digite o endereço do contato: ")
    email = input("Digite o endereço de e-mail: ")
    contato = {"Nome": nome, "Telefone": telefone, "Endereço": endereco, "E-mail": email}
    agenda_contatos[nome] = contato


def listar_contatos():
    for nome, contato in agenda_contatos.items():
        print(f"{nome}: {contato['Telefone']} ({contato['E-mail']})")


# Exemplo de uso
adicionar_contato()
listar_contatos()