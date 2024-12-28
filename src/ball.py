import pygame

from typing import Tuple
import random

class Ball(pygame.Rect):

  """
  Representa o objeto bola (pequeno quadrado) do jogo
  """

  def __init__(self, initial_position: Tuple[int, int], speed: float=1.75) -> None:
    
    left, top = initial_position
    self.initial_position = initial_position
    self.speed = speed

    super().__init__(left, top, 15, 15)

    self.x_direction = random.choice([-1, 1])
    self.y_direction = 0
  
  def move(self, delta_time: int) -> None:

    self.x += 300 * self.speed * delta_time * self.x_direction
    self.y += 300 * self.speed * delta_time * self.y_direction
  
  def resetBall(self) -> None:

    self.__init__(self.initial_position)