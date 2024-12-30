import pygame as pg

from typing import Tuple


class Agent(pg.Rect):

  """
  Representa um agente no jogo, o qual pode ser um player ou cpu
  """

  def __init__(self, initial_position: Tuple[int, int],
               speed: float=1.5) -> None:

    left, top = initial_position

    super().__init__(left, top, 15, 100)

    self.y_direction = 0 # Indica a direção em que o agente está movendo no eixo y (-1 para cima, 0 parado e 1 para baixo)
    self.speed = speed
  
  def move(self):

    pass