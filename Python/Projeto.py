Cadastros = []
while True:
    print ("Seja Bem Vindo ao FEI TV")
    print ("MENU:")
    print("DIGITE ALGUM DOS NUMEROS PARA NAVEGAR ENTRE O MENU")
    print("1. CADASTRAR USUARIO")
    print ("2. LOGIN")

    menu = int(input("Número Menu: "))

    # cadastrar usuario

    if menu == 1:
        Email = input("E-mail:")
        Senha = input("Senha: ")
        
        print("OS DADOS DE CADASTRO ESTÃO CORRETOS?:")
        print("Digite 1 para CONFIRMAR")
        print("Digite 2 para CORRIGIR")
        Confirmar = int(input("DESEJA CONFIRMAR OU CORRIGIR: "))
    
    if Confirmar == 2:
        Email = input("E-mail:")
        Senha = input("Senha: ")

    

    # armazenar cadastro na lista
    Cadastro = []
    Cadastro.append (Email)
    Cadastro.append (Senha)
    Cadastros.append (Cadastro) 
    
    # armazenar as listas de cadastros em arquivos
    if Confirmar == 1:
        Arquivo = open('Arquivo.txt','w')
        Arquivo.write(f"{Cadastro[0]}\t{Cadastro[1]}\n")
        Arquivo.close()

    #login

    if menu == 2:
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
