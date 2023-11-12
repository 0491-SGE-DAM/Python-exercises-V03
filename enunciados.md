# Enunciados ejercicios Python volumen III

## Consejos

 * No hace falta que compruebes que los datos que se proporcionan en los casos de prueba son correctos. Si se indica que se pasa un entero, se pasará un entero. Si se indica que será mayor o menor que algo, lo será.

* Puedes probar los casos de prueba redireccionando la entrada estándar 

> ```
>  python3 nombredelprograma.py < ficherocasodeprueba
> ``` 

* Tienes casos de prueba dentro de la carpeta _pruebas/test_cases_. Los resultados correctos de cada caso de prueba están en la carpeta _pruebas/result_.

## 001 Inventario

_Nivel_ [sin definir]

### Especificaciones

Crea un programa que permita la gestión del inventario de datos almacenados en diccionarios y listas. Para ello el programa deberá proporcionar funciones que realicen las siguientes tareas

1. Función: _create_inventary(items)_. Crea un diccionario que haga las veces de inventario

    - **Entrada**: lista -> ["agua", "pan", "leche", "agua", "leche", "cereales", "agua"]
    - **Salida**: diccionario -> { "agua": 3, "pan":1, "leche": 2, "cereales": 1}

2. Función: _add_items(inventary, items)_. Añade una listas de elementos al inventario

    - **Entrada**: inventary -> { "agua": 3, "pan":1, "leche": 2, "cereales": 1}, ["agua", "pan"]
    - **Salida**: items -> { "agua": 4, "pan":2, "leche": 2, "cereales": 1}, 

3. Función: _reduce_items(inventary, items)_. Reduce el inventario según los elementos de una lista.

    - **Entrada**: inventary -> { "agua": 3, "pan":1, "leche": 2, "cereales": 1}, ["agua", "pan"]
    - **Salida**: items -> { "agua": 2, "pan": 1, "leche": 2, "cereales": 1}, 

4. Función: _remove_item(inventary, item)_. Elimina un elemento del inventario

    - **Entrada**: { "agua": 3, "pan":1, "leche": 2, "cereales": 1}, "agua"
    - **Salida**: { "pan": 1, "leche": 2, "cereales": 1}, 

5. Función: _show_inventario(inventary)_. Muestra una lista de tuplas item, siempre que el numero de elementos en el inventario sea mayor de 0

    - **Entrada**: { "agua": 3, "pan":1, "leche": 2, "cereales": 1, "salchichon": 0}, 
    - **Salida**:  [("agua", 3), ("pan", 1), ("leche", 2), ("cereales", 1)]


## 002 Bodega

_Nivel_ [sin definir]

El objetivo es crear una pequeña aplicación que permita visualizar el estado actual de una bodega. Para ello es necesario crear 1 módulo denominado _ges_bodega_, que incluya los cuatro elementos básicos con los que se va a trabajar: la _bodega_, la _sala_, la _estantería_ y por último las _botella_.

Una bodega está compuesta de diferentes salas en las que en su interior habrá diferentes estanterías que contendrán botellas.

### Especificaciones

#### Bodega 

  1. Tiene como elementos fundamentales su nombre y un conjunto de salas.
  2. Debe incluir un método para añadir salas: _add_sala(sala)_
  3. Debe incluir una función de asignación de una botella en una estantería: _asigna_botella_en_estanteria(botella)_ La asignaciónn se realizará de manera secuencial: primer hueco adecuado que se encuentre.
  4. La salida de su valor como cadena debe mostrar el estado completo de la bodega tal y como se muestra en el caso de ejemplo
 
#### Sala

  1. Tiene como características un nombre, una temperatura y humedad actual y un conjunto de estanterias. 
  2. Debe incluir una función que permita añadir estanterías: _add_estanteria(estanteria)_
  3. Debe incluir una función que muestre el estado de temperatura y humedad actual tal y como se muestra en el ejemplo _imprime_estado()_
  4. Debe tener dos funciones que permitan registrar la temperatura y humedad actual: _registrar_temperatura( temperatura)_, _registrar_humedad(humedad)_
  5. Debe ser posible consultar cuál es la temperatura máxima y mínima alcanzada en **teniendo en cuenta todas las salas**.
  6. La salida de su valor como cadena debe mostrar el estado completo de la sala, con sus estanterias y su temperatura y humedad actuales, tal y como se muestra en el caso de ejemplo

#### Estanteria

  1. Existen 4 tipos de tamaños de estantería, definidos por una enumeración: CUADRADA_T1 = 0, CUADRADA_T2 = 1, RECTANGULAR_T1 = 2, RECTANGULAR_T2 = 3
  2. Los tamaños de celdas que tiene cada una de ellas son: CUADRADA_T1 = 3x3, CUADRADA_T2 = 4x4, RECTANGULAR_T1 = 3x4, RECTANGULAR_T2 = 4x5
  3. Cada estantería se define por la sala en la que está, su tamaño y el tamaño de la botella que puede almacenar. El tamaño de botella que almacena va en función de la forma, de manera que todas almacenan botellas pequeñas salvo la CUADRADA_T1 que almacena medianas y la RECTANGULAR_T1 que almacena grandes.
  4. Cada estantería tiene un código formado por la letra E seguida de 3 números que indican su número de orden, por ejemplo _E004_. Los números se asignan secuencialmente cuando se crean las estanterías, empezando por el 1.
  5. Debe de incluir una función que se encargue de colocar botellas en la estantería _coloca_botella(botella: Botella) -> bool_. Devuelve _True_ o _False_ si se ha podido colocar o no.
  6. Debe mostrar su ocupación mediante un diagrama como el mostrado en el ejemplo.
  7. La salida de su valor como cadena debe mostrar la palabra _Estanteria_ junto con el código de la estanteria y su tamaño XxY, por ejemplo: _Estantería E004 4x5_

#### Botella

  1. Existen 4 tipos de tamaños de botella, definidos por una enumeración: _SIN_DEFINIR = 0_, _GRANDE = 1_, _MEDIANA = 2_, _PEQUENYA = 3_
  2. Existen 5 tipos de vino, definidos por una enumeración: _TINTO = 0_,  _ROSADO = 1_, _BLANCO = 2_,  _VERDEJO = 3_, _DULCE = 4_. Su conversión en cadena tiene que porporcionar únicamente la primera letra del nombre, por ejemplo, de TINTO => T
  3. Cada botella debe almacenar la estantería y la posición en la que se encuentra, así como el tipo de vino que almacena.
  4. Para cada tamaño de botella debe existir una clase que la defina: _BotellaPeq_, _BotellaMed_, _BotellaGran_
  5. Cada botella tiene un código formado por la letra B seguida de 3 números que indican su número de orden, más una letra P,M,G según su tamaño y el tipo de vino, por ejemplo _B001PT_. Los números se asignan secuencialmente cuando se crean las botellas, empezando por el 1.
  6. La salida de su valor como cadena debe mostrar el código de la botella.
  7. Una botella será pequeña si su tamaño es menor de 33, mediana si es menor de 66 y en caso contrario será grande.
  
**Entrada**

- N,NS: 
    * N: Nombre de la bodega 
    * NS: Número de salas

- Por cada sala:

  * N,H,T,ECT1,ECT2,ERT1,ERT2:

     * N: Nombre de la sala 
     * H: humedad relativa
     * T: Temperatura
     * ECT1: número de estanterias CUADRADA_T1
     * ECT2: número de estanterias CUADRADA_T2
     * ERT1: número de estanterias RECTANGULAR_T1
     * ERT2: número de estanterias RECTANGULAR_T2

- NB: Número de botellas

- Por cada botella:
 
  * TAM,TV:
  
    *  TAM: Tamaño de la botella
    *  TV: Tipo de vino 0 <= TV <= 4 

**Salida**

Información completa de la bodega. Ver ejemplo

### Ejemplos

<br>

> **Entrada**

```
Mi bodega,2
001,65,16,1,0,1,0
002,95,19,0,1,0,1
2
12,0
56,4
```

> **Salida**

```
botella B001PT asignada a: Estantería E003 4x4 1x1
botella B002MD asignada a: Estantería E001 3x3 1x1
                      BODEGA Mi bodega                      
============================================================
                          SALA 001                          
-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                   Temperatura actual: 16                   
                   Humedad actual    : 65                   
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Estantería E001 3x3
+-+-+-+
|D| | |
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+

Estantería E002 3x4
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+
| | | |
+-+-+-+
                          SALA 002                          
-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                   Temperatura actual: 19                   
                   Humedad actual    : 95                   
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Estantería E003 4x4
+-+-+-+-+
|T| | | |
+-+-+-+-+
| | | | |
+-+-+-+-+
| | | | |
+-+-+-+-+
| | | | |
+-+-+-+-+

Estantería E004 4x5
+-+-+-+-+
| | | | |
+-+-+-+-+
| | | | |
+-+-+-+-+
| | | | |
+-+-+-+-+
| | | | |
+-+-+-+-+
| | | | |
+-+-+-+-+
############################################################
                 Temperatura min/max: 16/19                 
                 Humedad min/max    : 65/95                 
############################################################
``` 


<hr>
