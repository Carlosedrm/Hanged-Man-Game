forca = []
letrasUsadas = []
palavra = str(input("Digite sua palavra:"))
vidas = 6
check = 0

#Coloca X's na forca para simular a palavra
for i in palavra:
    forca.append("X")
    
#Funções

# Função para ver se a letra do usuário se encaxa nos critérios 
def verLetra(letra):
    # Se a palavra ja tiver sido usada ele fala sobre isso e termina a função 
    if letra in letrasUsadas:
        print("Essa letra já foi usada! Tente outra.")
        return 1
    # Se a letra não estar na palavra o jogador perde uma vida
    elif letra not in palavra:
        print("Essa letra não está na palavra!")
        letrasUsadas.append(letra)
        return 0
    # Vai vendo a letra 1 por um para colocar na forca se a letra estiver na palavra
    for i in range(len(palavra)):
        if letra == palavra[i]:
            forca[i] = letra
        i += i
    print("Acertou uma letra!")
    # Coloca a letra usada na lista de letras ja usadas
    letrasUsadas.append(letra)            
    return 1

# Função para ver se o usuário acertou a palavra  
def forcaCompleta():
    forcaString = ""
    #Compara a forca com a palavra para ver se o usuario acertou a palavra
    for i in forca:
        forcaString += i
    if forcaString == palavra:
        return 1
    else:
        return 0
# Função usada para imprimir a forca
def imprimirForca():
    for i in palavra:
        if i in letrasUsadas:
            print(i, end=" ")
        else:
            print("_", end=" ")
    print("")
    return 0
    
# Parte principal
while vidas != 0:
    check = forcaCompleta()
    if check == 1:
        print("Você acertou a palavra! Ela era:", palavra)
        break
    print("A forca está assim atualmente:")  
    #print(forca)  
    imprimirForca()    
    print("Letras usadas:")
    print(letrasUsadas)
    print("Quantidade de vidas", vidas)
    print("")
    letra = input("Digite a sua letra:")
    check = verLetra(letra)
    if check == 0:
        vidas -= 1
                
print("Obrigado por jogar!")
