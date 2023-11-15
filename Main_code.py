import os

biblioteca = {}
preco_total = 0
lista_cat = []
cont = 0

while True:
    print("--" * 40)
    mod = int(input("Pressione o número correspondente à alteração que deseja:\n\n[1]-Adicionar\n[2]-Excluir\n[3]-Atualizar\n[4]-Visualizar\n[5]-Dinheiro Gasto\n[6]-Parar\n\nDigite aqui a sua opção: "))
    
    if mod == 1:
        cat_add = input("Categoria do livro: ")
        livro_name = input("Nome do livro: ")
        livro_autor = input("Autor do livro: ")
        livro_preco = int(input("Preço do livro: "))
        livro = {"nome": livro_name, "autor": livro_autor, "preço": livro_preco}
        
        
        if cat_add in biblioteca:
            biblioteca[cat_add].append(livro)
        else:
            biblioteca[cat_add] = [livro]
        
        if cat_add in lista_cat:
            continue
        else:
            lista_cat.append(cat_add)
        
        cont += 1

        print("Livro adicionado com sucesso!")
        preco_total += livro_preco
    
    elif mod == 2:
        os.system("cls")
        option_2 = input("Digite o nome do livro que você deseja excluir: ")
        # Adicione aqui a lógica para excluir o livro
        
    elif mod == 3:
        print("Opção de atualizar. Adicione a lógica conforme necessário.")
        # Adicione aqui a lógica para alterar as informações do livro
    
    elif mod == 4:
        os.system("cls")
        print("Categorias disponiveis: \n")
        
        for x in range(cont):
            print('-',lista_cat[x])
            
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
    
    elif mod == 5:
        print("\nDinheiro total gasto: R$", preco_total)
    
    elif mod == 6:
        print("Saindo do programa. Obrigado!")
        break