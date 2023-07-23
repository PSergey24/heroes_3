import math
import pygame

pygame.init()


class Settings:
    width: int = 1200
    height: int = 800
    start_battle_filed = [100, 140]
    n_columns: int = 15
    n_rows: int = 11
    R: int = 33
    r: float = round(math.sqrt(3) * R / 2, 2)
    bold: int = 1
    COLOR_BORDER = (128, 140, 64)
    COLOR_HOVER = (40, 40, 40, 120)
    COLOR_ACTIVE = (255, 215, 0)
    COLOR_POSSIBLE = (0, 0, 140, 60)
    FONT = pygame.font.Font('data/fonts/Times New Roman Bold.ttf', 12)
