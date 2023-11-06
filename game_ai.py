import os
import pygame
import numpy as np

from modules.settings import Settings, States
from modules.my_queue import MyQueue
from modules.hex_worker import HexWorker
from modules.unit_worker import UnitWorker
from modules.info_updater import InfoUpdater
from modules.block_updater import BlockUpdater
from modules.damage_counter import DamageCounter
from modules.game_generator import GameGenerator
from modules.ai_action_worker import AIActionWorker


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
        self.action_matrix_worker = AIActionWorker()

        self.reset()

    def reset(self):
        self.screen.blit(self.bg, (0, 0))
        self.create_cursor()
        self.hex_worker.create_hexagons()
        self.generate_units()
        self.create_units()
        self.generate_move_order()
        self.create_info_block()

    def run(self):
        run = True

        while run:
            self.play_step([1, 0, 0])
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

    def update_button_info(self, action):
        if action == "wait":
            self.block_updater.update_wait_by_click()
        if action == "defend":
            self.block_updater.update_defend_by_click()

    def update_unit_info(self, action):
        if action not in [False, "wait", "defend"]:
            self.unit_worker.update_units(action)
            self.block_updater.update_avatars()

    def play_step(self, ai_move):
        flag = True
        while len(States.animations) > 0 or flag:
            flag = False

            self.screen.blit(self.bg, (0, 0))

            self.update_round_info()
            self.info_updater.update_step_info()

            for event in pygame.event.get():
                pass

            if len(States.animations) == 0:
                action, reward = self.action_matrix_worker.num_to_action(ai_move)
                self.update_button_info(action)
                self.update_unit_info(action)

            self.hex_worker.draw_hexagons(self.screen)
            self.unit_worker.draw_units(self.screen)

            pygame.display.update()

        return reward, False, 0

    @staticmethod
    def get_state():
        states = []
        for row in range(Settings.n_rows):
            for col in range(Settings.n_columns):
                if not States.hexagons[row][col].who_engaged:
                    states.append([1, 0, 0])
                else:
                    if States.hexagons[row][col].who_engaged.team == States.queue.current[0].team:
                        states.append([0, 1, 0])
                    else:
                        states.append([0, 0, 1])
        return np.hstack(states).tolist()


if __name__ == '__main__':
    game = GameAI()
    game.run()
