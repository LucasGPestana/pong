import pygame

from typing import Tuple, Dict

class Player(pygame.Rect):

  """
  Representa um player (retangulo) do jogo
  """

  def __init__(self, initial_position: Tuple[int, int], 
               controls: Dict[str, int]) -> None:

    left, top = initial_position

    super().__init__(left, top, 15, 100)

    self.y_direction = 0 # Indica a direção em que o jogador está movendo no eixo y (-1 para cima, 0 parado e 1 para baixo)
    self.speed = 1.5

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
    