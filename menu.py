import time
lista_estudantes = []
lista_notas = []
#Função responsável por dar um efeito visual e um delay
def efeito_tempo():#sem cálculo
    print("."*2)
    time.sleep(1)
    print("."*4)
    time.sleep(1)
    print("."*8)
    time.sleep(1)
#Função responsável por chamar todas as outras incluvise o sair
def menu():#sem cálculo
    decisao = int(input("MENU:\n1.Cadastrar estudante\n2.Média da turma\n3.Lista de estudantes\n4.Buscar média de um estudante\n5.Deletar estudante\n0.Sair\n"))
    if decisao == 1:
        cadastrar_estudante()
    elif decisao == 2:
        media_geral()
    elif decisao == 3:
        ver_estudante()  
    elif decisao == 4:
        media_individual()
    elif decisao == 5:
        deletar_estudante()
    elif decisao == 0:
        exit(0)
    else:
        print("Digite somente os números do menu")
        menu()
#Função responsável por cadastrar um ou mais estudantes
def cadastrar_estudante():#com cálculos
    nome = str(input("Digite o nome: ")).upper()
    nota01 = float(input("nota 01: "))
    nota02 = float(input("Nota 02: "))
    nota03 = float(input("Nota 03: "))
    nota04 = float(input("Nota 04: "))
    notas = [nota01, nota02, nota03, nota04]
    soma = 0
    for valor in notas:
        if valor <= 10 and valor >= 0:
            soma += valor
        else:
            print("Digite somente números positivos por favor(entre 0 e 10)")
            cadastrar_estudante()
    efeito_tempo()
    lista_estudantes.append(nome)
    lista_notas.append(soma/4)
    print("Criado com sucesso!")

    escolher = str(input("Deseja adicionar outro estudante?(S/N)")).upper()
    if escolher == "S":
        cadastrar_estudante()
    else:
        menu()
#Função responsável por mostrar a média geral da turma
def media_geral():#sem cálculo
    efeito_tempo()
    print("A média geral da turma é: {:.2f}".format(sum(lista_notas)/len(lista_estudantes)))
    menu()
#Função responsável por mostrar todos os estudantes registrados
def ver_estudante():#sem cálculo
    escolha = str(input("Você deseja ver a lista de estudantes?(S/N) ")).upper()
    if escolha == "S":
        efeito_tempo()
        print(lista_estudantes)
    elif escolha == "N":
        print("Retornando ao menu...")
        efeito_tempo()
    else:
        print("Digite somente as opções indicadas")
        ver_estudantes()
    menu()
#Função responsável por mostrar uma média individual de um estudante previamente registrado
def media_individual():#sem cálculo
    nome = str(input("Digite o nome do estudante que deseja ver a média: ")).upper()
    count = 0
    for estudante in lista_estudantes:
        if nome == estudante:
            efeito_tempo()
            print(lista_estudantes[count],"tem média:", lista_notas[count])
            menu()
        else:
            pass
        count += 1
    print("Estudante não encontrado!")
    media_individual()
#Função responsável por deletar um estudante previamente registrado
def deletar_estudante():#sem cálculo
    nome_estudante = str(input("Digite o nome do estudante que deseja deletar: ")).upper()
    count = 0
    for termo in lista_estudantes:
        if nome_estudante == termo:
            lista_estudantes.pop(count)
            lista_notas.pop(count)
            efeito_tempo()
            print("Estudante deletado do nosso sistema")
        else: 
            pass
        count += 1
    menu()

menu()  