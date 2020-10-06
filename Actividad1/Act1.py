if __name__ == "__main__":

    #define los vectores
    paisesefectoinvernadero = []
    paises2010 = []

    with open('greenhousedata.csv') as f:

        #lee archivo
        r = f.read().splitlines()
        #elimina la primer linea del archivo
        r.pop(0)

        #Separa por comas
        for j in r:

            lin = j.split(',')
            #agrega valores en lista
            paisesefectoinvernadero.append([float(lin[2]),int(lin[1]),str(lin[0])])

        for i in paisesefectoinvernadero:
            # si el año, alojado en el 2do valor es 2010:
            if i[1] == 2010:
                paises2010.append(i)

        #ordena el vector(paises2010)
        ordenada = sorted(paises2010, reverse = True)
    print("Mayores productores de gases de efecto invernadero:", "\n1: ", ordenada[0], "\n2: ", ordenada[3], "\n3: ",ordenada[6], "\n4: ", ordenada[9], "\n5: ", ordenada[12])

    #define el vector
    paises_poblacion = []
    with open('populationbycountry19802010millions.csv') as p:
        #Lee el archivo
        reader = p.read().splitlines()
        #Elimina el primer valor
        reader.pop(0)

        for i in reader:
            #Separa por comas
            line = i.split(',')
            #agrega valores a vector
            paises_poblacion.append([float(line[31]),str(line[0])])
    #ordena lista
    Paises_poblacionOrdenado = sorted(paises_poblacion, reverse = True)
    #imprime primeros 5 valores
    print("Países más poblados (2010): ","\n1: ",Paises_poblacionOrdenado[1],"\n2: ",Paises_poblacionOrdenado[2],"\n3: ",Paises_poblacionOrdenado[3],"\n4: ",Paises_poblacionOrdenado[4],"\n5: ",Paises_poblacionOrdenado[5])

