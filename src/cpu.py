import pygame

from typing import Tuple, Dict

from src.agent import Agent

class CPU(Agent):

  """
  Representa um agente controlado pela cpu no jogo
  """

  def __init__(self, initial_position: Tuple[int, int], 
               speed: float) -> None:

    super().__init__(initial_position, speed)
  
  def move(self, delta_time: float,
           y_ball: int,
           ball_y_direction: int) -> None:

    self.y_direction = ball_y_direction

    # Para siutações em que a bola está fora da area de colisão do agente
    if not y_ball in range(self.y, self.y + self.height):

      if y_ball < self.y:

        self.y_direction = -1
      
      else:

        self.y_direction = 1
    
    self.y += 300 * self.speed * delta_time * self.y_direction
    