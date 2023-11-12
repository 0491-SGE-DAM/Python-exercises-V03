from .sala import Sala

class Bodega:
  """
  Implementa una bodega
  Tiene como datos el nombre y las salas
  """  
  def __init__(self, nombre):
    self.nombre = nombre 
    self.salas = []  
 
  def __str__(self):
    """
    Sobreescribe el método str para mostrar el estado actual de la bodega
    """

    cabecera = f'BODEGA {self.nombre}'
    cabecera_centrada = f'{cabecera:^60}\n'+'='*60
   
    sala_des = ''
    for sala in self.salas:
      sala_des += f'{sala}'

    return cabecera_centrada + '\n' + sala_des + Sala.imprime_estado_actual()
  
  def add_sala(self, sala):
    """ Añade una sala a la bodega"""
    self.salas.append(sala)
  
  def asigna_botella_en_estanteria(self, botella) -> bool:
    """
    Asigna un lugar en una estanteria a una botella
    Devuelve True si la puede colocar o False en caso contrario
    """
    for sala in self.salas:
      for est in sala.estanterias:
        # si la estanteria no es del tamaño de la botella
        if est.tipo != botella.tamanyo:
          continue
         # si la estanteria está llena
        elif est.esta_llena() == True:
          continue
        else:
          # coloca loa botella
          if not est.coloca_botella(botella):
            continue
          else:
            return True

    return False