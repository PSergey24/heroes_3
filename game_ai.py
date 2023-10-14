import os
import pygame

from modules.settings import Settings, States
from modules.my_queue import MyQueue
from modules.units import unit
from modules.hex_worker import HexWorker
from modules.unit_worker import UnitWorker
from modules.info_updater import InfoUpdater
from modules.block_updater import BlockUpdater
from modules.damage_counter import DamageCounter
from modules.game_generator import GameGenerator


class GameAI:

    def __init__(self):
        self.screen = pygame.display.set_mode((Settings.width, Settings.height))
        self.bg = pygame.image.load(os.path.join("data/bg", "CmBkDrDd.bmp"))
        self.bg = pygame.transform.scale(self.bg, (Settings.width, Settings.height))

        self.left_team = None
        self.right_team = None

        self.hex_worker = HexWorker()
        self.unit_worker = UnitWorker()
        self.info_updater = InfoUpdater()
        self.block_updater = BlockUpdater()
        self.damage_counter = DamageCounter()
        self.game_generator = GameGenerator()

    def run(self):
        run = True

        self.screen.blit(self.bg, (0, 0))

        self.create_cursor()
        self.hex_worker.create_hexagons()
        self.generate_units()
        self.create_units()
        self.generate_move_order()
        self.create_info_block()

        while run:
            self.screen.blit(self.bg, (0, 0))

            self.update_round_info()
            self.info_updater.update_step_info()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                # self.update_unit_info(action)

            self.draw_info_block()
            self.hex_worker.draw_hexagons(self.screen)
            self.unit_worker.draw_units(self.screen)

            pygame.display.update()
        pygame.quit()

    @staticmethod
    def create_cursor():
        States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom000.png"))
        pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), States.cursor))

    def generate_units(self):
        self.left_team, self.right_team = self.game_generator.main()

    def create_units(self):
        self.unit_worker.create_units(self.left_team)
        self.unit_worker.create_units(self.right_team)

    def create_info_block(self):
        self.block_updater.create_info_block()

    def generate_move_order(self):
        States.queue = MyQueue(self.info_updater.generate_move_order(self.left_team, self.right_team))

    def update_round_info(self):
        if not States.is_animate and len(States.queue.current) == States.step:
            States.queue.update_queue()
            self.info_updater.update_steps()
            self.info_updater.update_rounds()

    def update_buttons(self):
        self.block_updater.update_buttons()

    def update_unit_info(self, action):
        self.unit_worker.update_units(action)
        self.block_updater.update_avatars()

    @staticmethod
    def draw_cursor():
        pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), States.cursor))

    def draw_info_block(self):
        def draw_child(parent):
            for child in parent.children:
                draw_child(child)
                if child.parent is not None:
                    child.draw()

        draw_child(States.main)
        self.screen.blit(States.main.surf, States.main.rect)


if __name__ == '__main__':
    game = GameAI()
    game.run()
