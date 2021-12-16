def aprovado_t():
    esc_t = int(input("Tonny insira:\n1 para aprovado ou 2 para reprovado:\n"))

    if esc_t == 1:
            print("Aprovado!\n")
            return True
    if esc_t == 2:
            print("Reprovado!\n")
            return False



def aprovado_a():
    esc_a = int(input("Arthur insira:\n1 para aprovado ou 2 para reprovado:\n"))

    if esc_a == 1:
            print("Aprovado!\n")
            return True
    if esc_a == 2:
            print("Reprovado!\n")
            return False       



def aprovado_k():
    esc_k = int(input("Kelton insira:\n1 para aprovado ou 2 para reprovado:\n"))

    if esc_k == 1:
            print("Aprovado!\n")
            return True
    if esc_k == 2:
            print("Reprovado!\n")
            return False



def quem_reprovou():
    valores=[aprovado_t(),aprovado_a(),aprovado_k()]
    nomes=["Tonny", "Arthur", "Kelton"]
    
    for i in range(len(valores)):
        
        if valores [i]==False:
            print("Quem reprovou foi:", nomes[i])
            
            return nomes[i]
 
        




#def man():
valores=[aprovado_t(),aprovado_a(),aprovado_k()]
nomes=["Tonny", "Arthur", "Kelton"]
sina=True
stop=0
pare=0

print("Resultado do fluxo de AS: \n")

for i in range(len(valores)):

    if valores[i]==True:
#if: (aprovado_t() and aprovado_a() and aprovado_k()):
        stop+=1
        if stop==3:
            print("AS aprovada!")
    else:
        if sina:
            print("AS enviada para revisão!\n")
            sina=False
        if valores [i]==False:
            print("Quem reprovou foi:", nomes[i])
        


        






