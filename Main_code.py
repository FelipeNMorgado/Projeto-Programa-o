import os

biblioteca = {}
lista_cat = []
soma = 0
cont_mudar = 0
lista_carrinho = []
preco_total = 0
preco_totalc = 0

def salvar_biblioteca():
    with open("biblioteca.txt", "w", encoding="utf8") as file:
        for cat, livros in biblioteca.items():
            file.write(f"Categoria: {cat}\n")
            for livro in livros:
                file.write(f"Nome: {livro['nome']}\n")
                file.write(f"Autor: {livro['autor']}\n")
                file.write(f"Preço: {livro['preço']}\n")
            file.write("\n")


def carregar_biblioteca():
    global biblioteca
    biblioteca = {}

    with open("biblioteca.txt", "r", encoding="utf8") as file:
        cat = None
        livro = None

        for line in file:
            line = line.strip()

            if line.startswith("Categoria: "):
                cat = line.split(": ")[1]
                lista_cat.append(cat)
                biblioteca[cat] = []
            elif line.startswith("Nome: "):
                livro = {"nome": line.split(": ")[1]}
            elif line.startswith("Autor: "):
                livro["autor"] = line.split(": ")[1]
            elif line.startswith("Preço: "):
                livro["preço"] = int(line.split(": ")[1])
                if cat and livro["nome"] and livro["autor"] and "preço" in livro:
                    biblioteca[cat].append(livro)
                    livro = None


def salvar_carrinho():
    with open("carrinho.txt", "w", encoding="utf8") as file:
        for livro in lista_carrinho:
            file.write(f"Nome: {livro['nome']}\n")
            file.write(f"Categoria: {livro['categoria']}\n")
            file.write(f"Autor: {livro['autor']}\n")
            file.write(f"Preço: {livro['preço']}\n")
        file.write("\n")

def carregar_carrinho():
    global lista_carrinho
    lista_carrinho = []

    with open("carrinho.txt", "r", encoding="utf8") as file:
        nome = None
        categoria = None
        autor = None
        preco = None

        for line in file:
            line = line.strip()

            if line.startswith("Nome: "):
                nome = line.split(": ")[1]
            elif line.startswith("Categoria: "):
                categoria = line.split(": ")[1]
            elif line.startswith("Autor: "):
                autor = line.split(": ")[1]
            elif line.startswith("Preço: "):
                preco = int(line.split(": ")[1])
                lista_carrinho.append({"nome": nome, "categoria": categoria, "autor": autor, "preço": preco})


carregar_carrinho()
carregar_biblioteca()


def adicionar():
    os.system("cls")

    cat_add = input("Categoria do livro: ")
    livro_name = input("Nome do livro: ")
    
    for cat_add in biblioteca:
        for livro in biblioteca[cat_add]:
            if livro_name == livro['nome']:
                print("Esse livro já existe nessa categoria")


    livro_autor = input("Autor do livro: ")
        
    try:
        livro_preco = int(input("Preço do livro: "))
    except ValueError:
        print("Por favor, insira um valor numérico para o preço.")
        return

    livro = {"nome": livro_name, "autor": livro_autor, "preço": livro_preco}

    print("\nLivro adicionado com sucesso!")

    if cat_add in biblioteca:
        biblioteca[cat_add].append(livro)
    else:
        biblioteca[cat_add] = [livro]

    if cat_add not in lista_cat:
        lista_cat.append(cat_add)

    salvar_biblioteca()

def excluir():
    os.system("cls")
    global preco_total
    cont_remove = 0

    print("Categorias disponíveis: \n")

    for x in lista_cat:
        print('-', x)

    print()
    cat_remove = input("Digite a categoria do livro que você deseja remover: ")

    if cat_remove in biblioteca:
        print(f"\nCategoria: {cat_remove}")
        print("\nLivros:\n")
        for livro in biblioteca[cat_remove]:
            print(f"Nome: {livro['nome']}")

        livro_remove = input("\nDigite o livro que você deseja remover: ")
        for livro in biblioteca[cat_remove]:
            cont_remove += 1
            if livro['nome'] == livro_remove:
                biblioteca[cat_remove].remove(livro)
                print(f"\nLivro removido com sucesso!")
                preco_total -= livro["preço"]
                cont_remove -= 100000

        if cont_remove > 0:
            print(f"\nO livro {livro_remove} não foi encontrado!")
    else:
        print(f"\nA categoria {cat_remove} não foi encontrada!")

    salvar_biblioteca()

def atualizar():
    os.system("cls")
    print("Categorias disponíveis: \n")

    cont_mudar = 0

    for x in lista_cat:
        print('-', x)

    print()

    cat_atualizada = input("Digite a categoria do livro que você deseja atualizar: ")

    if cat_atualizada in biblioteca:
        print(f"\nCategoria: {cat_atualizada}")
        print("\nLivros:\n")

        for livro in biblioteca[cat_atualizada]:
            print(f"Nome: {livro['nome']}")

        livro_novo = input("\nDigite o livro que você deseja atualizar: ")

        for livro in biblioteca[cat_atualizada]:
            cont_mudar += 1
            if livro['nome'] == livro_novo:
                opcao_atualizar = input("\nDigite o que você deseja mudar:\n- Nome[N];\n- Autor[A];\n- Preço[P];\nSua opção: ")
                if opcao_atualizar == 'N':
                    livro['nome'] = input("\nNovo nome do livro: ")
                elif opcao_atualizar == 'A':
                    livro['autor'] = input("\nNovo autor do livro:")
                elif opcao_atualizar == 'P':
                    livro['preço'] = int(input("\nNovo preço do livro: "))
                print(f"\nLivro atualizado com sucesso!\n")
                cont_mudar -= 10000000

                if cont_mudar > 0:
                    print("\nLivro não encontrado!")

    salvar_biblioteca()

def visualizar():
    os.system("cls")
    print("Categorias disponíveis: \n")

    for x in lista_cat:
        print('-', x)

    print()
    cat_visualizar = input("Digite qual a categoria do livro que você deseja visualizar: ")

    if cat_visualizar in biblioteca:
        print(f"\nCategoria: {cat_visualizar}")

        for livro in biblioteca[cat_visualizar]:
            print(f"Nome: {livro['nome']}")

        livro_escolhido = input("\nDigite o nome do livro para uma visão mais detalhada (ou '0' para voltar): ")

        if livro_escolhido != '0':
            for livro in biblioteca[cat_visualizar]:
                if livro['nome'] == livro_escolhido:
                    print(f"\nDetalhes do Livro:\nNome: {livro['nome']}\nAutor: {livro['autor']}\nPreço: {livro['preço']}")
                    break
            else:
                print(f"O livro {livro_escolhido} não foi encontrado na categoria {cat_visualizar}.")
    else:
        print(f"A categoria {cat_visualizar} não foi encontrada.")


def carrinho_add():
    os.system("cls")
    global lista_carrinho, preco_totalc

    livro_name = input("Nome do livro: ")
    livro_categoria = input("Categoria do livro: ")
    livro_autor = input("Autor do livro: ")
    
    try:
        livro_preco = int(input("Preço do livro: "))
    except ValueError:
        print("Por favor, insira um valor numérico para o preço.")
        return

    livro = {"nome": livro_name, "categoria": livro_categoria, "autor": livro_autor, "preço": livro_preco}

    lista_carrinho.append(livro)

    print("\nLivro adicionado ao carrinho com sucesso!")

    salvar_carrinho()

def carrinho_visualizar():
    global lista_carrinho
    print("\nLivros no carrinho:")
    for livro in lista_carrinho:
        print(f"\nNome: {livro['nome']}\nCategoria: {livro['categoria']}\nAutor: {livro['autor']}\nPreço: {livro['preço']}")
        print("--" * 40 + '\n')

    salvar_carrinho()

def carrinho_excluir():
    os.system("cls")
    global preco_totalc, lista_carrinho

    print("Livros no carrinho:\n")
    for livro in lista_carrinho:
        print(f"Nome: {livro['nome']}")

    livro_excluir = input("\nQual livro você deseja excluir? ")

    for livro in lista_carrinho:
        if livro['nome'] == livro_excluir:
            preco_totalc -= livro['preço']
            lista_carrinho.remove(livro)
            print(f"Seu livro {livro_excluir} foi excluído com sucesso!")
            break
    else:
        print("Livro não encontrado")

    salvar_carrinho()

while True:
    while True:
        try:
            print("--" * 40)
            mod = int(input("Pressione o número correspondente à alteração que deseja:\n\n[1]-Adicionar\n[2]-Excluir\n[3]-Atualizar\n[4]-Visualizar\n[5]-Dinheiro Gasto\n[6]-Carrinho\n[7]-Parar\n\nDigite aqui a sua opção: "))
            break
        except ValueError:
            print("Por favor digite um valor entre os estabelecidos anteriormente.")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    if mod == 1:
        adicionar()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif mod == 2:
        excluir()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif mod == 3:
        atualizar()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif mod == 4:
        visualizar()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif mod == 5:
        preco_total = sum(livro['preço'] for categoria in biblioteca for livro in biblioteca[categoria])
        print("\nDinheiro total gasto em todos os livros: R$", preco_total)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif mod == 6:
        os.system("cls")
        print("[1]-Adicionar livro ao carrinho")
        print("[2]-Visualizar livros no carrinho")
        print("[3]-Excluir livros do carrinho")
        preco_totalc = sum(livro['preço'] for livro in lista_carrinho)
        print(f"\nPreço total do livros no carrinho: R$ {preco_totalc}\n")
        escolha_carrinho = int(input("Sua escolha: "))
        if escolha_carrinho == 1:
            carrinho_add()
        elif escolha_carrinho == 2:
            carrinho_visualizar()
        elif escolha_carrinho == 3:
            carrinho_excluir()
    
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif mod == 7:
        salvar_biblioteca()
        salvar_carrinho()
        print("Dados salvos nos arquivos 'biblioteca.txt' e 'carrinho.txt'.")
        print("Saindo do programa. Obrigado!\n")
        print("-------- Volte sempre! --------\n")
        break

    else:
        print("Por favor digite um valor entre os estabelecidos anteriormente.")