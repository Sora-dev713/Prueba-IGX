#Funcion que comprueba recursivamente la conexion entre nodos
#se trabajara con 0s y 1s como valores de verdad, estos seran traducidos a YES o NO mas adelante
#0 = no, 1 = yes
def comprobar(nodoA, nodoB, arbol):
    #Caso base 1: Nodos iguales
    if nodoA == nodoB:
        print("La arista que estoy revisando es: "+ str(nodoA)+", "+str(nodoB)+ " y son el mismo por lo que encontré el camino")
        return 1
    #Caso base 2 = no se encuentran las aristas
    if nodoA == None or nodoB == None:
        print("La arista que estoy revisando es: "+ str(nodoA)+", "+str(nodoB))
        return 0
    #caso recursivo: nodoA distinto a nodoB
    if nodoA != nodoB:
        #si comprobamos los valores
        resultado = 0  
        #en caso de que sean diferentes, no necesariamente u<v
        arista = [nodoA, nodoB]
        print("La arista que estoy revisando es: "+ str(nodoA)+", "+str(nodoB))
        #si la arista no esta en el arbol, no hay camino
        if arista not in arbol:
            #se comprueban los nodos adyacentes
            nodoTemp = None
            for i in arbol:
                #se buscan las posibilidades
                if i[0] == nodoA:
                    nodoTemp = i[1]
                    print("La arista no estaba, pero se encuentra: " + str(nodoA)+", "+str(nodoTemp))
                    return resultado + comprobar(nodoTemp, nodoB, arbol)
        else:
            print("la arista estaba por lo que retornamos 1")
            return 1
        
#Funcion para abrir el archivo y leer sus contenidos de manera logica
def abrirArchivo():
    file = open("input.txt", "r")
    archivoRaw = file.readlines()
    #print(archivoRaw)
    archivo = []
    for linea in archivoRaw:
        #se le da el formato de [numero , numero]
        temporal = linea.strip("\n").strip("\0").split(" ")
        archivo.append([int(temporal[0]), int(temporal[1])])
    return archivo

#Lectura del arbol dado en el archivo
def lecturaArbol(archivo):
    #se toma el n
    n = archivo[0][0]
    arbol = []
    i = 1
    #se genera un ciclo que va hasta n-1
    while i < n:
        #agregamos las aristas al arbol
        arbol.append(archivo[i])
        i+=1
    return arbol

#Funcion que realiza las queries, una a una.
def retornoQueries(archivo):
    #se toman los datos necesarios desde el archivo
    n = int(archivo[0][0])
    q = int(archivo[0][1])
    #se lee el arbol
    arbol = lecturaArbol(archivo)
    resultados=[]
    i = n
    #como las queries parten en la linea siguiente a la ultima de las aristas,
    #el archivo tiene n + q lineas, partiendo las queries en la linea n
    while i < n + q:
        #se leen ambos nodos
        nodoA = archivo[i][0]
        nodoB = archivo[i][1]
        #los prints son desechables, unicamente sirven para revision propia
        print("Query a revisar = " + str(nodoA) +","+ str(nodoB))
        #se pide el resultado con la funcion anterior
        resultados.append(comprobar(nodoA, nodoB, arbol))
        print("--------------------------")
        i+=1
    return resultados

#funcion para que los resultados queden como en el output deseado
#una especie de "Traductor" de 0s y 1s
def impresorResultados(listado):
    print("Output:\n---------------------")
    for i in listado:
        if(i >= 1):
            print("YES")
        else:
            print("NO")


## comenzando con el flujo principal
#lectura de archivo
archivo = abrirArchivo()
#a partir del archvio, se revisan las queries
#dentro de este proceso se obtiene el arbol
resultados = retornoQueries(archivo)
#se imprime el resultado por pantalla
impresorResultados(resultados)

    