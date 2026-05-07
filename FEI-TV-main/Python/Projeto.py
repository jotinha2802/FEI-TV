Cadastros = []
while True:
    print("-" * 50)
    print ("Seja Bem Vindo ao FEI TV")
    print ("MENU:")
    print("DIGITE ALGUM DOS NUMEROS PARA NAVEGAR ENTRE O MENU")
    print("1. CADASTRAR USUARIO")
    print ("2. LOGIN")
    print ("3. FILMES EM CATALÓGO")
    print ("4. PESQUISAR FILME POR NOME")
    print("-" * 30)
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
        Arquivo = open('Arquivo.txt','w')
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
                    print("Login Realizado com Sucesso =)")
            else:
                print("USÚARIO NÃO ENCONTRADO =( ")

    #filmes

    if menu == 3:
        arquivo = open('Filmes.txt', 'r')
        conteudo = arquivo.read()

        print ()
        print(conteudo)
        print ()

        arquivo.close()

    if menu == 4:   
        busca = input("Digite o nome do filme: ").lower()

        arquivo = open('Filmes.txt', 'r')

        resultados = []
        
        for linha in arquivo:
            # Remove espaços extras e quebras de linha 
            nome_filme = linha.strip()
            
            # Verifica se a busca está dentro do nome do filme (ignorando maiúsculas/minúsculas)
            if busca in nome_filme.lower():
                resultados.append(nome_filme)

        arquivo.close()

        # Mostra os resultados na tela
        print("-" * 30)
        if resultados:
            print(f"Encontramos {len(resultados)} resultado(s):")
            for item in resultados:
                print(f"• {item}")
        else:
            print("Nenhum filme encontrado com esse nome.")
        print("-" * 30)