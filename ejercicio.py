#Se acumulan las palabras censuradas
palabras_censuradas = []

while True : 
    #Menu
    print("Ingrese una opcion")
    print("1.- Ingresar una palabra a Censurar")
    print("2.- Ingrese un texto")
    print("3.-Salir")

    #Se guarda la opcion ingresada
    opcion_usuario = int(input("Ingrese un texto : "))

    if opcion_usuario == 1 :
        #Se guarda una palabra ingresada
        palabra = input("Ingrese una palabra : ")
        #Se agrega la palabra ingresada en la lista "palabras censuradas"
        palabras_censuradas.append(palabra)

    if opcion_usuario == 2 :
        #Se guarda un texto ingresado por el usuario
        texto = input("Ingrese un texto o escriba algo ; ")
        #Se separan las palabras del texto usando como separador los espacioc
        texto_separado = texto.split(" ")
        #Ciclo para recorrer el teo separado
        for i in texto_separado : 
            #Si la iteracion esta dentro de la lista de palabras censuradas
            if i in palabras_censuradas  : 
                texto_censurado = texto_censurado.replace(i,"*"*len(i))
                '''
                El texto cemsrurado es igual a que si i esta dentro de las
                palanbras sencuradas , se reemplaza com un "*" con el largo de la palabra que es i
                '''
        
            print(texto_censurado)


    if opcion_usuario == 3 :
        print("A salido del programa")
        break


    


