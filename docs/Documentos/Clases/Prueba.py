mi_musica = {70: ["Stairway to heaven", "Bohemian Rhapsody"],80: ["Dancing in the dark", "Welcome to the jungle", "Under pressure"], 2000:["Given up", "The pretender"]} 
tema = input("Ingresá un nuevo tema (FIN para terminar): ")
while tema !="FIN":
    try:
        decada = int(input("ingresá a qué década pertenece: "))
        mi_musica[decada].append(tema)
    except ValueError:
        print("Para ingresar la decada, tenés que ingresar un número. Empecemos de nuevo...")
    except KeyError:
        print("""Por ahora, sólo tengo registradas las décadas: 70, 80 y 2000. Ingresá una de ellas. Empecemos de nuevo...""")
    tema = input("Ingresá un nuevo tema (FIN para terminar): ")