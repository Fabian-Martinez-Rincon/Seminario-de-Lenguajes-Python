# 2da Defensa 

## `Carpetas`

### Analysis_section

Contiene el analisis y estadisticas de los eventos obtenidos del juevo.

### Dataset_section

Contiene el procesamiento de los datasets, junto con los datasets modificados
### Documentos

Como registros y objetivos junto con los enunciados

### Typings

Contiene las importaciones necesarias para que funciones pySimpleGui

# SRC/ORIGEN

### \_\_init__

¿Porque esta vacia?

Hace que la carpeta src se comporte como un módulo

Por el simple hecho de existir

Ej:  `import SRC from constants.py`


- ### Constans

Contiene constantes globales de la aplicación.
Como todas las rutas por donde nos manejamos en el juego y el nombre de todos los eventos que vamos a manejar

- ### Controllers

Controladores consumidos en la aplicación para administrar y acceder a estados


---




- `set()` Genera un objeto iterable (para cualquier tipo de dato) si es un string lo genera random y en si son nros los genera ordenados

- `@property` Es un decorador que viene por defecto con Python, y puede ser usado para modificar un método para que sea un atributo o propiedad.

- `*bads` Eje:  event_type, *event_data = event.split() Empaqueta todos los datos

Ej `[1,4,5,6,8,9]`

En event_type me quedo con el `1` y en *event_data, me quedo coin todo el resto

- `@type.setter`

- `Any` Tipo especial que indica un tipo sin restricciones. Todos los tipos son compatibles con Any y este es compatible con todos los tipos


- `Callable`

- `observer`  es un patrón de diseño de comportamiento que permite que algunos objetos notifiquen a otros objetos sobre cambios en su estado. Proporciona una forma de reaccionar a los eventos que suceden en otros objetos sin acoplarse a sus clases.

- `@dataclass` Este módulo proporciona un decorador y funciones para agregar automáticamente métodos especiales generados como \_\_init__() a clases definidas por el usuario. El decorador devuelve la misma clase, no crea ninguna nueva


- `copy` Las declaraciones de asignación en Python no copian objetos, crean enlaces entre un objetivo y un objeto. A veces se necesita una copia para poder cambiar una copia sin cambiar la otra.

- `jsonify` una muestral json 

- ```Python 
    self._difficulties = {        
    name: Difficulty(**definition) for name, definition in raw_difficulties.items()
    }
    ```

Desempaca un diccionario en clave y valor

---

# Nuevo

### Pantalla de Puntajes

- Run_event
- Default
- Carpeta events

### run_event

- `uuid` (Para generar una id unica)
- `enum` Seleccionar tipos de datos como si fueran constantes. 

```Python
class EventNames(Enum):
    START = 'inicio_partida'
    TRY = 'intento'
    END = 'fin'
```
Porque podemos hacer lo siguiente

```python
print(EventNames.START)
#EventName.START
```
Esto nos sirve para comprobar que el usuario halla presionado START

```Py
if event_data['name'] == EventNames.START:
```

Sin necesidad de crear un constructor directamente apuntando a esta variable


Por que se usa el `.value`? (Linea 61) `event_data['name'].value`

Porque nos queremos quedar con el valor, no con el nombre, que en el ejemplo de arriba seria `¿inicio_partida?`

Por que accedemos usando el `.get`? (Linea 62) 

`event_data.get('state', EventStates.DEFAULT).value`

Porque en el caso de que no tenga valores la clave (key), retornamos valores por defecto.

Pregunta si existe `state` y sino, retorna el DEFAULT


`¿Inicializar en una ventana puntual?`