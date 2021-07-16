


def usuario_escolhe_jogada(n,m):
    
    while n<=m:
        print("Oops! Jogada inválida! Tente de novo")
        n=int(input("Digite novamente o n"))
        m=int (input("Digite Novamente o m"))

    jm=0
    jm=int(input("Qual e o numero(s) de peça(s) retirada(s): "))

    while jm>m or jm<=0:
        print("Oops! Jogada inválida! Tente de novo")
        jm=int(input("Qual e o numero(s) de peça(s) retirada(s): " ))
        
    if jm<=m:
        print("O jogador tirou",jm,"peça(a)")
        n=n-jm
        return jm       
        
#devolver apenas o numero de peças removidas



def computador_escolhe_jogada (n,m):
    #n= Quantas peças?
    #m= Limite de peças por jogada?
    mt=m+1
    x=0 #numero retirado de peça(s)
    s=n

    while x<m:
        x+=1 
        if(n-x)%mt==0:
            print ("O computador tirou",x,"peça(s).")
            n-=x
            return x            
    #print ("O computador tirou",m,"peça(s).")
    x=m
    print ("O computador tirou",x,"peça(s).")
    n=n-x
    return x  



def partida():
    n=int(input("Quantas peças?"))
    m=int(input("Limite de peças por jogada?"))
    mt=m+1
    jm=0
    x=0
    
    if n%mt==0:
        print("Você começa!") #usuario_escolhe_jogada(n,m)
        while n>0:
            jm=usuario_escolhe_jogada(n,m)
            n-=jm
            x=computador_escolhe_jogada(n,m)
            n-=x
        print ("Fim do jogo! O computador ganhou!")
    else:
        print("Computador começa!") #computador_escolhe_jogada(n,m)
        while n>0:
            x=computador_escolhe_jogada(n,m)
            n-=x
            if n==0:
                print ("Fim do jogo! O computador ganhou!")
            else: jm=usuario_escolhe_jogada(n,m)
            n-=jm



def campeonato():
    print("**** Rodada 1 ****")
    partida()
    print("**** Rodada 2 ****")
    partida()
    print("**** Rodada 3 ****")
    partida()
    print("******* Final do campeonato! ****")
    print("Placar: Você 0 X 3 Computador")
    
    
    
#def man():
print ("Bem-vindo ao jogo do NIM! Escolha: ")
    
camp=int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato\n"))
while camp<1 or camp>2:
    print ("informe uma opção válida!")
    camp=int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato\n"))
        
if camp==1:
        print("Você escolheu uma partida isolada!")
        partida()
if camp==2:
        print("Voce escolheu um campeonato!")
        campeonato()