bandas = []


#CONSTRUYENDO LA INTERFAZ 
print("***ALTAVOZ ES TU VOZ***")
print("**************************")

opcion=100
while(opcion!=5):
    print("1.Registrar Banda")
    print("2.Buscar informacion de una Banda")
    print("3.Agenda el evento")
    print("4.Modificar una banda")
    print("5.SALIR")

    opcion= int(input("Digita una opcion:  "))

    if opcion==1:
        #Creando los datos del diccionario.
        banda = {}
        banda["id"]= int(input("Digita el id: "))
        banda["nombre"]= (input("Nombre de la banda: "))
        banda["genero"]= (input("Genero:"))
        banda["clasificacion"]= (input("Clasificacion: "))
        banda["tiempo"]= int(input("Tiempo: "))
        banda["costo"]= int(input("Costo: $"))

        #Agregando un diccionario a una lista
        bandas.append(banda)

    elif opcion==2:
        bandaBuscada=input("Digita el nombre de la banda que estás buscando: ")
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"]==bandaBuscada:
                #Muestro los datos de la bandaAuxiliar
                print(f"id: {bandaAuxiliar["id"]}--- nombre: {bandaAuxiliar["nombre"]}")
            else:
                print("Siga intentando socio")
                

    elif opcion==3:
        print(bandas)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        pass





