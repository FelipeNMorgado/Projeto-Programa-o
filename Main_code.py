import os
os.system("cls")

biblioteca = {}
lista_cat = []
preco_total = 0
cont = 0

while True:
    
    print("--"*40)
    mod = int(input("Pressione o número correspondente a alteração que deseja:\n\n[1]-Adicionar\n[2]-Excluir\n[3]-Atualizar\n[4]-Visualizar\n[5]-Dinheiro Gasto\n[6]-Parar\n\nDigite aqui a sua opção: "))
    

    if mod == 1:
        
        cat_add = input("Categoria do livro: ")
        livro_name = input("Nome do livro: ")
        livro_autor = input("Autor do livro: ")
        livro_preco = int(input("Preço do livro: "))
        livro = {"nome": livro_name, "autor": livro_autor, "preço": livro_preco}
        if cat_add in lista_cat:
            continue
        else:
            lista_cat.append(cat_add)
            
        if cat_add in biblioteca:
                biblioteca[cat_add].append(livro)
        else:
                biblioteca[cat_add] = [livro]
        cont += 1
            
        print(biblioteca)
        preco_total += livro_preco
        
    elif mod == 2:
        
        option_2 = input("Digite o nome do livro que você deseja excluir: ")        

    elif mod == 3:
        print()

    elif mod == 4:
        print("Categorias disponiveis")
        for x in range(cont):
            print('-',lista_cat[x],'\n')
        cat_visualizar = input("Digite qual é categoria do livro que você deseja visualizar: ")
        if cat_visualizar in biblioteca:
            print(f"Categoria: {cat_visualizar}")
            for livro in biblioteca[cat_visualizar]:
                 print(f"{livro['nome']}")
                 cont+=1
                 
        #print(categoria)
        #print()
        #input("Digite qual o livro que você deseja visualizar: ")
    
    elif mod == 5:
        print()
    
    elif mod == 6:
        print("Saindo do programa. Obrigado!")
        break

    else:
        print("Operação Inválida")