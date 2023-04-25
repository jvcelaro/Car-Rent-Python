import os

lista = ["Chevrolet Tracker - 120 / dia",
            "Chevrolet Onix - 90 / dia",
            "Chevrolet Spin - 150 / dia",
            "Hyundai HB20 - 85 / dia",
            "Hyundai Tcson - 120 / dia",
            "Fiat Uno - 60 / dia",
            "Fiat Mobi - 70 / dia",
            "Fiat Pulse - 130 / dia"]

listaPreco = [120, 90, 150, 85, 120, 60, 70, 130]

listaAlugados = []

#=======================================================

def inicio():

    print("==================")
    print("Bem vindo á locadora de carros!")
    print("==================")
    print("O que deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")
    choice = int(input())

    if choice == 0:
        os.system('cls') or None
        portifolio()
    elif choice == 1:
        os.system('cls') or None
        alugar()
    elif choice == 2:
        os.system('cls') or None
        devolver()
    else:
        while choice != 0 or choice != 1 or choice != 2:
            os.system('cls') or None
            print("======== Resposta invalida ========")
            inicio()

#=======================================================

def portifolio():


    for i in lista:
        print([lista.index(i)] , i)
    
    print("========================")
    print("0 - Continuar | 1 - Sair")
    choice2 = int(input())

    if choice2 == 0:
        inicio()
    elif choice2 == 1:
        os.system('cls') or None
    else:
        while choice2 != 1 and choice2 != 0:
            os.system('cls') or None
            print("==================")
            print("Opção incorreta!")
            inicio()

#=======================================================

def execAlugar(choiceCarros, choiceDias):

    total = listaPreco[choiceCarros] * choiceDias

    os.system('cls') or None
    print("Voce escolheu {0} por {1} dias".format(lista[choiceCarros], choiceDias))
    print("O aluguel totalizaria R$ {}. Deseja alugar?".format(total))
    print("0 - SIM | 1 - NÃO")
    alugarChoice = int(input())
    if alugarChoice == 0:
        listaAlugados.append(lista.pop(choiceCarros))
        print("Parabéns você alugou {0} por {1} dias".format(lista[choiceCarros], choiceDias))
        print("========================")
        print("0 - Continuar | 1 - Sair")
        choice = int(input())
        if choice == 0:
            inicio()
        elif choice == 1:
            os.system('cls') or None
        else:
            while choice != 1 and choice != 0:
                os.system('cls') or None
                print("Opção incorreta!")
                print("0 - Continuar | 1 - Sair")
                choice = int(input())
                if choice == 0:
                    inicio()
                elif choice == 1:
                    os.system('cls') or None
    else:
        os.system('cls') or None
        inicio()

#=======================================================

def alugar():

    for i in lista:
        print([lista.index(i)], i)

    print("========================")
    print("Escolha um carro:")
    choiceCarros = int(input())
    print("Escolha por quantos dias quer alugar o carro:")
    choiceDias = int(input())

    if choiceCarros >= 0 and choiceCarros <= 7:
        execAlugar(choiceCarros, choiceDias)           
    else:
        while choiceCarros < 0 or choiceCarros > 7:
            print("Escolha invalida!")
            print("========================")
            print("Escolha um carro:")
            choiceCarros = int(input())
            if choiceCarros >= 0 and choiceCarros <= 7:
                execAlugar(choiceCarros, choiceDias)

#=======================================================
            
def devolver():

    print("========================")
    print("Segue a lista dos carros alugados. Qual você deseja devolver?")

    for i in listaAlugados:
        print([listaAlugados.index(i)], i)

    print("Qual o codigo do carro que deseja devolver?")
    choiceCarros = int(input())
    
    if listaAlugados == []:
        print("========================")
        print("======== Não há carros para devolver, vamos te redirecionar para o menu inicial ========")
        inicio()
    if choiceCarros == listaAlugados.index(i):
        os.system('cls') or None
        print("Obrigado pelo sua devolução!!!")
        lista.append(listaAlugados.pop(choiceCarros))
        inicio()
    else:
        print("======== Codigo invalido ========")
        inicio()
    
#=======================================================
    
inicio()