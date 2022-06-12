<h1 align="center"><img src="https://media.giphy.com/media/iQrDORShLPiqQ/giphy.gif" height="38" /> Seminario de Lenguajes Python </a>
 <img style="transform:scaleX(-1);" src="https://media.giphy.com/media/NLu0gwvgUMdxPtAHqS/giphy.gif" height="38" /></h1>

<div align="center">
<img src="https://media.giphy.com/media/KbUEFowFNOLSAsHT7u/giphy.gif" align="right" height="178" >



<table >
<tr>
<td> Teoria (Desafios y Tareas)</td> <td> Practica (Ejercicios)</td>
</tr>
<tr>
<td>
 
- [Clase 1](/docs/Documentos/Clases/Clase1.md)
- [Clase 1.1](/docs/Documentos/Clases/Clase1_1.md)
- [Clase 2](/docs/Documentos/Clases/Clase2.md)
- [Clase 3](/docs/Documentos/Clases/Clase3.md)
- [Clase 3.1](/docs/Documentos/Clases/Clase3_1.md)
- [Clase 4](/docs/Documentos/Clases/Clase4.md)
- [Clase 6](/docs/Documentos/Clases/Clase6.md)
- [Clase 7](/docs/Documentos/Clases/Clase7.md)

</td>
<td>


- [Ahorcado](/docs/Documentos/Ahorcado.md)
- [Practica 1](/docs/Documentos/Practica1.md)
- [Practica 2](/docs/Documentos/Practica2.md)
- [Practica 3](/docs/Documentos/Practica3.md)

 
</td>
</tr>
 
</table>

</div>

---


### 📖 Resumenes de cada tema:



<br>



<details ><summary>Clase_1_Introduccion</summary> 
<br>

```Python
cadena = "dos"
match cadena:
    case "uno":
        print("UNO")
    case "dos" | "tres":
        print("DOS O TRES")
    case _:
        print("Ups.. ninguno de los anteriores")
```

```Python
intento = 3
nombre = "claudia"
print(f'Hola {nombre} !!! Ganaste! y necesitaste {intento} intentos!!!')
x = 4
print(f"{x:2d} {x*x:3d} {x*x*x:4d}")
```

</details>




<details><summary> Clase_2_Secuencias_Funciones </summary><br>

#### Cargar una Lista desde teclado

```Python
def Ingresar(lista_de_notas:list[int]):
    nota = int(input("Ingresá una nota (-1 para finalizar)"))
    while nota != -1:
        lista_de_notas.append(nota)
        nota = int(input("Ingresá una nota (-1 para finalizar)"))
    return lista_de_notas

lista_de_notas:list[int] = []
lista_de_notas=Ingresar(lista_de_notas)
print(lista_de_notas)

```

``Las tuplas no se pueden modificar``

#### Cargar un Diccionario desde teclado

```Python
def ingreso_notas():
""" Esta función retorna un diccionario con los nombres y notas de estudiantes """
    nombre = input("Ingresa un nombre (<FIN> para finalizar)")
    dicci = {}
    while nombre != "FIN":
        nota = int(input(f"Ingresa la nota de {nombre}"))
        dicci[nombre] = nota
        nombre = input("Ingresa un nombre (<FIN> para finalizar)")
    return dicci
notas_de_estudiantes = ingreso_notas()
notas_de_estudiantes
```

#### Los parametros pueden tener valores por defecto

```Python
def mi_musica(dicci_musica, nombre, tipo_musica="nacional"):
    if nombre in dicci_musica:
        interpretes = dicci_musica[nombre]
        for elem in interpretes[tipo_musica]:
            print(elem)
    else:
    print(f"¡Hola {nombre}! No tenés registrada música en esta colección")
mi_musica(nombre="vivi", tipo_musica="internacional", dicci_musica=dicci_musica)
```

</details>


<details><summary> Clase_3_Argumentos_lambda </summary><br>
</details>


<details><summary> Clase_4_Archivos </summary><br>
</details>


<details><summary> Clase_5_Repaso_archivos </summary><br>
</details>


<details><summary> Clase_6_Excepciones </summary><br>
</details>


<details><summary> Clase_7_Intro_POO </summary><br>
</details>


<details><summary> Clase_8_Iteradores_y_excepciones </summary><br>
</details>


<details><summary> Clase_9_Intro_DS </summary><br>
</details>


<details><summary> Clase_10_Pandas_Copa_America </summary><br>
</details>


<details><summary> Clase_11_Intro_Testing </summary><br>
</details>


















