biblioteca = {}

result = "S"
preco_total = 0
while result == "S":
    mod = int(input("Precione o numero correspondente a alteração que deseja:\n1-Adicionar\n2-Remover\n3-Alterar\n4-Visualizar\n5-Carrinho\n"))
    if mod == 1:
        option_1 = input("Voce deseja adicionar uma categoria('C') ou um Livro('L')?")
        if option_1 == "C":
            cat_add = input("Qual a categoria que deseja adicionar?")
            biblioteca[cat_add] = ""
            print(biblioteca)
        elif option_1 == "L":
            livro_name = input("Nome do livro:")
            livro_autor = input("Autor do livro")
            livro_categoria = input("Categoria do livro:")
            livro_preco = int(input("Preço do livro:"))
            livro = livro_name , livro_autor , livro_categoria , livro_preco
            biblioteca[livro_categoria] = [livro]
            print(biblioteca)
            preco_total =+ livro_preco
        else:
            print("Operação Invalida")

            
            







