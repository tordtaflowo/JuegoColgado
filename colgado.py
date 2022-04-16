print("JUEGO DEL COLGADO")
print("TIENE 6 VIDAS")
print("ingrese las letras en minuscula")
print("_ _ _ _ _ _ _ _ _ \n")
## la palabra es programar
## 1=P 2=R 3=O 4=G 5=R 6=A 7=M 8=A 9=R

uno = "_"
dos = "_"
tres = "_"
cuatro = "_"
cinco = "_"
seis = "_"
siete = "_"
ocho = "_"
nueve = "_"

contador = 0

while contador < 6 :
    letra = str(input("ingrese una letra: "))
    if letra == "p":
        uno = "P"
        print("\nLA LETRA ES CORRECTA")
        contador += 1
    if letra == "r":
        dos = "R"
        cinco = "R"
        nueve = "R"
        print("\nLA LETRA ES CORRECTA")
        contador += 1
    if letra == "o":
        tres = "O"
        print("\nLA LETRA ES CORRECTA")
        contador += 1
    if letra == "g":
        cuatro = "G"
        print("\nLA LETRA ES CORRECTA")
        contador += 1
    if letra == "a":
        seis = "A"
        ocho = "A"
        print("\nLA LETRA ES CORRECTA")
        contador += 1
    if letra == "m":
        siete = "M"
        print("\nLA LETRA ES CORRECTA")
        contador += 1
    print(uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve ,"\n")
        

