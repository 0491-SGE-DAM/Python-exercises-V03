from .estanteria import Estanteria

class Sala:
  """
  Implementa un sala, con una temperatura y humedad y un numoer de estanterias
  """
  # valores miembors de la clase, ya que son comunes para todos los objetos
  humedad_maxima = 0    # en %
  humedad_minima = 100  # en %

  temperatura_maxima = -100   # en º
  temperatura_minima = 100  # en º

  # Lo lógico sería definir la temperatura y humedad actual, pero no lo defino 
  # para poder comprbar que no es necesario declarar las varialbes del objeto en el constructor
  def __init__(self, nombre: str):
    self.nombre = nombre
    self.estanterias = []

  def __str__(self):
    """
    Sobreescribe el método str para mostrar el estado actual de la sala
    """
    cabecera = f'SALA {self.nombre}'
    cabecera_centrada = f'{cabecera:^60}\n'+'-.'*30
    
    estanteria_des = ''
    for estanteria in self.estanterias:
      estanteria_des += f'\n{estanteria}\n'
      estanteria_des += estanteria.imprime_ocupacion()
      estanteria_des += '\n'

    return cabecera_centrada + '\n' + \
      self.imprime_estado() + \
      estanteria_des
  
  def add_estanteria(self, estanteria: Estanteria) -> None:
    """Añade una estantería a la sala"""
    self.estanterias.append(estanteria)
    
  def imprime_estado(self) -> str:
    """
    Devuelve una cadena que muestra la temperatura y humedad actuales
    """
    franja = ':'*60
    temp = f'Temperatura actual: {self.temperatura_actual}'
    humedad = f'Humedad actual    : {self.humedad_actual}'
    return  f'{franja}\n{temp:^60}\n{humedad:^60}\n{franja}'

  def registrar_temperatura(self, temperatura: int):
    """Permite definir la temperatura actual de la sala"""
    self.temperatura_actual = temperatura
    Sala.calcula_temperatura_maxmin(temperatura)    # puedo acceder desde la clase

  def registrar_humedad(self, humedad: int):
    """Permite definir la humedad actual de la sala"""
    self.humedad_actual = humedad 
    self.calcula_humedad_maxmin(humedad)    # puedo acceder desde la instancia

  @classmethod
  def calcula_temperatura_maxmin(cls, temperatura: int):
    """Recalcula la temperatura máxima y minima"""
    if temperatura > cls.temperatura_maxima:
      cls.temperatura_maxima = temperatura
    if temperatura < cls.temperatura_minima:
      cls.temperatura_minima = temperatura

  @classmethod
  def calcula_humedad_maxmin(cls, humedad: int):
    """Recalcula la humedad máxima y minima"""
    if humedad > cls.humedad_maxima:
      cls.humedad_maxima = humedad
    if humedad < cls.humedad_minima:
      cls.humedad_minima = humedad

  @classmethod
  def imprime_estado_actual(cls) -> str:
    """
    Devuelve una cadena con la información de temperatura y humedad de todas las salas
    """
    franja = '#'*60
    temp = f'Temperatura min/max: {cls.temperatura_minima}/{cls.temperatura_maxima}'
    humedad = f'Humedad min/max    : {cls.humedad_minima}/{cls.humedad_maxima}'

    return  f'{franja}\n{temp:^60}\n{humedad:^60}\n{franja}'
  
