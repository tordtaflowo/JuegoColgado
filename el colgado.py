print("JUEGO DEL COLGADO")
print("TIENE 6 VIDAS")
print("(ingrese las letras en minuscula)")
print("_ _ _ _ _ _ _ _ _ \n")
## la palabra es programar

letra1 = str(input("ingrese una letra: "))
if letra1 == "p" :
    print("\nLA LETRA ES CORRECTA")
    print("P _ _ _ _ _ _ _ _ \n")
    
    letra2 = str(input("ingrese una letra: "))
    if letra2 == "r" :
        print("\nLA LETRA ES CORRECTA")
        print("P R _ _ R _ _ _ R \n")
        
        letra3 = str(input("ingrese una letra: "))
        if letra3 == "o" :
            print("\nLA LETRA ES CORRECTA")
            print("P R O _ R _ _ _ R \n")

            letra4 = str(input("ingrese una letra: "))
            if letra4 == "g" :
                print("\nLA LETRA ES CORRECTA")
                print("P R O G R _ _ _ R \n")

                letra5 = str(input("ingrese una letra: "))
                if letra5 == "a" :
                    print("\nLA LETRA ES CORRECTA")
                    print("P R O G R A _ A R \n")

                    letra6 = str(input("ingrese una letra: "))
                    if letra6 == "m" :
                        print("\nLA LETRA ES CORRECTA")
                        print("P R O G R A M A R \n")
                        print("ENCONTRASTE LA PALABRA")
    
                    else:
                        print("\nLA LETRA ES INCORRECTA, TIENE 5 VIDAS")
                        print("P R O G R A _ A R \n")

    
                elif letra5 == "m" :
                    print("\nLA LETRA ES CORRECTA")
                    print("P R O _ R _ M _ R \n")
    
                else:
                    print("\nLA LETRA ES INCORRECTA, TIENE 5 VIDAS")
                    print("P R O _ R _ _ _ R \n")
    
            elif letra4 == "a" :
                print("\nLA LETRA ES CORRECTA")
                print("P R O _ R A _ A R \n")
    
            elif letra4 == "m" :
                print("\nLA LETRA ES CORRECTA")
                print("P R O _ R _ M _ R \n")
    
            else:
                print("\nLA LETRA ES INCORRECTA, TIENE 5 VIDAS")
                print("P R _ _ R _ _ _ R \n")
                
        elif letra3 == "g" :
            print("\nLA LETRA ES CORRECTA")
            print("P R _ G _ R _ _ R \n")
    
        elif letra3 == "a" :
            print("\nLA LETRA ES CORRECTA")
            print("P R _ _ R A _ A R \n")
    
        elif letra3 == "m" :
            print("\nLA LETRA ES CORRECTA")
            print("P R _ _ R _ M _ R \n")
    
        else:
            print("\nLA LETRA ES INCORRECTA, TIENE 5 VIDAS")
            print("P R _ _ R _ _ _ R \n")
    
    elif letra1 == "o" :
        print("\nLA LETRA ES CORRECTA")
        print("P _ O _ _ _ _ _ _ \n")
    
    elif letra1 == "g" :
        print("\nLA LETRA ES CORRECTA")
        print("P _ _ G _ _ _ _ _ \n")
    
    elif letra1 == "a" :
        print("\nLA LETRA ES CORRECTA")
        print("P _ _ _ _ A _ A _ \n")
    
    elif letra1 == "m" :
        print("\nLA LETRA ES CORRECTA")
        print("P _ _ _ _ _ M _ _ \n")
    
    else:
        print("\nLA LETRA ES INCORRECTA, TIENE 5 VIDAS")
        print("P _ _ _ _ _ _ _ _ \n")
    
    
elif letra1 == "r" :
    print("\nLA LETRA ES CORRECTA")
    print("_ R _ _ R _ _ _ R \n")
    
elif letra1 == "o" :
    print("\nLA LETRA ES CORRECTA")
    print("_ _ O _ _ _ _ _ _ \n")
    
elif letra1 == "g" :
    print("\nLA LETRA ES CORRECTA")
    print("_ _ _ G _ _ _ _ _ \n")
    
elif letra1 == "a" :
    print("\nLA LETRA ES CORRECTA")
    print("_ _ _ _ _ A _ A _ \n")
    
elif letra1 == "m" :
    print("\nLA LETRA ES CORRECTA")
    print("_ _ _ _ _ _ M _ _ \n")
    
else:
    print("\nLA LETRA ES INCORRECTA, TIENE 5 VIDAS")
    print("_ _ _ _ _ _ _ _ _ \n")
    
