import os
import pygame

from modules.settings import Settings, States
from modules.my_queue import MyQueue
from modules.units import unit
from modules.hex_worker import HexWorker
from modules.unit_worker import UnitWorker
from modules.info_updater import InfoUpdater
from modules.block_updater import BlockUpdater


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((Settings.width, Settings.height))
        self.bg = pygame.image.load(os.path.join("data/bg", "CmBkDrDd.bmp"))
        self.bg = pygame.transform.scale(self.bg, (Settings.width, Settings.height))

        self.left_team = [unit('gdrag', 6, 7, 3, 1), unit('plich', 4, 5, 73, 1), unit('plich', 4, 7, 73, 1), unit('harpy', 5, 9, 53, 1)]
        self.right_team = [unit('lich', 6, 10, 3, 2), unit('hydra', 7, 10, 3, 2)]

        self.hex_worker = HexWorker()
        self.unit_worker = UnitWorker()
        self.info_updater = InfoUpdater()
        self.block_updater = BlockUpdater()

    def run(self):
        run = True

        self.screen.blit(self.bg, (0, 0))

        self.create_cursor()
        self.hex_worker.create_hexagons()
        self.create_units()
        self.generate_move_order()
        self.create_info_block()

        while run:
            self.screen.blit(self.bg, (0, 0))

            self.update_round_info()
            self.info_updater.update_step_info()
            self.update_buttons()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEMOTION and States.is_animate is False:
                    States.point_over = pygame.mouse.get_pos()

                    self.hex_worker.update_point_over()
                    self.hex_worker.update_cursor()
                    self.hex_worker.update_hexagons()

                if event.type == pygame.MOUSEBUTTONDOWN and States.is_animate is False:
                    self.block_updater.update_buttons_by_click()

                    if action := self.hex_worker.get_move_type():
                        self.update_unit_info(action)

            self.draw_cursor()
            self.draw_info_block()
            self.hex_worker.draw_hexagons(self.screen)
            self.unit_worker.draw_units(self.screen)

            pygame.display.update()
        pygame.quit()

    @staticmethod
    def create_cursor():
        States.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom000.png"))
        pygame.mouse.set_cursor(pygame.cursors.Cursor((0, 0), States.cursor))

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
    game = Game()
    game.run()
