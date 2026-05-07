Cadastros = []
while True:
    print("=" * 50)
    print ("Seja Bem Vindo ao FEI TV")
    print ("MENU:")
    print("DIGITE ALGUM DOS NUMEROS PARA NAVEGAR ENTRE O MENU")
    print("1. CADASTRAR USUARIO")
    print ("2. LOGIN")
    print ("3. FILMES EM CATALÓGO")
    print ("4. PESQUISAR FILME POR NOME")
    print("=" * 50)
    menu = int(input("Número Menu: "))
    print("-" * 30)
    # cadastrar usuario

    if menu == 1:
        Email = input("E-mail:")
        Senha = input("Senha: ")
        print("-" * 30)
        print("OS DADOS DE CADASTRO ESTÃO CORRETOS?:")
        print("Digite 1 para CONFIRMAR")
        print("Digite 2 para CORRIGIR")
        Confirmar = int(input("DESEJA CONFIRMAR OU CORRIGIR: "))
        
        if Confirmar == 2:
            print("-" * 30)
            Email = input("E-mail:")
            Senha = input("Senha: ")
            

    

        # armazenar cadastro na lista
        Cadastro = []
        Cadastro.append (Email)
        Cadastro.append (Senha)
        Cadastros.append (Cadastro) 
        
        # armazenar as listas de cadastros em arquivos
        Arquivo = open('Arquivo.txt','a')
        Arquivo.write(f"{Cadastro[0]}\t{Cadastro[1]}\n")
        Arquivo.close()

    #login

    if menu == 2:
        print("-" * 30)
        print("Faça o seu Login:")
        Arquivo = open ('Arquivo.txt','r')
        lista = []
        for l in Arquivo:
            Email,Senha = l.strip().split("\t")
            lista.append((Email,Senha))
        Arquivo.close()

        Email_Login = input("Insira seu Email:")
        for Email,Senha in lista:
            if Email_Login == Email :
                Senha_Login = input("Insira sua Senha:")
                if Senha_Login == Senha:
                    print("LOGIN REALIZADO COM SUCESSO =)")
                else:
                    print("USÚARIO OU SENHA NÃO ESTÃO ERRADOS =( ")

    #filmes

    if menu == 3:
        arquivo = open('Filmes.txt', 'r')
        conteudo = arquivo.read()

        print ()
        print(conteudo)
        print ()

        arquivo.close()

    if menu == 4:   
        busca = input("Digite o nome do filme para ver os detalhes: ").lower()
        # encoding='utf-8' serve para não dar erro com acentos
        arquivo = open('Pesquisa_Filmes.txt', 'r', encoding='utf-8')

        encontrado = False
        
        print("\n" + "="*50)
        print(f"RESULTADOS PARA: {busca.upper()}")
        print("="*50)

        for linha in arquivo:
            # strip() remove o pulo de linha do final
            # split("/") divide a linha em uma lista de 3 partes
            dados = linha.strip().split("/")

            # Verifica se a linha tem as 3 partes
            if len(dados) >= 3:
                nome_filme = dados[0]
                diretor = dados[1]
                sinopse = dados[2]

                # Se o que o usuário digitou estiver no nome do filme...
                if busca in nome_filme.lower():
                    print(f"FILME: {nome_filme}")
                    print(f"DIRETOR: {diretor}")
                    print(f"SINOPSE: {sinopse}")
                    print("=" * 50)
                    encontrado = True

        if not encontrado:
            print("Esse filme não está no catálogo.")

        arquivo.close()
