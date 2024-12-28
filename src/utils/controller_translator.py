from typing import Dict


import pygame as pg

def translateControls(controls: Dict[str, str]) -> Dict[str, int]:

  # Mapeando as teclas dos arquivos .json de controles para o valor correspondente da tecla no pygame
  unicode_codepoints = list(range(48, 58)) + list(range(97, 123))
  control_mapping = {chr(codepoint): codepoint for codepoint in unicode_codepoints}

  for key_name, key_code in [("up", pg.K_UP), ("down", pg.K_DOWN), 
                             ("left", pg.K_LEFT), ("right", pg.K_RIGHT)]:
    
    control_mapping[key_name] = key_code

  for command, key in controls.items():

    controls[command] = control_mapping.get(key.lower(), None)
  
  return controls