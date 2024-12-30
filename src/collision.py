from pygame import Surface

from src.ball import Ball
from src.agent import Agent

from typing import Union

class Collision:

  def __init__(self, obj1: Union[Ball, Agent], obj2: Union[Agent, Surface]) -> None:

    self.obj1 = obj1
    self.obj2 = obj2
  
  def checkCollision(self) -> int:

    """
    Verifica se há uma colisão entre os objeto, e trata situação por situação. Se ocorrer colisão no eixo x entre a bola e a tela, será retornado um número correspondente ao jogador que fez ponto. Caso contrário, o valor retornado é 0.
    """

    if isinstance(self.obj1, Ball):

      if isinstance(self.obj2, Agent):
          
        if abs(self.obj1.x - self.obj2.x) <= self.obj2.width and self.obj2.y <= self.obj1.y and self.obj2.y + self.obj2.height >= self.obj1.y:
          
          self.obj1.y_direction = self.obj2.y_direction
          self.obj1.x_direction *= -1
          print("Colisão bola e player")
        
      elif isinstance(self.obj2, Surface):
        
        # Deixa uma folga de 10 pixels para que ocorra a colisão em y
        if 10 > self.obj1.y or self.obj2.get_height() - 10 < self.obj1.y:

          self.obj1.y_direction *= -1
          print("Colisão bola e tela")
        
        if self.obj1.x <= 0:

          print("Ponto do Jogador 2!")
          return 2
        
        if self.obj1.x >= self.obj2.get_width():

          print("Ponto do Jogador 1!")
          return 1
      
      else:

        pass
    
    if isinstance(self.obj1, Agent) and isinstance(self.obj2, Surface):
       
       if self.obj1.y < 10 or self.obj1.y + self.obj1.height > self.obj2.get_height() - 10:
         
          self.obj1.y += 20 * self.obj1.y_direction * -1 # Movimenta o jogador 20 pixels, na direção contrária ao do movimento atual, em y
    
    return 0