from enum import Enum
from .botella import TipoBotella, Botella

class FormaEstanteria(Enum):
  CUADRADA_T1 = 0
  CUADRADA_T2 = 1
  RECTANGULAR_T1 = 2
  RECTANGULAR_T2 = 3

class Estanteria: 
  """
  Clase que implementa una estanteria de una sala. Puede ser de varios tamaños 
  y almacena un tipo de botella. Además tiene un tipo asignado
  """

  # los tamños son comunes a todas las estanterías
  tamanosEstanteria = {
    FormaEstanteria.CUADRADA_T1.value: (3,3),
    FormaEstanteria.CUADRADA_T2.value: (4,4),
    FormaEstanteria.RECTANGULAR_T1.value: (3,4),
    FormaEstanteria.RECTANGULAR_T2.value: (4,5),
  }

  numero_estanterias = 0
  
  def __init__(self, sala, forma = FormaEstanteria.CUADRADA_T1, tipo = TipoBotella.SIN_DEFINIR):
    # otra forma de acceder a la variable de clase
    __class__.numero_estanterias = self.numero_estanterias + 1

    self.codigo = f'E{self.numero_estanterias:03d}'
    self.columnas = self.tamanosEstanteria[forma.value][0]
    self.filas = self.tamanosEstanteria[forma.value][1]
    self.tipo = tipo
    self.sala = sala
    self.distribucion = ' ' * self.filas * self.columnas

  def __str__(self):
    return f"Estantería {self.codigo} {self.columnas}x{self.filas}"
  
  def esta_llena(self) -> bool:
    """
    Devuelve True o False si la estanteria está llena o no
    """
    if self.distribucion.find(' ') == -1:
      return True
    
    return False
  
  def coloca_botella(self, botella: Botella) -> bool:
    """
    Coloca una botella en la estanteria.
    Devuelve True si puede o False en caso contrario
    """
    if self.esta_llena():
      return False
    
    if botella.tamanyo != self.tipo:
      return False
    
    pos = self.distribucion.find(' ') 
    vino_botella = f'{botella}'
    self.distribucion = self.distribucion.replace(' ', vino_botella[-1], 1)
    botella.estanteria = self
    botella.fila = pos // self.columnas + 1
    botella.columna = pos - self.columnas * (pos // self.columnas) + 1

    return True 

  def imprime_ocupacion(self):
    """
    Imprime una tabla con la ocuipacion de la estantería, poniendo una T,R,B,V en funciín del tipo 
    de vino de la botella
    """
    ocupacion = ''

    for f in range(self.filas):
      ocupacion += '+-'*self.columnas +'+\n' 

      for c in range(self.columnas):  
        ocupacion += f'|{self.distribucion[f*self.columnas+c:(f*self.columnas+c+1)]}'

      ocupacion += '|\n'
    
    ocupacion += '+-'*self.columnas + '+'

    return ocupacion

  @classmethod
  def creaEstanteria(cls,sala, forma):
    """
    Factoria que crea las estantería asignándoles también el tamaño de botella que almacenan
    Como es necesaria la clase Estanteria opto por un método de clase
    """
    if forma == FormaEstanteria.CUADRADA_T1:
      return cls(sala, forma, TipoBotella.MEDIANA)
    if forma == FormaEstanteria.RECTANGULAR_T1:
      return cls(sala, forma, TipoBotella.GRANDE)
    
    return cls(sala, forma, TipoBotella.PEQUENYA)
    