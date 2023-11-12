from enum import Enum

class TipoBotella(Enum):
  SIN_DEFINIR = 0
  GRANDE = 1
  MEDIANA = 2
  PEQUENYA = 3

  def __str__(self):
    return self.name[0]
  
class TipoVino(Enum):
  TINTO = 0
  ROSADO = 1
  BLANCO = 2
  VERDEJO = 3
  DULCE = 4

  def __str__(self):
    return self.name[0]

class Botella:
  """
  Implementa un botella, definiendo el tipo vino que almacena
  Además guarda información del código y de en qué estanteria y cual es su posición"""

  tamanyo = TipoBotella.SIN_DEFINIR
  numero_botellas = 0     #contador para genberar el código
  
  def __init__(self, tipo_vino = TipoVino.TINTO):
    __class__.numero_botellas = self.numero_botellas + 1

    # En principio no está asignada a ninguna estanteria  
    self.estanteria = None
    self.fila = None
    self.columna = None  

    self.tipo_vino = tipo_vino
    self.code = f'B{self.numero_botellas:03d}'

  def __str__(self):
    return self.code
  
  @staticmethod
  def creaBotella(tipo_vino,tamanyo):
    """
    Factoria para crear botellas en función del tamaño.
    Como no es necesaria la clase Botella opto por un método estático
    """
    if tamanyo < 33:
      return BotellaPeq(TipoVino(tipo_vino))
    if tamanyo < 66:
      return BotellaMed(TipoVino(tipo_vino))
    else:
      return BotellaGran(TipoVino(tipo_vino))


class BotellaPeq(Botella):
  """
  Implementa una botella pequeña
  """
  tamanyo = TipoBotella.PEQUENYA

  def __init__(self,tipo_vino):
    super().__init__(tipo_vino)
    self.code += str(self.tamanyo) + str(self.tipo_vino)
  
class BotellaMed(Botella):
  """
  Implementa una botella mediana
  """
  tamanyo = TipoBotella.MEDIANA

  def __init__(self,tipo_vino):
    super().__init__(tipo_vino)
    self.code += str(self.tamanyo) + str(self.tipo_vino)
  
class BotellaGran(Botella):
  """
  Implementa una botella grande
  """
  tamanyo = TipoBotella.GRANDE

  def __init__(self,tipo_vino):
    super().__init__(tipo_vino)
    self.code += str(self.tamanyo) + str(self.tipo_vino)