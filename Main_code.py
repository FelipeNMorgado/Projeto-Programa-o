biblioteca = {}
preco_total = 0

while True:
    mod = int(input("Pressione o número correspondente à alteração que deseja:\n1-Adicionar\n2-Remover\n3-Alterar\n4-Visualizar\n5-Carrinho\n6-Parar\n"))

    if mod == 1:
        option_1 = input("Você deseja adicionar uma categoria ('C') ou um Livro ('L')?")
        if option_1 == "C":
            cat_add = input("Qual a categoria que deseja adicionar?")
            biblioteca[cat_add] = []
            print(biblioteca)
        elif option_1 == "L":
            livro_name = input("Nome do livro:")
            livro_autor = input("Autor do livro:")
            livro_categoria = input("Categoria do livro:")
            livro_preco = int(input("Preço do livro:"))
            livro = {'nome': livro_name, 'autor': livro_autor, 'preco': livro_preco}
            
            if livro_categoria in biblioteca:
                biblioteca[livro_categoria].append(livro)
            else:
                biblioteca[livro_categoria] = [livro]
            
            print(biblioteca)
            preco_total += livro_preco
        else:
            print("Operação Inválida")

    elif mod == 6:
        print("Saindo do programa. Obrigado!")
        break


print(biblioteca)

            







