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
        
        print("Os dados de cadastros estao corretos?:")
        print("DIGITE 1 PARA CONFIRMAR")
        print("DIGITE 2 PARA CORRIGIR")
        Confirmar = int(input("DESEJA CONFIRMAR OU CORRIGIR: "))
    
    elif Confirmar == 2:
        Email = input("E-mail:")
        Senha = input("Senha: ")

    # armazenar cadastro
    Cadastro = []
    Cadastro.append (Email)
    Cadastro.append (Senha)
    Cadastros.append (Cadastro)