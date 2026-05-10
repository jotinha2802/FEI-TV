Cadastros = []
while True:
    print("==================================================\n" 
    "Seja Bem Vindo ao FEI TV\n"
    "MENU:\n"
    "DIGITE ALGUM DOS NUMEROS PARA NAVEGAR ENTRE O MENU\n"
    "1. CADASTRAR USUARIO\n"
    "2. LOGIN\n"
    "3. FILMES EM CATALÓGO\n"
    "4. PESQUISAR FILME POR NOME\n"
    "5. LISTA DE FAVORITOS\n"
    "==================================================")
    menu = int(input("Número Menu: "))
    print("=" * 50)
    # cadastrar usuario

    if menu == 1:
        Email = input("E-mail:")
        Senha = input("Senha:")
        print("=" * 50)
        print("OS DADOS DE CADASTRO ESTÃO CORRETOS?:\n"
        "Digite 1 para CONFIRMAR\n"
        "Digite 2 para CORRIGIR")
        Confirmar = int(input("DESEJA CONFIRMAR OU CORRIGIR: "))
        
        if Confirmar == 2:
            print("=" * 50)
            Email = input("E-mail:")
            Senha = input("Senha:")
        
        # armazenar cadastro na lista
        Cadastro = []
        Cadastro.append (Email)
        Cadastro.append (Senha)
        Cadastros.append (Cadastro) 
        
        # armazenar as listas de cadastros em arquivos
        Arquivo = open('Arquivo.txt','a')
        Arquivo.write(f"{Cadastro[0]}\t{Cadastro[1]}\n")
        Arquivo.close()
        
        print ("==================================================\n" 
        "CADASTRO REALIZADO COM SUCESSO =)")
    #login

    if menu == 2:
        print("Faça o seu Login:\n"
        "==================================================")
        Arquivo = open ('Arquivo.txt','r')
        lista = []
        for l in Arquivo:
            Email,Senha = l.strip().split("\t")
            lista.append((Email,Senha))
        Arquivo.close()

        Email_Login = input("Insira seu Email:")
        for Email,Senha in lista:
            usuario_encontrado = False
            if Email_Login == Email :
                usuario_encontrado = True
                Senha_Login = input("Insira sua Senha:")
                if Senha_Login == Senha:
                    print("==================================================\n"
                    "LOGIN REALIZADO COM SUCESSO =)")
                else:
                    print("==================================================\n"
                    "SENHA ESTA INCORRETA =( ")
                break  

        if not usuario_encontrado:
            print("=" * 50)
            print("USUÁRIO INCORRETO =(")
    #filmes

    if menu == 3:
        arquivo = open('Filmes.txt', 'r')
        conteudo = arquivo.read()

        print ()
        print(conteudo)
        print ()

        arquivo.close()

    if menu == 4:   
        busca = input("DIGITE O NOME DO FILME PARA TER OS DETALHES: ").lower()
        
        arquivo = open('Pesquisa_Filmes.txt', 'r', encoding='utf-8')
        linhas = arquivo.readlines()
        arquivo.close() 
        
        encontrado = False
        conteudo_atualizado = []

        print("==================================================\n")
        print(f"RESULTADOS PARA: {busca.upper()}\n"
        "==================================================")

        for linha in linhas:
            dados = linha.strip().split("/")
            
            if len(dados) >= 3:
                nome_filme = dados[0]
                diretor = dados[1]
                sinopse = dados[2]
                
                curtidas = int(dados[3]) if len(dados) > 3 else 0
                descurtidas = int(dados[4]) if len(dados) > 4 else 0

                # Verifica se o termo buscado está no nome do filme
                if busca in nome_filme.lower():
                    encontrado = True
                    print (f"FILME: {nome_filme}\n"
                    f"DIRETOR: {diretor}\n"
                    f"SINOPSE: {sinopse}\n"
                    f"AVALIAÇÕES: 👍 {curtidas} | 👎 {descurtidas}\n"
                    "==================================================\n" 
                    "DÊ PLAY PARA ASSISTIR O FILME\n"
                    "1. ASSISTIR FILME\n"
                    "2. SAIR DESSE FILME")
                    
                    x = input("ESCOLHA UMA OPÇÃO:") 
                    print("=" * 50)
                    
                    if x == "1":
                        print("PEGUE A SUA PIPOCA, O FILME ESTÁ RODANDO...\n"
                        "===================================================\n"
                        "O QUE VOCÊ CURTIU O FILME?\n"
                        "1. Curtir 👍\n"
                        "2. Descurtir 👎\n"
                        "3. Sair")
                        opcao_voto = input("ESCOLHA UMA OPÇÃO:")
                        
                        if opcao_voto == "1":
                            curtidas += 1
                            print("SUCESSO! VOCÊ CURTIU O FILME.")
                        elif opcao_voto == "2":
                            descurtidas += 1
                            print("SUCESSO! VOCÊ DESCURTIU O FILME.")
                        print("=" * 50)
                    else:
                        print("SAINDO DO FILME...\n"
                        "==================================================" )

                # remonta a linha (com os dados novos ou os originais)
                # e adiciona na lista para não perder nenhum filme do arquivo
                ##nova_linha = f"{nome_filme}/{diretor}/{sinopse}/{curtidas}/{descurtidas}\n"
                ##conteudo_atualizado.append(nova_linha)
        
        if encontrado:
            # Salva tudo de volta no arquivo
            arquivo = open('Pesquisa_Filmes.txt', 'w', encoding='utf-8')
            arquivo.writelines(conteudo_atualizado)
            arquivo.close()
        else:
            print("ESSE FILME NÃO EXISTE NO CATÁLOGO.")

    if menu == 5:
        print ("SEJA BEM VINDO AO GERENCIADOR DE FILMES FAVORITOS\n"
        "==================================================\n"
        "1. VER OS FILMES FAVORITOS\n"
        "2. FAVORITAR FILMES\n"
        "3. DELETAR FILME DOS FAVORITOS\n")
        favoritos = int(input("OQUE VOÇÊ DESEJA FAZER?\n"))
        print("=" * 50)

        if favoritos == 1:
        
            arquivo_fav = open('Favoritos.txt', 'r', encoding='utf-8')
            FAV = arquivo_fav.read()
            arquivo_fav.close()
            
            if FAV.strip() == "":
                print("SUA LISTA DE FAVORITOS ESTÁ VAZIA!")
            else:
                print("SEUS FILMES FAVORITOS:")
                print(FAV)
        
        if favoritos == 2:
            
            print ("QUAL FILME VOÇÊ QUER FAVORITAR:\n"
            "==================================================\n"
            "1. Avatar (2009)\n"
            "2. Vingadores (2012)\n"
            "3. Titanic (1997)\n"
            "4. Divertida Mente (2015)\n"
            "5. Homem-Aranha (2002)\n"
            "6. Michael (2025)\n"
            "7. Matrix (1999)\n"
            "8. Interestelar (2014)\n"
            "9. Pantera Negra (2018)\n"
            "10. Homem de Ferro (2008)\n"
            "==================================================" )
            adc_fav = int(input("DIGITE O NUMERO DO FILME QUE DESEJA:"))
            
            lista_filmes = ["Avatar", "Vingadores", "Titanic", "Divertida Mente", 
            "Homem-Aranha", "Michael", "Matrix", "Interestelar", 
            "Pantera Negra", "Homem de Ferro"]

            if 1 <= adc_fav <= 10:
                filme_escolhido = lista_filmes[adc_fav - 1]

                # Lê os favoritos já salvos
                arquivo_fav = open('Favoritos.txt', 'r', encoding='utf-8')
                favoritos_salvos = arquivo_fav.read()
                arquivo_fav.close()
                
                # Verifica se o filme já está na lista
                if filme_escolhido in favoritos_salvos:
                    print("=" * 50)
                    print(f"'{filme_escolhido}' JÁ ESTA NA SUA LISTA DE FAVORITOS")
                else:
                    arquivo_fav = open('Favoritos.txt', 'a', encoding='utf-8')
                    arquivo_fav.write(filme_escolhido + "\n")
                    arquivo_fav.close()
                    print("=" * 50)
                    print(f"SUCESSO! '{filme_escolhido}' FOI ADICIONADO AOS FAVORITOS")
            else:
                print("=" * 50)
                print("NÚMERO INVALIDO, DIGITE UM NÚMERO DE 1 A 10.")
        
        if favoritos == 3:
            
            arquivo_fav = open('Favoritos.txt', 'r', encoding='utf-8')
            linhas = arquivo_fav.readlines()
            arquivo_fav.close()

            if not linhas:
                print("SUA LISTA ESTÁ VAZIA!")
            else:
                arquivo_fav = open('Favoritos.txt', 'r', encoding='utf-8')
                FAV = arquivo_fav.read()
                arquivo_fav.close()
                print (FAV)
                print("=" * 50)

                # Passo 2: filtrar
                filme_deletar = input("DIGITE O NOME DO FILME PARA DELETAR: ")
                linhas_atualizadas = []
                for l in linhas:
                    if filme_deletar.strip().lower() != l.strip().lower():  
                        linhas_atualizadas.append(l)

                # Passo 3: verificar e reescrever
                if len(linhas_atualizadas) == len(linhas):
                    print(f"'{filme_deletar}' NÃO FOI ENCONTRADO!")
                else:
                    arquivo_fav = open('Favoritos.txt', 'w', encoding='utf-8')
                    arquivo_fav.writelines(linhas_atualizadas)
                    arquivo_fav.close()
                    print(f"'{filme_deletar}' FOI DELETADO DA LISTA DE FAVORITOS!")