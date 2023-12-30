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
        self.reset_states()
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

    @staticmethod
    def reset_states():
        States.hexagons = []
        States.queue = None
        States.step = 0
        States.round = 1

    def generate_units(self):
        self.left_team, self.right_team = self.game_generator.main()

    def create_units(self):
        self.unit_worker.create_units(self.left_team)
        self.unit_worker.create_units(self.right_team)

    def create_info_block(self):
        self.block_updater.create_info_block()

    def generate_move_order(self):
        States.queue = MyQueue(self.info_updater.generate_move_order(self.left_team, self.right_team))
        States.unit_active = States.queue.current[0]

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
            # self.block_updater.update_avatars()

    def play_step2(self, ai_move):
        reward, is_done = 0, False

        flag = True
        while len(States.animations) > 0 or flag:
            flag = False

            self.screen.blit(self.bg, (0, 0))

            for event in pygame.event.get():
                pass

            if len(States.animations) == 0:
                action, reward = self.action_matrix_worker.num_to_action(ai_move)
                self.update_button_info(action)
                self.update_unit_info(action)

            self.hex_worker.draw_hexagons(self.screen)
            self.unit_worker.draw_units(self.screen)

            pygame.display.update()

        if self.is_end_game() is True:
            reward, is_done = 1, True

        return reward, is_done, 0

    def play_step(self, ai_move):
        reward, is_done = 0, False

        action, reward = self.action_matrix_worker.num_to_action(ai_move)
        self.update_button_info(action)
        self.update_unit_info(action)

        if self.is_end_game() is True:
            reward, is_done = 1, True

        return reward, is_done, 0

    def get_state(self):
        states, masks = [], []

        for row in range(Settings.n_rows):
            for col in range(Settings.n_columns):
                x, y, z = self.hex_worker.offset2cube(row, col)
                is_close = 1 if ((row, col) in States.reachable_points and States.unit_active != States.hexagons[row][col].who_engaged) else 0

                masks.append(self.get_cell_mask(is_close, (x, y, z)))
                states.append(self.get_cell_state(is_close, row, col))

        return np.hstack(states), np.hstack(masks)

    def get_cell_mask(self, is_close, position):
        mask = [0] * 7

        if not is_close:
            return mask

        r, c = self.hex_worker.cube2offset(position[0], position[1], position[2])
        if States.hexagons[r][c].who_engaged is not None:
            return mask

        mask[6] = 1
        for i in range(6):
            neighbor = self.hex_worker.cube_neighbor((position[0], position[1], position[2]), i)
            r, c = self.hex_worker.cube2offset(neighbor[0], neighbor[1], neighbor[2])
            if 0 <= r < Settings.n_rows and 0 <= c < Settings.n_columns and States.hexagons[r][c].who_engaged is not None and States.hexagons[r][c].who_engaged.team != States.queue.current[0].team:
                mask[i] = 1

        return mask

    @staticmethod
    def get_cell_state(is_close, row, col):
        if not States.hexagons[row][col].who_engaged:
            return [1, is_close, 0, 0]
        else:
            if States.hexagons[row][col].who_engaged.team == States.queue.current[0].team:
                return [0, is_close, 1, 0]
            else:
                return [0, is_close, 0, 1]

    @staticmethod
    def is_end_game():
        return len({unit.team for unit in States.queue.current}) == 1


if __name__ == '__main__':
    game = GameAI()
    game.run()
