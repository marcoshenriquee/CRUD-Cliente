#Programa CRUD (Gerenciador de clientes)
#Adicionar cliente {Campos: nome, idade, email, telefone e cidade}
import re
import smtplib
import json
import os
import main

#Carrega dados Json já criados e cria caso não tenha
def carregar_dados():
    if os.path.exists("clientes.json"):
        with open("clientes.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    else:
        return[]


#Salva os dados no arquivo Json
def salvar_dados(dados):
    with open("clientes.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


#Cadastra os clientes
def cadastrar_cliente(clientes):
    cliente = {}
    
    print("\n========== ➕ CADASTRO DE CLIENTES ==========")
    while True:
        nome = input("Nome: ").strip().capitalize()
        if not nome:
            print("Nome é obrigatório!\n")
            continue
        cliente['nome'] = nome
        break
        
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("Idade não pode ser menor que zero.\n")
                continue
            cliente['idade'] = idade
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.\n")
            
    while True:
        email = input("E-mail: ").strip().lower()
        if not validar_email(email):
            print("Email inválido!\n")
            continue
        cliente['email'] = email
        break
        
    while True:
        telefone = input("Telefone: ").strip()
        telefone_formatado = validar_telefone(telefone)
        if telefone_formatado:
            cliente['telefone'] = telefone_formatado
            break
        print("número inválido. Deve conter 11 dígitos.")
        
    while True:
        cidade = input("Cidade: ").strip().capitalize()
        if not cidade:
            print("A cidade é obrigatória!\n")
            continue
        cliente['cidade'] = cidade
        break
        
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")


#Listar todos os clientes
def listar_clientes(lista):
    print("\n===== 📓 LISTA DE CLIENTES =====")
    if not lista:
        print("Nenhum cliente cadastrado!")
    for i, cliente in enumerate(lista, start=1):
        print(f"\n----------- CLIENTE {i} -----------")
        for chave, valor in cliente.items():
            print(f"{chave.capitalize()}: {valor}")


#Limpar a lista de clientes
def limpar_lista_clientes(lista):
    escolha = input("Tem certeza que deseja apagar todos os cadastros de clientes? (s/n): ").strip().lower()
    if escolha == "s":
        lista.clear()
        print("Todos os clientes foram excluídos com sucesso!")


#Validar e formatar número de telefone
def validar_telefone(telefone):
    # Remove tudo que não for número
    numeros = re.sub(r'\D', '', telefone)

    if len(numeros) == 11:
        ddd = numeros[:2]
        numero = numeros[2:7] + '-' + numeros[7:]
        return None


#Validar email
def validar_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None


#Pesquisar cliente pelo nome
def buscar_cliente(clientes):
    print("\n========== 🔎 BUSCAR CLIENTE ==========")
    
    while True:
        nome = input("\nDigite o nome ou parte do nome: ").strip()
        if not nome:
            print("Digite um nome!\n")
            continue
        
        resultados = []
        
        for cliente in clientes:
            if nome.lower() in cliente['nome'].lower():
                resultados.append(cliente)
        
        if resultados:
            
            print("\n============ RESULTADO(S) ============")
            for i, cliente in enumerate(resultados, 1):
                print(f"[{i}] {cliente['nome'].capitalize()}")
            print("-----------------------------------")
                
            if 1 == len(resultados):
                for chave, valor in cliente.items():
                    print(f"{chave.capitalize()}: {valor}")
                break
                    
            while True:
                try:
                    escolha = int(input("Selecione o cliente: "))
                    if 1 <= escolha <= len(resultados):
                        for chave, valor in resultados[escolha - 1].items():
                            print(f"{chave.capitalize()}: {valor}")
                        break
                    else:
                        print("Opção inválida!\n")
                        continue
                        
                except ValueError:
                    print("Opção inválida. Digite um número inteiro.")
                    
            sair = input("\nDeseja buscar outro cliente? (s/n): ").strip().lower()
            if sair == "n":
                break
            
        else:
            print("❌ Cliente não encontrado!")
            continue


#Editar clientes
def editar_cliente(clientes):
    print("\n========== 🔎 BUSCAR CLIENTE PARA EDITAR ==========")
    
    while True:
        nome = input("\nDigite o nome ou parte do nome: ").strip()
        if not nome:
            print("Digite um nome!\n")
            continue
        
        resultados = []
        
        for cliente in clientes:
            if nome.lower() in cliente['nome'].lower():
                resultados.append(cliente)
        
        if resultados:
            
            print("\n============ RESULTADO(S) ============")
            for i, cliente in enumerate(resultados, 1):
                print(f"[{i}] {cliente['nome'].capitalize()}")
            print("-----------------------------------")
                
            if 1 == len(resultados):
                for chave, valor in cliente.items():
                    print(f"{chave.capitalize()}: {valor}")
                break
                    
            while True:
                try:
                    escolha = int(input("Selecione o cliente: "))
                    if 1 <= escolha <= len(resultados):
                        for chave, valor in resultados[escolha - 1].items():
                            print(f"{chave.capitalize()}: {valor}")
                        break
                    else:
                        print("Opção inválida!\n")
                        continue
                        
                except ValueError:
                    print("Opção inválida. Digite um número inteiro.")
            break
                    
        else:
            print("❌ Cliente não encontrado!")
            continue
    
    
    print("""
[1] 👤 Nome
[2] 🔢 Idade
[3] 📩 E-mail
[4] 📞 Telefone
[5] 🏙️ Cidade""")

    while True:
        try:
            editar = int(input("\nO que deseja editar? 0 para sair: "))
            if editar == 0:
                print("Saindo... ")
                break
            
            elif editar == 1:
                novo_nome = input("Nome: ").strip()
                cliente['nome'] = novo_nome
                print("Nome editado com sucesso!")
                
            elif editar == 2:
                nova_idade = int(input("Idade: "))
                cliente['idade'] = nova_idade
                print("Idade editada com sucesso!")
                
            elif editar == 3:
                novo_email = input("E-mail: ").strip.capitalize()
                cliente['email'] = novo_email
                print("E-mail editado com sucesso!")
                
            elif editar == 4:
                novo_telefone = input("Telefone: ").strip().capitalize()
                cliente['telefone'] = novo_telefone
                print("Telefone editado com sucesso!")
                
            elif editar == 5:
                novo_cidade = input("Cidade: ").strip.capitalize()
                cliente['cidade'] = novo_cidade
                print("Cidade editada com sucesso!")
                
            else:
                print("Opção inválida.")
                
        except ValueError:
            print("Opção inválida. Digite um número inteiro!")


#Excluir cliente
def excluir_cliente(clientes):
    print("\n========== 🔎 BUSCAR CLIENTE PARA EXCLUIR ==========")
    
    while True:
        nome = input("\nDigite o nome ou parte do nome: ").strip()
        if not nome:
            print("Digite um nome!\n")
            continue
        
        resultados = [cliente for cliente in clientes if nome.lower() in cliente['nome'].lower()]
        
        if resultados:
            print("\n============ RESULTADO(S) ============")
            for i, cliente in enumerate(resultados, 1):
                print(f"[{i}] {cliente['nome'].capitalize()}")
            print("-----------------------------------")
                
            if len(resultados) == 1:
                cliente = resultados[0]
                for chave, valor in cliente.items():
                    print(f"{chave.capitalize()}: {valor}")
                excluir = input("\nO cliente será excluído permanentemente, tem certeza? (s/n): ").strip().lower()
                if excluir == "s":
                    clientes.remove(cliente)  # 👉 Remove da lista original
                    print("✅ Cliente excluído com sucesso!")
                break
            
            while True:
                try:
                    escolha = int(input("Selecione o cliente: "))
                    if 1 <= escolha <= len(resultados):
                        cliente = resultados[escolha - 1]
                        for chave, valor in cliente.items():
                            print(f"{chave.capitalize()}: {valor}")
                            
                        excluir = input("\nO cliente será excluído permanentemente, tem certeza? (s/n): ").strip().lower()
                        if excluir == "s":
                            clientes.remove(cliente)  # 👉 Remove da lista original
                            print("✅ Cliente excluído com sucesso!")
                        break
                    else:
                        print("Opção inválida!\n")
                        continue
                        
                except ValueError:
                    print("Opção inválida. Digite um número inteiro.")
            break
                    
        else:
            print("❌ Cliente não encontrado!")
            continue

        
    
    


#Editar cliente - Poder editar qualquer campo de um cliente específico.
#Remover cliente

