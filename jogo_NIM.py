def campeonato():
    print('Vamos jogar NIM! :)')
    print()
    print('Instruções: O jogo começa com um número de peças escolhido por você. Você deve revezar as jogadas com o computador, sendo que a cada rodada, cada um deve retirar no mínimo uma peça do jogo. O número máximo de peças a ser retirado a cada rodada também deve ser definido por você ao começo do jogo. Ganha quem retirar as últimas peças do jogo.')
    print()
    x = int(input('Digite 1 para jogar uma partida isolada e 2 para jogar um campeonato com três partidas: '))
    print()
    while x!=1 and x!=2:
        x=int(input('Entrada inválida. Tente novamente: '))
    if x==1:
        print('Você escolheu jogar uma partida isolada!')
        print()
        partida()
    if x==2:
        print('Você escolheu jogar um campeonato!')
        print()
        print('RODADA 1')
        print()
        partida()
        print('RODADA 2')
        print()
        partida()
        print('RODADA 3')
        print()
        partida()
        print('Placar: Você 0 X 3 Computador')

def partida():
    n=int(input("Defina o número de peças inicial: "))
    m=int(input("Defina o número máximo de peças que podem ser retiradas: "))
    while m>n or n<=0 or m<=0:
        print()
        print('Jogada inválida. O número de peças iniciais deve ser maior que o número máximo de peças a serem retiradas e ambos os números devem ser inteiros maiores que 0.')
        print()
        n=int(input("Defina o número de peças inicial: "))
        m=int(input("Defina o número máximo de peças que podem ser retiradas: "))
    if n%(m+1)==0:
        print()
        print ('Você começa!')
        r=usuario_escolhe_jogada(n,m)
        n=n-r
    else:
        print()
        print('Computador começa!')
    while n!=0:
        r=computador_escolhe_jogada(n,m)
        if n!=0:
             n=n-r
             r=usuario_escolhe_jogada(n,m)
             if n!=0:
                n=n-r
        else:
            print()

def computador_escolhe_jogada(n,m):
    while n!=0:
        r=n%(m+1)
        n=n-r
        if r==0:
            r=m
            n=n-r
            print('O computador tirou',r,'peças.')
        elif r!=1:
            print('O computador tirou',r,'peças.')
        else:
            print('O computador tirou 1 peça.')
        if n==0:
            print('O computador ganhou!')
            print()
        elif n==1:
            print ('Agora resta 1 peça no tabuleiro.')
        else:
            print('Agora restam',n,'peças no tabuleiro.')
            print()
            return r
    if n==0:
        return r

def usuario_escolhe_jogada(n,m):
    if n!=0:
        r=int(input('Quantas peças você vai tirar?: '))
        while r>m or r>n or r<=0:
            r=int(input('Jogada inválida. Tente outro número: '))
        if r!=1:
            print('Você tirou',r,'peças.')
        else:
            print('Você tirou 1 peça.') 
        n=n-r
        if n==0:
            print('Parabéns! Você ganhou o jogo!')
        else:
            if n!=1:
                print('Agora restam',n,'peças no tabuleiro.')
            else:
                print('Agora resta 1 peça no tabuleiro.')
            print()
        return r

campeonato()
