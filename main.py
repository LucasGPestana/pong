import pygame as pg

from src.player import Player
from src.cpu import CPU
from src.ball import Ball
from src.collision import Collision
from src.points import Points
from src.utils.controller_translator import translateControls

import json
import os
from typing import Dict, Any

def buildVictoryScreen(player_name: str, running: bool) -> bool:

    # Superfície transparente para o fundo
    overlay = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(128)
    overlay.fill((0, 0, 0))

    # Poe a superfície transparente no fundo
    screen.blit(overlay, (0, 0))

    message_text_surface = pg.Surface = font.render(f"{player_name} venceu!", 
                                                      True, 
                                                      (255, 255, 255), 
                                                      (0, 0, 0))
    message_text_surface_width = (SCREEN_WIDTH / 2) - (message_text_surface.get_width() / 2)
    message_text_surface_height = (SCREEN_HEIGHT / 2) - (message_text_surface.get_height() / 2)

    screen.blit(message_text_surface, (message_text_surface_width, message_text_surface_height))
    pg.display.flip()

    start_time = pg.time.get_ticks()
    current_time = pg.time.get_ticks()

    while current_time - start_time < 5000:

        for event in pg.event.get():

            if event.type == pg.QUIT:

                running = False
            
        if not running:

            break

        current_time = pg.time.get_ticks()

    running = False

    return running


pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Pong")
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

clock = pg.time.Clock()
running = True # Controla se o jogo está em execução ou não
delta_time = 0 # Diferença, em segundos, do tempo atual e o tempo de inicio do jogo

CONFIG_DIR = os.path.join(os.path.dirname(__file__), 
                            "config") # Diretório com os arquivos de controles de cada jogador

# Atributos do Player 1
position_player1 = (16, SCREEN_HEIGHT / 2)
controls_player1 = translateControls(json.load(open(os.path.join(CONFIG_DIR, 
                                          "p1_controls.json"), 'r')))

# Atributos do Player 2
position_player2 = (SCREEN_WIDTH - 28, SCREEN_HEIGHT / 2)
controls_player2 = translateControls(json.load(open(os.path.join(CONFIG_DIR, 
                                          "p2_controls.json"), 'r')))

# Configurações de jogo
game_config: Dict[str, Any] = json.load(open(os.path.join(CONFIG_DIR,
                                                          "game_config.json"), 'r'))
VICTORY_SCORE = game_config["victory_score"]
MODE = game_config["mode"]

position_ball = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

agent1 = Player(position_player1, controls_player1)

if MODE == "player_vs_cpu":

    cpu_config: Dict[str, Any] = json.load(open(os.path.join(CONFIG_DIR,
                                                          "cpu_config.json"), 'r'))
    CPU_SPEED = cpu_config["speed"]

    agent2 = CPU(position_player2, CPU_SPEED)

elif MODE == "player_vs_player":

    agent2 = Player(position_player2, controls_player2)

else:

    exit("Esse modo de jogo não é válido!")

ball = Ball(position_ball)

points = Points()

font = pg.font.Font(None, 64)

while running:

    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():

        if event.type == pg.QUIT:

            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 0, 0))

    score_text_surface: pg.Surface = font.render(f"{points.player1_points:^5} | {points.player2_points:^5}",
                                                 True, 
                                                 (255, 255, 255), 
                                                 (0, 0, 0))
    score_text_surface_width = (SCREEN_WIDTH / 2) - (score_text_surface.get_width() / 2)
    score_text_surface_height = 10
    
    screen.blit(score_text_surface, (score_text_surface_width, score_text_surface_height))

    pg.draw.rect(screen, (255, 255, 255), agent1, 15)
    pg.draw.rect(screen, (255, 255, 255), agent2, 15)
    pg.draw.rect(screen, (255, 255, 255), ball, 15)
        
    agent1.move(delta_time)

    if isinstance(agent2, Player):

        agent2.move(delta_time)
    
    else:

        agent2.move(delta_time, ball.y, ball.y_direction)

    ball.move(delta_time)

    Collision(ball, agent1).checkCollision()
    Collision(ball, agent2).checkCollision()
    player_pointed = Collision(ball, screen).checkCollision()
    Collision(agent1, screen).checkCollision()
    Collision(agent2, screen).checkCollision()

    match player_pointed:
    
        case 1:
        
            points.player1_points += 1
            ball.resetBall()

        case 2:
        
            points.player2_points += 1
            ball.resetBall()

        case _:

            pass
    
    if points.player1_points == VICTORY_SCORE:

        running = buildVictoryScreen("Player 1", running)
    
    if points.player2_points == VICTORY_SCORE:

        running = buildVictoryScreen("Player 2" if isinstance(agent2, Player) else "CPU", running)

    pg.display.flip()

    delta_time = clock.tick(60) / 1000

pg.quit()