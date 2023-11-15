import os
os.system("cls")

biblioteca = {}
lista_cat = []
cont = 0
cont_remove = 0
soma = 0
cont_mudar = 0

while True:
    print("--" * 40)
    mod = int(input("Pressione o número correspondente à alteração que deseja:\n\n[1]-Adicionar\n[2]-Excluir\n[3]-Atualizar\n[4]-Visualizar\n[5]-Dinheiro Gasto\n[6]-Carrinho\n[7]-Parar\n\nDigite aqui a sua opção: "))
    os.system("cls")
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    if mod == 1: 
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
        
        if cat_add in lista_cat:
            continue
        else:
            lista_cat.append(cat_add)
            cont += 1
            
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif mod == 2:
        os.system("cls")

        cont_remove = 0

        print("Categorias disponiveis: \n")

        for x in range(cont):
            print('-',lista_cat[x])

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
                    print(f"\nLivro '{livro_remove}' removido com sucesso!")
                    preco_total -= livro['preço']
                    cont_remove -= 100000
                    
            if cont_remove > 0:
                    print(f"\nO livro {livro_remove} não foi encontrado!")
        else:
            print(f"\nA categoria {cat_remove} não foi encontrada!")

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    elif mod == 3:
        os.system("cls")
        print("Categorias disponiveis: \n")

        cont_mudar = 0

        for x in range(cont):
            print('-',lista_cat[x])

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
                    opcao_atualizar = input("\nDigite o que você deseja mudar:\n- Nome[N];\n- Autor[A];\n- Preço[P]\nSua opção: ")
                    if opcao_atualizar == 'N':
                        livro['nome'] = input("\nNovo nome do livro: ")
                    elif opcao_atualizar == 'A':
                        livro['autor'] = input("\nNovo autor do livro:")
                    elif opcao_atualizar == 'P':
                        livro['preço'] = int(input("\nNovo preço do livro: "))
                    print(f"\nLivro '{livro_novo}' atualizado com sucesso!\n")
                    cont_mudar -= 10000000
                                                        
                    if cont_mudar > 0:
                        print("\nLivro não encontrado!")

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

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
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    elif mod == 5:
        
        preco_total = sum(livro['preço'] for categoria in biblioteca for livro in biblioteca[categoria])
        print("\nDinheiro total gasto em todos os livros: R$",preco_total)

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    elif mod == 6:
        print("wqe")
        #Carrinho#
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    elif mod == 7:
        print("Saindo do programa. Obrigado!\n")
        print("---------Volte sempre!---------\n")
        break