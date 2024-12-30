import pygame

from typing import Tuple, Dict

from src.agent import Agent

class Player(Agent):

  """
  Representa um player no jogo
  """

  def __init__(self, initial_position: Tuple[int, int], 
               controls: Dict[str, int],
               speed: float=1.5) -> None:

    super().__init__(initial_position, speed)

    self.controls = controls
  
  def move(self, delta_time: float) -> None:

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[self.controls["up"]]:

      self.y_direction = -1
    
    elif pressed_keys[self.controls["down"]]:

      self.y_direction = 1
    
    else:

      self.y_direction = 0
    
    self.y += 300 * self.speed * delta_time * self.y_direction
    