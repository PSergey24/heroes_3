import os
import pygame

from modules.settings import Settings
from modules.states import States, Objects

from modules.tools import Tools
from modules.damage_counter import DamageCounter
from modules.cursor import Cursor
from modules.queue_ import Queue
from modules.field import Field
from modules.render.renderer import BattleRenderer
from modules.units import unit
from modules.active_unit import ActiveUnit
from modules.info_block import InfoBlock


class Game:

    def __init__(self):
        self.screen = None
        self.renderer = None
        self.init()

    def init(self):
        self.create_window()
        self.create_game()

    def run(self):
        run = True

        while run:
            self.renderer.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEMOTION and States.is_animate is False:
                    self.handle_motion()
                if event.type == pygame.MOUSEBUTTONDOWN and States.is_animate is False:
                    self.handle_click()

            self.update_frame()
            self.draw_game()
            pygame.display.update()
        pygame.quit()

    def create_window(self):
        window_size = (Settings.width, Settings.height)

        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Heroes III of might and magic')
        self.renderer = BattleRenderer(self.screen)
        self.renderer.load_background("CmBkDrDd.bmp")
        self.renderer.on_unit_move_complete = self.on_unit_move_complete

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
        Objects.damage_counter = DamageCounter()

    @staticmethod
    def create_cursor():
        Objects.cursor = Cursor()

    @staticmethod
    def create_field():
        Objects.field = Field()

    def create_teams(self):
        self.left_team = [unit('magog', 4, 2, 45, 1), unit('magel', 8, 8, 15, 1), unit('crusd', 7, 7, 25, 1)]
        self.right_team = [unit('ddrag', 5, 5, 1, 2), unit('skele', 6, 5, 120, 2), unit('grelf', 6, 4, 38, 2)]

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

    def on_unit_move_complete(self):
        pass

    def draw_game(self):
        self.renderer.draw_background()
        self.draw_cursor()
        self.draw_info_block()
        self.draw_field()
        self.draw_units()

    @staticmethod
    def draw_cursor():
        Objects.cursor.draw()

    def draw_field(self):
        self.renderer.draw_field(Objects.field)

    def draw_units(self):
        self.renderer.draw_units(Objects.queue.dead_units + Objects.queue.sequence)

    def update_animation_tick(self):
        pass

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
        if States.is_animate is not True:
            Objects.active_unit.update()

    @staticmethod
    def info_block_update():
        Objects.info_block.update()

    @staticmethod
    def units_update():
        def is_animate():
            for unit_ in Objects.queue.sequence:
                if unit_.current_animation != "standing" or len(unit_.next_actions) > 0:
                    return True
            return False

        [unit_.update() for unit_ in Objects.queue.sequence + Objects.queue.dead_units]
        States.is_animate = is_animate()

    


if __name__ == '__main__':
    game = Game()
    game.run()
