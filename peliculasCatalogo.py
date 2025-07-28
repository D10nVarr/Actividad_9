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
                continue

def eliminar_peli(title):
    global peliculas
    for i in peliculas:
        for j in i:
            if j==title:
                peliculas.remove(i)
            else:
                continue

def ver_stats():
    print(f"Existen {len(peliculas)} peliculas registradas")

    print("Existen estos generos de películas")
    for i in peliculas:
        print(i[2])

    est_antigua=peliculas[0][1]
    antigua=peliculas[0]

    for i in peliculas:
        if i[1]<est_antigua:
            est_antigua=i[1]
            antigua=i
    print("La pelicula más antigua es: ",antigua)

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
            if len(peliculas)>0:
                print("\nLas películas ingresadas son:")
                mostrar_peliculas()
            else:
                print("No hay peliculas registradas")

        case "3":
            if len(peliculas) > 0:
                genero=input("\nIngrese el genero de las peliculas que desee ver: ").lower()
                print(f"Las peliculas catalogadas con el genero {genero} son:")
                buscar_genero(genero)
            else:
                print("No hay peliculas registradas")

        case "4":
            if len(peliculas) > 0:
                titl=input("\nIngrese el titulo de la pelicula que desee eliminar: ").lower()
                eliminar_peli(titl)
                print("Registro eliminado exitosamente")
            else:
                print("No hay peliculas registradas")

        case "5":
            if len(peliculas) > 0:
                ver_stats()
            else:
                print("No hay peliculas registradas")

        case "6":
            print("\nSaliendo del programa...")
            break

        case _:
           print("Opcion no valida")



