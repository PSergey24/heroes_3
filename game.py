import os
import pygame

from modules.settings import Settings
from modules.states import States, Objects

from modules.tools import Tools
from modules.cursor import Cursor
from modules.queue_ import Queue
from modules.field import Field
from modules.units import unit
from modules.active_unit import ActiveUnit
from modules.info_block import InfoBlock


class Game:

    def __init__(self):
        self.screen = None
        self.bg = None

        self.left_team = None
        self.right_team = None

        self.init()

    def init(self):
        self.create_window()
        self.create_game()

    def run(self):
        run = True

        while run:
            self.screen.blit(self.bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEMOTION and States.is_animate is False:
                    self.handle_motion()

                if event.type == pygame.MOUSEBUTTONDOWN and States.is_animate is False:
                    self.handle_click()

            self.draw_game()
            pygame.display.update()

            self.update_frame()
        pygame.quit()

    def create_window(self):
        window_size = (Settings.width, Settings.height)

        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Heroes III of might and magic')
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join("data/bg", "CmBkDrDd.bmp")), window_size)
        # self.bg = pygame.transform.scale(pygame.image.load(os.path.join("data/bg", "CmBkLvSt.bmp")), window_size)

    def create_game(self):
        self.create_workers()
        self.create_cursor()
        self.create_field()
        self.create_teams()
        self.create_queue()
        self.create_active_unit()
        self.create_info_block()

    @staticmethod
    def create_workers():
        Objects.tools = Tools()

    @staticmethod
    def create_cursor():
        Objects.cursor = Cursor()

    @staticmethod
    def create_field():
        Objects.field = Field()

    def create_teams(self):
        # self.left_team = [unit('nosfe', 3, 1, 35, 1), unit('nosfe', 8, 0, 267, 1), unit('devil', 7, 2, 1, 1)]
        # self.left_team = [unit('grelf', 3, 1, 327, 1), unit('nosfe', 4, 0, 30, 1), unit('ndrgn', 6, 0, 1, 1)]
        # self.left_team = [unit('chydr', 10, 9, 298, 1), unit('elf', 10, 13, 327, 1), unit('crusd', 7, 1, 7, 1)]
        # self.right_team = [unit('chydr', 5, 10, 427, 2), unit('crusd', 10, 11, 56, 2)]
        self.left_team = [unit('chydr', 10, 9, 298, 1), unit('pliza', 7, 5, 298, 1)]
        self.right_team = [unit('chydr', 5, 10, 427, 2)]

    def create_queue(self):
        Objects.queue = Queue(self.left_team, self.right_team)

    @staticmethod
    def create_active_unit():
        Objects.active_unit = ActiveUnit()

    @staticmethod
    def create_info_block():
        Objects.info_block = InfoBlock()

    @staticmethod
    def handle_motion():
        Objects.cursor.handle_motion()
        Objects.field.handle_motion()

    @staticmethod
    def handle_click():
        Objects.info_block.handle_click()
        Objects.cursor.handle_click()
        Objects.active_unit.handle_click()

    def update_frame(self):
        self.update_round_info()
        self.active_unit_update()
        self.info_block_update()
        self.units_update()

    @staticmethod
    def update_round_info():
        if not States.is_animate and len(Objects.queue.sequence) == States.step:
            Objects.queue.reset_queue()
            States.step = 0
            States.round += 1

    @staticmethod
    def active_unit_update():
        Objects.active_unit.update()

    @staticmethod
    def info_block_update():
        Objects.info_block.update()

    @staticmethod
    def units_update():
        States.is_animate = True if len(States.stack_animations) > 0 else False
        [unit_.update() for unit_ in Objects.queue.sequence]

    def draw_game(self):
        self.draw_cursor()
        self.draw_info_block()
        self.draw_field()
        self.draw_units()

    @staticmethod
    def draw_cursor():
        Objects.cursor.draw()

    def draw_info_block(self):
        Objects.info_block.draw(self.screen)

    def draw_field(self):
        Objects.field.draw(self.screen)

    def draw_units(self):
        [item.draw(self.screen) for item in sorted(Objects.queue.sequence, key=lambda x: x.hex[0][0], reverse=False)]


if __name__ == '__main__':
    game = Game()
    game.run()
