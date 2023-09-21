letras_orden = []
letras_reversa = []
def introducir_frase(): #Este metodo devuelve una frase o palabra introducida por el usuario
    frase = input("Escribe una palabra o frase:  ")
    return frase.replace(" ","")

def seperar_frases(frase): # Este metodo guarda la frase introducida en 2 cadenas elminando los espacios
    for i in range(len(frase)):
       if (frase[i] not in " "):
            letras_orden.append(frase[i])
            letras_reversa.append(frase[i])

def ordenar_frase_reversa():# Este metodo ordena en reversa una de las cadenas donde se guardo la frase o letra sin espacios
    letras_reversa.reverse()

def comprobar_palindromo():# Este metodo compara ambas cadenas una en orden y otra en reversa
    if(letras_orden == letras_reversa):
        print("La frase o palabra introducida es palidroma")
    else:
        print("La frase o palabra intorducida no es palidroma")

seperar_frases(introducir_frase()) #Como el metodo introducir frase retorna el string lo paso como argumento a la funcion de separar
ordenar_frase_reversa()
comprobar_palindromo()