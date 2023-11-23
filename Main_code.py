import os
import time


biblioteca = {}
lista_cat = []
cont_mudar = 0
lista_carrinho = []
preco_total = 0
preco_totalc = 0



def salvar_biblioteca():
    #abre o arquivo "biblioteca.txt" em modo de escrita ("w") com codificação UTF-8
    with open("biblioteca.txt", "w", encoding="utf8") as file:
        #percorre cada categoria e seus livros correspondentes no dicionário da biblioteca
        for cat, livros in biblioteca.items():
            #escreve a categoria no arquivo
            file.write(f"Categoria: {cat}\n")
            
            #percorre cada livro na categoria atual
            for livro in livros:
                #escreve o nome do livro no arquivo
                file.write(f"Nome: {livro['nome']}\n")
                
                #escreve o autor do livro no arquivo
                file.write(f"Autor: {livro['autor']}\n")
                
                #escreve o preço do livro no arquivo
                file.write(f"Preço: {livro['preço']}\n")
            
            #adiciona uma quebra de linha para separar diferentes categorias no arquivo
            file.write("\n")



def carregar_biblioteca():
    #define a variável global 'biblioteca' que será preenchida com os dados do arquivo
    global biblioteca
    biblioteca = {}

    #abre o arquivo "biblioteca.txt" para leitura, utilizando a codificação UTF-8
    with open("biblioteca.txt", "r", encoding="utf8") as file:
        #inicializa as variáveis 'cat' e 'livro' que serão usadas para armazenar temporariamente
        #a categoria atual e os dados de cada livro
        cat = None
        livro = None

        #percorre cada linha no arquivo
        for line in file:
            #remove espaços em branco no início e no final da linha
            line = line.strip()

            #verifica se a linha indica o início de uma nova categoria
            if line.startswith("Categoria: "):
                #extrai o nome da categoria da linha
                cat = line.split(": ")[1]
                #adiciona a categoria à lista global 'lista_cat'
                lista_cat.append(cat)
                #inicializa uma lista vazia para os livros da categoria
                biblioteca[cat] = []
            #verifica se a linha indica o nome de um livro
            elif line.startswith("Nome: "):
                #cria um dicionário para armazenar os dados do livro
                livro = {"nome": line.split(": ")[1]}
            #verifica se a linha indica o autor de um livro
            elif line.startswith("Autor: "):
                #adiciona o autor ao dicionário do livro
                livro["autor"] = line.split(": ")[1]
            #verifica se a linha indica o preço de um livro
            elif line.startswith("Preço: "):
                #adiciona o preço ao dicionário do livro como um número de ponto flutuante
                livro["preço"] = float(line.split(": ")[1])
                #verifica se todas as informações necessárias estão presentes para adicionar o livro à categoria
                if cat and livro["nome"] and livro["autor"] and "preço" in livro:
                    #adiciona o livro à lista de livros da categoria
                    biblioteca[cat].append(livro)
                    #reinicializa a variável 'livro' para a próxima iteração
                    livro = None


def salvar_carrinho():
    #abre o arquivo "carrinho.txt" em modo de escrita ("w") com codificação UTF-8
    with open("carrinho.txt", "w", encoding="utf8") as file:
        #percorre cada livro no carrinho (representado pela lista global 'lista_carrinho')
        for livro in lista_carrinho:
            #escreve no arquivo o nome do livro
            file.write(f"Nome: {livro['nome']}\n")
            #escreve no arquivo a categoria do livro
            file.write(f"Categoria: {livro['categoria']}\n")
            #escreve no arquivo o autor do livro
            file.write(f"Autor: {livro['autor']}\n")
            #escreve no arquivo o preço do livro
            file.write(f"Preço: {livro['preço']}\n")
        
        #adiciona uma quebra de linha para separar diferentes livros no arquivo
        file.write("\n")



def carregar_carrinho():
    #torna a variável 'lista_carrinho' global para que possa ser acessada e modificada fora da função
    global lista_carrinho
    
    #inicializa a lista_carrinho como uma lista vazia
    lista_carrinho = []
    
    #abre o arquivo "carrinho.txt" em modo de leitura ("r") com codificação UTF-8
    with open("carrinho.txt", "r", encoding="utf8") as file:
        
        #inicializa variáveis que armazenarão temporariamente os dados do livro
        nome = None
        categoria = None
        autor = None
        preco = None
        
        #itera sobre cada linha no arquivo
        for line in file:
            #remove espaços em branco no início e no final da linha
            line = line.strip()
            
            #verifica se a linha começa com "Nome: "
            if line.startswith("Nome: "):
                #extrai o nome do livro da linha
                nome = line.split(": ")[1]
            
            #verifica se a linha começa com "Categoria: "
            elif line.startswith("Categoria: "):
                #extrai a categoria do livro da linha
                categoria = line.split(": ")[1]
            
            #verifica se a linha começa com "Autor: "
            elif line.startswith("Autor: "):
                #extrai o autor do livro da linha
                autor = line.split(": ")[1]
            
            #verifica se a linha começa com "Preço: "
            elif line.startswith("Preço: "):
                #extrai o preço do livro da linha e converte para float
                preco = float(line.split(": ")[1])
                
                #adiciona um dicionário representando o livro à lista_carrinho
                lista_carrinho.append({"nome": nome, "categoria": categoria, "autor": autor, "preço": preco})
                



carregar_carrinho()
carregar_biblioteca()


def adicionar():
    #limpa a tela do console
    os.system("cls")
    
    #inicializa a variável de controle 'cont_add'
    cont_add = 0
    
    #solicita a categoria do livro ao usuário
    cat_add = input("Categoria do livro: ")
    
    #solicita o nome do livro ao usuário
    livro_name = input("Nome do livro: ")
    
    try:
        #verifica se o livro já existe na categoria especificada
        for livro in biblioteca[cat_add]:
            if livro_name == livro["nome"]:
                print("\nEsse livro já existe nessa categoria")
                time.sleep(2)
                cont_add += 1
                #chama recursivamente a função para permitir nova entrada
                adicionar()
        
        #se o livro não existe na categoria, continua o processo de adição
        if cont_add == 0:
            #solicita o autor do livro ao usuário
            livro_autor = input("Autor do livro: ")
            
            while True:
                try:
                    #solicita o preço do livro ao usuário e converte para float
                    livro_preco = float(input("Preço do livro: "))
                    break
                except ValueError:
                    print("Por favor, insira um valor numérico para o preço.")
            
            #cria um dicionário representando o livro
            livro = {"nome": livro_name, "autor": livro_autor, "preço": livro_preco}
            
            print("\nLivro adicionado com sucesso!")
            time.sleep(2)
            
            #adiciona o livro à biblioteca
            if cat_add in biblioteca:
                biblioteca[cat_add].append(livro)
            else:
                biblioteca[cat_add] = [livro]
            
            #atualiza a lista de categorias, se necessário
            if cat_add not in lista_cat:
                lista_cat.append(cat_add)
            
            #salva as alterações na biblioteca
            salvar_biblioteca()
    
    except KeyError:
        #se a categoria não existe, solicita o autor e preço do livro e adiciona à biblioteca
        livro_autor = input("Autor do livro: ")
        while True:
            try:
                livro_preco = float(input("Preço do livro: "))
                break
            except ValueError:
                print("Por favor, insira um valor numérico para o preço.")
        
        livro = {"nome": livro_name, "autor": livro_autor, "preço": livro_preco}
        print("\nLivro adicionado com sucesso!")
        time.sleep(2)
        
        if cat_add in biblioteca:
            biblioteca[cat_add].append(livro)
        else:
            biblioteca[cat_add] = [livro]
        
        if cat_add not in lista_cat:
            lista_cat.append(cat_add)
        
        salvar_biblioteca()


def excluir():
    #limpa a tela do console
    os.system("cls")
    
    #declara a variável global para armazenar o preço total
    global preco_total
    
    print("Categorias disponíveis: \n")
    
    #exibe as categorias disponíveis
    for x in lista_cat:
        print('-', x)
    print()
    
    #solicita a categoria do livro que o usuário deseja remover
    cat_remove = input("Digite a categoria do livro que você deseja remover: ")
    
    try:
        #obtém a lista de livros na categoria especificada
        livros_na_categoria = biblioteca[cat_remove]
        
        print(f"\nCategoria: {cat_remove}")
        print("\nLivros:\n")
        
        #exibe os livros na categoria
        for livro in livros_na_categoria:
            print(f"Nome: {livro['nome']}")
        
        #solicita o nome do livro que o usuário deseja remover
        livro_remove = input("\nDigite o livro que você deseja remover: ")
        
        try:
            #busca o livro na lista de livros da categoria e o remove
            for livro in livros_na_categoria:
                if livro['nome'] == livro_remove:
                    biblioteca[cat_remove].remove(livro)
                    print(f"\nLivro removido com sucesso!")
                    
                    #atualiza o preço total subtraindo o preço do livro removido
                    preco_total -= livro["preço"]
                    
                    break
           
        except ValueError:
            print("Erro: Livro não encontrado, tente novamente!")
            time.sleep(1)
        
    except KeyError:
        print(f"\nA categoria {cat_remove} não foi encontrada!")
        time.sleep(1)      
    
    #salva as alterações na biblioteca
    salvar_biblioteca()


def atualizar():
    #limpa a tela do console
    os.system("cls")
    
    print("Categorias disponíveis: \n")
    
    #declara a variável para contar as mudanças
    cont_mudar = 0
    
    #exibe as categorias disponíveis
    for x in lista_cat:
        print('-', x)
    print()
    
    #solicita a categoria do livro que o usuário deseja atualizar
    cat_atualizada = input("Digite a categoria do livro que você deseja atualizar: ")
    
    if cat_atualizada in biblioteca:
        print(f"\nCategoria: {cat_atualizada}")
        print("\nLivros:\n")
        
        #exibe os livros na categoria
        for livro in biblioteca[cat_atualizada]:
            print(f"Nome: {livro['nome']}")
        
        #solicita o nome do livro que o usuário deseja atualizar
        livro_novo = input("\nDigite o livro que você deseja atualizar: ")
        
        for livro in biblioteca[cat_atualizada]:

            if livro['nome'] == livro_novo:
                #solicita a opção de atualização
                cont_mudar += 1
                while True:
                    opcao_atualizar = input("\nDigite o que você deseja mudar:\n- Nome[N];\n- Autor[A];\n- Preço[P];\nSua opção: ")
                
                    if opcao_atualizar == 'N' or opcao_atualizar == 'n':
                        livro['nome'] = input("\nNovo nome do livro: ")
                        break
                    elif opcao_atualizar == 'A' or opcao_atualizar == 'a':
                        livro['autor'] = input("\nNovo autor do livro:")
                        break
                    elif opcao_atualizar == 'P' or opcao_atualizar == 'p':
                        while True:
                            try:
                                livro['preço'] = float(input("\nNovo preço do livro: "))
                                break
                            except ValueError:
                                print("\nDigite um valor numérico!")
                    else:
                        print("\nOpção invalida")
                
                print(f"\nLivro atualizado com sucesso!\n")
                cont_mudar -= 10000000
                
        if cont_mudar == 0:
            print("\nLivro não encontrado!")
                
            
    else:
        print("\nCategoria não encontrada")
    
    #salva as alterações na biblioteca
    salvar_biblioteca()

def visualizar():
    #limpa a tela do console
    os.system("cls")
    
    print("Categorias disponíveis: \n")
    
    #exibe as categorias disponíveis
    for x in lista_cat:
        print('-', x)
    print()
    
    #solicita a categoria do livro que o usuário deseja visualizar
    cat_visualizar = input("Digite qual a categoria do livro que você deseja visualizar: ")
    
    #limpa a tela do console
    os.system("cls")
    
    try:
        #verifica se a categoria existe na biblioteca
        if cat_visualizar in biblioteca:
            print(f"\nCategoria: {cat_visualizar}")
            
            #exibe os nomes dos livros na categoria
            for livro in biblioteca[cat_visualizar]:
                print(f"Nome: {livro['nome']}")
            
            #solicita o nome do livro para uma visão mais detalhada (ou '0' para voltar)
            livro_escolhido = input("\nDigite o nome do livro para uma visão mais detalhada (ou '0' para voltar): ")
            
            if livro_escolhido != '0':
                #procura o livro na categoria
                for livro in biblioteca[cat_visualizar]:
                    if livro['nome'] == livro_escolhido:
                        #exibe detalhes do livro
                        print(f"\nDetalhes do Livro:\nNome: {livro['nome']}\nAutor: {livro['autor']}\nPreço: {livro['preço']}")
                        break
                else:
                    #se o livro não for encontrado, levanta uma exceção
                    raise ValueError(f"\nO livro {livro_escolhido} não foi encontrado na categoria {cat_visualizar}.")
            else:
                print("\nVoltando...")
                time.sleep(2)
        else:
            #se a categoria não for encontrada, levanta uma exceção
            raise KeyError(f"A categoria {cat_visualizar} não foi encontrada.")
        
    except (KeyError, ValueError) as e:
        #trata exceções (KeyError para categoria não encontrada, ValueError para livro não encontrado)
        print(f"Erro: {e}")
        time.sleep(2)
        #chama a função novamente em caso de erro
        visualizar()

def carrinho_add():
    #limpa a tela do console
    os.system("cls")
    
    global lista_carrinho, preco_totalc
    
    #contador para verificar se o livro já está no carrinho
    cont_carrrinho_add = 0
    
    #solicita o nome do livro que o usuário deseja adicionar ao carrinho
    livro_name = input("Nome do livro: ")
    
    #verifica se o livro já está no carrinho
    for livro in lista_carrinho:
        if livro_name == livro["nome"]:
            print("\nEsse livro já se encontra no carrinho")
            time.sleep(1)
            cont_carrrinho_add += 1
            #chama a função novamente se o livro já estiver no carrinho
            carrinho_add()
    
    #se o livro não estiver no carrinho, prossegue com a adição
    if cont_carrrinho_add == 0:
        #solicita informações adicionais sobre o livro
        livro_categoria = input("Categoria do livro: ")
        livro_autor = input("Autor do livro: ")
        
        #tenta obter o preço do livro (valor numérico)
        try:
            livro_preco = float(input("Preço do livro: "))
        except ValueError:
            #trata exceção se o preço não for um valor numérico
            print("Por favor, insira um valor numérico para o preço.")
            return
        
        #cria um dicionário representando o livro e adiciona à lista do carrinho
        livro = {"nome": livro_name, "categoria": livro_categoria, "autor": livro_autor, "preço": livro_preco}
        lista_carrinho.append(livro)
        
        print("\nLivro adicionado ao carrinho com sucesso!")
        time.sleep(1)
        
        #salva o carrinho após adicionar o livro
        salvar_carrinho()


def carrinho_visualizar():
    #limpa a tela do console
    os.system("cls")
    
    global lista_carrinhoir
    
    #imprime a lista de livros no carrinho
    print("\nLivros no carrinho:")
    for livro in lista_carrinho:
        print(f"\nNome: {livro['nome']}\nCategoria: {livro['categoria']}\nAutor: {livro['autor']}\nPreço: {livro['preço']}")
        print("--" * 40 + '\n')  # Linha de separação entre os livros
    
    #solicita que o usuário digite qualquer coisa para sair
    encerrar = input("Digite qualquer coisa para sair: ")
    
    #salva o carrinho após visualizar os livros
    salvar_carrinho()



def carrinho_excluir():
    try:
        #limpa a tela do console
        os.system("cls")
        
        #variáveis globais
        global preco_totalc, lista_carrinho
        
        #imprime os livros no carrinho
        print("Livros no carrinho:\n")
        for livro in lista_carrinho:
            print(f"Nome: {livro['nome']}")
        
        #solicita ao usuário qual livro ele deseja excluir
        livro_excluir = input("\nQual livro você deseja excluir? ")
        
        try:
            #busca o livro no carrinho pelo nome
            livro_encontrado = next( livro for livro in lista_carrinho if livro['nome'] == livro_excluir)
        except StopIteration:
            raise ValueError
        
        #subtrai o preço do livro excluído do total do carrinho
        preco_totalc -= livro_encontrado['preço']
        
        #remove o livro do carrinho
        lista_carrinho.remove(livro_encontrado)
        
        print(f"\nO livro {livro_excluir} foi excluído com sucesso!")
        time.sleep(1)
        
        #limpa a tela do console
        os.system("cls")
    
    except ValueError:
        print(f"Erro: Livro não encontrado, Tente novamente! ")

#salva o carrinho após a execução da função
salvar_carrinho()


while True:
    while True:
        try:
            #imprime o menu de opções
            print(("--" * 13),"Menu",("--" * 13))
            mod = int(input("Pressione o número correspondente à alteração que deseja:\n\n[1]-Adicionar\n[2]-Excluir\n[3]-Atualizar\n[4]-Visualizar\n[5]-Dinheiro Gasto\n[6]-Carrinho\n[7]-Parar\n\nDigite aqui a sua opção: "))
            break
        except ValueError:
            print("Por favor digite um valor entre os estabelecidos anteriormente.")
    
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    if mod == 1:
        #chama a função para adicionar um livro
        adicionar()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif mod == 2:
        #chama a função para excluir um livro
        excluir()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif mod == 3:
        #chama a função para atualizar um livro
        atualizar()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif mod == 4:
        #chama a função para visualizar os livros
        visualizar()
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif mod == 5:
        #calcula e imprime o dinheiro total gasto em todos os livros
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
            #chama a função para adicionar um livro ao carrinho
            carrinho_add()
        elif escolha_carrinho == 2:
            #chama a função para visualizar os livros no carrinho
            carrinho_visualizar()
        elif escolha_carrinho == 3:
            #chama a função para excluir livros do carrinho
            carrinho_excluir()
    
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    elif mod == 7:
        #salva a biblioteca e o carrinho, e encerra o programa
        salvar_biblioteca()
        salvar_carrinho()
        print("Saindo do programa. Obrigado!\n")
        print("-------- Volte sempre! --------\n")
        break
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    else:
        print("\nPor favor digite um valor entre os estabelecidos anteriormente.")
        time.sleep(2)

