#Programa CRUD (Gerenciador de clientes)
#Adicionar cliente {Campos: nome, idade, email, telefone e cidade}
import functions

clientes = functions.carregar_dados()

def main():
    while True:
        print("""
===== 👤 CLIENTES =====\n
[1] ➕ Cadastrar
[2] 📓 listar
[3] 🔎 Pesquisar
[4] 🔄 Editar
[5] ➖ Excluir
[6] 🆑 Limpar
[0] 👋 Sair
        """)
        
        escolha = input("O que quer fazer? ")
            
        if escolha == "0":
            print("Saindo...  👋")
            break
        
        elif escolha == "1":
            functions.cadastrar_cliente(clientes)
            functions.salvar_dados(clientes)
            continue
        
        elif escolha == "2":
            functions.listar_clientes(clientes)
            continue
        
        elif escolha == "3":
            functions.buscar_cliente(clientes)
            
        elif escolha == "4":
            functions.editar_cliente(clientes)
            functions.salvar_dados(clientes)
        
        elif escolha == "5":
            functions.excluir_cliente(clientes)
            functions.salvar_dados(clientes)
        
        elif escolha == "6":
            functions.limpar_lista_clientes(clientes)
            functions.salvar_dados(clientes)
            continue
        
        else:
            print("Opção inválida!\n")
            continue
        break


if __name__ == "__main__":
    main()