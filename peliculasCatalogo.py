peliculas = []

def agregar_pelicula(num_pelis):
    for i in range(num_pelis):
        pelis=[]

        titulo=input("\nIngrese el título de la película: ").lower()
        pelis.append(titulo)
        estreno=int(input("Ingrese el año de estreno de la película: "))
        pelis.append(estreno)
        gen=input("Ingrese el género de la película: ").lower()
        pelis.append(gen)

        peliculas.append(pelis)

def mostrar_peliculas():
    contador=1
    for i in peliculas:
        print(f"Película {contador} ingresada: {i}")
        contador+=1
def buscar_genero(gen):
    for i in peliculas:
        for j in i:
            if j==gen:
                print(i)
            else:
                pass


while True:
    print("\n____MENÚ DE REGISTRO DE PELÍCULAS____")
    print("1. Agregar datos de películas")
    print("2. Mostrar las películas registradas")
    print("3. Buscar película por genero")
    print("4. Eliminar un registro por el título")
    print("5. Ver estadísticas de las peliculas")
    print("6. Salir del programa")

    opcion=input("\nSeleccione la opcion que desee:")

    match opcion:
        case "1":
            num_pls=int(input("\nIngrese la cantidad de peliculas de desea registrar: "))
            agregar_pelicula(num_pls)
            print("Pelicula agregada exitosamente")

        case "2":
            print("\nLas películas ingresadas son:")
            mostrar_peliculas()

        case "3":
            genero=input("Ingrese el genero de las peliculas que desee ver: ")
            print(f"Las peliculas catalogadas con el genero {genero} son:")
            buscar_genero(genero)


