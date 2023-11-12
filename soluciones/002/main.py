#!/usr/bin/python3
import ges_bodega as gb

# lectura fila 1 del fichero: nombre bodega y número de salas
datos_bodega = input().split(',')
bodega = gb.Bodega(datos_bodega[0])

# lectura de las salas 
for sala in range(int(datos_bodega[1])):
  datos_sala = input().split(',')

  sala = gb.Sala(datos_sala[0])

  # obtención de temp y humedad
  sala.registrar_humedad(int(datos_sala[1]))
  sala.registrar_temperatura(int(datos_sala[2]))

  # creación de las estanterias
  # enumerate devuelve dos valores: el contador de la iteración y el valor
  for idx, te in enumerate(datos_sala[3:]): 
    for e in range(int(te)):
      sala.add_estanteria(gb.Estanteria.creaEstanteria(sala, gb.FormaEstanteria(idx)))

  bodega.add_sala(sala)

# creación de las botellas
num_botellas = int(input())
for _ in range(num_botellas):
  datos_botella = input().split(',')
  botella = gb.Botella.creaBotella(int(datos_botella[1]), int(datos_botella[0]))
 
  if bodega.asigna_botella_en_estanteria(botella):
    print(f'botella {botella} asignada a: {botella.estanteria} {botella.columna}x{botella.fila}')
  else:
    print(f'botella {botella} no puede asignarse')

# impresión final
print(bodega)