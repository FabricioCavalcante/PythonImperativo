import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    #print(freq)
    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    positivo=[]
    total_a_b=[]
    pos_a=0
    pos_b=0

    if len(as_a) and len(as_b)==6:
    
        for a in range(6):
            total_a_b.append(as_a[pos_a]-as_b[pos_b])
            pos_b+=1
            pos_a+=1
    #print(total_a_b)
    #print(len(total_a_b))

    for posit in total_a_b:
        positivo.append(abs(posit))

    print(positivo)
    
    sum_2textos=sum(positivo)
    #print(sum_2textos)
    g_similaridade=sum_2textos/6
    
    return g_similaridade
    
    #pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    assinatura=[]
    
    lista_palavras=[]
    #texto="Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
    sentencas = separa_sentencas(texto)
    for sent in sentencas:
        novas_frases = separa_frases(sent)
        for fr in novas_frases:
            novas_palavras = separa_palavras(fr)
            lista_palavras.extend(novas_palavras)
            
    n_frases=[]            
    sentencas = separa_sentencas(texto)
    for sent in sentencas:
        novas_frases = separa_frases(sent)
        for fr in novas_frases:
            n_frases.append(fr)

    n_caracteres=[]
    for palavra in lista_palavras:
        n_caracteres.extend(palavra)
    
            
    TMP=len(n_caracteres)/len(lista_palavras)
    #print("TMP= ",TMP)
    assinatura.append(TMP)
        
    MPD=n_palavras_diferentes(lista_palavras)/len(lista_palavras)
    #print("MPD= ", MPD)
    assinatura.append(MPD)
    
    MPU=n_palavras_unicas(lista_palavras)/len(lista_palavras)
    #print("MPU= ",MPU)
    assinatura.append(MPU)
    
    n_carac_sent=[]
    sentencas = separa_sentencas(texto)
    for sent in sentencas:
        n_carac_sent.extend(sent)    

    TMS=len(n_carac_sent)/len(separa_sentencas(texto))
    #print(n_carac_sent)
    assinatura.append(TMS)
    
    CS=len(n_frases)/len (separa_sentencas(texto))
    #print("CS: ",CS)
    assinatura.append(CS)
    
    n_caract_frase=[]
    sentencas = separa_sentencas(texto)
    for sent in sentencas:
        novas_frases = separa_frases(sent)
        for fr in novas_frases:
            n_caract_frase.extend(fr)        
    
    TMF=len(n_caract_frase)/len(n_frases)
    #print("TMF: ",TMF)
    #print(n_caract_frase)
    assinatura.append(TMF)
    
    return assinatura
    
    #pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    lista_g_similaridade=[]
    total_ass=[]
    for tex in textos:
        total_ass.append(calcula_assinatura(tex))
   #print("\ntotal_ass: ",total_ass)    
        
    for ass in total_ass:
        lista_g_similaridade.append(compara_assinatura(ass,ass_cp))
    #print("\nlista_g_similaridade: ",lista_g_similaridade)

    menor=min(lista_g_similaridade)
    #print("\nMenor",menor)
               
    #for pos, ind in enumerate(lista_g_similaridade,start=1):
        #print(f"\nNa posição: {pos}, encontrei o valor: {ind}")

    pos=1
    for graus in lista_g_similaridade:
        if graus == menor:
            return pos
        else:
            pos+=1        
        
    
    #pass
