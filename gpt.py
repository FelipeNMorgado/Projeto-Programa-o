import os

biblioteca = {}
lista_cat = []
preco_total = 0

def adicionar_livro():
    global preco_total
    os.system("cls")
    
    cat_add = input("Categoria do livro: ")
    livro_name = input("Nome do livro: ")
    livro_autor = input("Autor do livro: ")
    livro_preco = int(input("Preço do livro: "))
    livro = {"nome": livro_name, "autor": livro_autor, "preço": livro_preco}
    
    print("\nLivro adicionado com sucesso!")

    if cat_add in biblioteca:
        biblioteca[cat_add].append(livro)
    else:
        biblioteca[cat_add] = [livro]

    if cat_add not in lista_cat:
        lista_cat.append(cat_add)
    preco_total += livro_preco

def excluir_livro():
    global preco_total
    os.system("cls")

    print("Categorias disponíveis: \n")
    for cat in lista_cat:
        print('-', cat)

    print()
    cat_remove = input("Digite a categoria do livro que você deseja remover: ")

    if cat_remove in biblioteca:
        print(f"\nCategoria: {cat_remove}")
        print("\nLivros:\n")
        for livro in biblioteca[cat_remove]:
            print(f"Nome: {livro['nome']}")

        livro_remove = input("\nDigite o livro que você deseja remover: ")
        for livro in biblioteca[cat_remove]:
            if livro['nome'] == livro_remove:
                biblioteca[cat_remove].remove(livro)
                print(f"\nLivro '{livro_remove}' removido com sucesso!")
                preco_total -= livro['preço']
                break
        else:
            print(f"\nO livro '{livro_remove}' não foi encontrado!")
    else:
        print(f"\nA categoria '{cat_remove}' não foi encontrada!")

def atualizar_livro():
    os.system("cls")
    print("Categorias disponíveis: \n")

    for cat in lista_cat:
        print('-', cat)

    print()
    
    cat_atualizada = input("Digite a categoria do livro que você deseja atualizar: ") 
    
    if cat_atualizada in biblioteca:
        print(f"\nCategoria: {cat_atualizada}")
        print("\nLivros:\n")
        
        for livro in biblioteca[cat_atualizada]:
            print(f"Nome: {livro['nome']}")

        livro_novo = input("\nDigite o nome do livro que você deseja atualizar: ")  

        for livro in biblioteca[cat_atualizada]:    
            if livro['nome'] == livro_novo:
                opcao_atualizar = input("\nDigite o que você deseja mudar:\n- Nome[N];\n- Autor[A];\n- Preço[P]\nSua opção: ")
                if opcao_atualizar == 'N':
                    livro['nome'] = input("\nNovo nome do livro: ")
                elif opcao_atualizar == 'A':
                    livro['autor'] = input("\nNovo autor do livro:")
                elif opcao_atualizar == 'P':
                    novo_preco = int(input("\nNovo preço do livro: "))
                    preco_total += novo_preco - livro['preço']
                    livro['preço'] = novo_preco
                print(f"\nLivro '{livro_novo}' atualizado com sucesso!\n")
                break
        else:
            print("\nLivro não encontrado!")
    else:
        print(f"\nA categoria '{cat_atualizada}' não foi encontrada!")

def visualizar_livro():
    os.system("cls")
    print("Categorias disponíveis: \n")
    
    for cat in lista_cat:
        print('-', cat)
    
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
                print(f"O livro '{livro_escolhido}' não foi encontrado na categoria '{cat_visualizar}'.")
    else:
        print(f"A categoria '{cat_visualizar}' não foi encontrada.")

def dinheiro_gasto():
    global preco_total
    preco_total = sum(livro['preço'] for categoria in biblioteca for livro in biblioteca[categoria])
    print("\nDinheiro total gasto em todos os livros: R$", preco_total)

def carrinho():
    # Implemente a lógica do carrinho aqui
    print("Função do carrinho ainda não implementada.")

while True:
    print("--" * 40)
    mod = int(input("Pressione o número correspondente à alteração que deseja:\n\n[1]-Adicionar\n[2]-Excluir\n[3]-Atualizar\n[4]-Visualizar\n[5]-Dinheiro Gasto\n[6]-Carrinho\n[7]-Parar\n\nDigite aqui a sua opção: "))
    os.system("cls")
    
    if mod == 1:
        adicionar_livro()
    elif mod == 2:
        excluir_livro()
    elif mod == 3:
        atualizar_livro()
    elif mod == 4:
        visualizar_livro()
    elif mod == 5:
        dinheiro_gasto()
    elif mod == 6:
        carrinho()
    elif mod == 7:
        print("Saindo do programa. Obrigado!\n")
        print("---------Volte sempre!---------\n")
        break
