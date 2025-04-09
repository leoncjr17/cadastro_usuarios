menu = """
=== MENU ===
1 - Cadastrar usuário
2 - Listar usuários
3 - Buscar usuário
4 - Sair
"""

usuarios = []  # Lista para armazenar os usuários

opcao = 0

while opcao != 4:
    print(menu)
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if opcao == 1:
        # Cadastro de usuário
        nome = input("Digite o seu nome: ").strip()
        if not nome.istitle():
            print("Ausência de inicial maiúscula no nome.")
        idade = input("Digite a sua idade: ")
        email = input("Digite o seu e-mail: ")

        # Adiciona o usuário a lista
        usuario = {
            "nome": nome,
            "idade": idade,
            "email": email
        }

        usuarios.append(usuario)
        print("Usuário cadastrado.")

    elif opcao == 2:
        #Verifica se a lista está vazia antes de listar os usuários
        if not usuarios:
            print("Sem usuários cadastrados.")
        else:
            print("\nUsuários cadastrados:")
            for i, usuario in enumerate(usuarios, start=1):
                print(f"\nUsuário {i}:")
                print(f"  Nome: {usuario['nome']}")
                print(f"  Idade: {usuario['idade']}")
                print(f"  Email: {usuario['email']}")

    elif opcao == 3:
        # Verifica especificamente por um usuário ao procurar pelo nome
        nome_busca = input("Digite o nome do usuário que deseja buscar: ").strip().capitalize()

        # Percorre a lista em busca de um nome idêntico, caso encontre, retorna os dados do usuário
        for usuario in usuarios:
            if usuario["nome"] == nome_busca:
                print(f"Nome: {usuario['nome']}")
                print(f"Idade: {usuario['idade']}")
                print(f"Email: {usuario['email']}")
                break
        else:
            print("Usuário não encontrado.")
            
    else:
        print("Opção inválida. Tente novamente.")
