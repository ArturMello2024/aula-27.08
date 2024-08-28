clientes = []

def adicionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    cliente.append(clientes)
    print(f"Cliente {nome} cadastrado!")

def exibir_clientes():
    for cliente in clientes:
        print(f"Nome {cliente[0]}, email {cliente[1]}, telefone {cliente[2]}, endereço {cliente[3]}.")

def remover_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            clientes.remove(cliente)
            print(f"O cliente com {email}, foi removido! ")
            return 
    print(f"Cliente nao encontrado")

def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f"Nome {cliente[0]}, email {cliente[1]}, telefone {cliente[2]}, endereço {cliente[3]}.")
            return 
def testar():
        adicionar_cliente("Artur Mello", "arturmello123@univassouras", "229999999", "Av saquarema")
        exibir_clientes()
        remover_cliente("arturmello123@univassouras")
        

def menu():
    while True:
        print("MENU")
        print("1 - ADD")
        print("2 - EXIB")
        print("3 - REMOVER")
        print("4 - BUSCAR")
        print("5 - SAIR")
        print("6 - TESTAR")

        opcao= input("Escolha uma opção")

        if opcao == "1":
            nome = input(" Entre com o Nome:")
            email = input(" Entre com o Email:")
            telefone = input("Entre com o Telefone:")
            endereco = input("Entre com o Endereço:")
            adicionar_cliente(nome, email, telefone, endereco)
        elif opcao == "2":
            print[clientes]
        elif opcao == "3":
           remover_cliente(email)
           email = input(" Entre com o email a ser removido:")
        elif opcao == "4":
           buscar_cliente(email)
        elif opcao == "s":
            print("saindo do programa")
            break
        elif opcao == "6":
            testar()
            break
        else:
            print("opcao inválida")
menu()