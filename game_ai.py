import os
import pygame

from modules.settings import Settings
from modules.states import States, Objects

from modules.tools import Tools
from modules.damage_counter import DamageCounter
from modules.queue_ import Queue
from modules.field import Field
from modules.units import unit
from modules.active_unit import ActiveUnit


class GameAI:

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

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         run = False

            self.draw_game()
            pygame.display.update()

            self.update_frame()
        pygame.quit()

    def create_window(self):
        window_size = (Settings.width, Settings.height)

        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Heroes III of might and magic')
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join("data/bg", "CmBkDrDd.bmp")), window_size)

    def create_game(self):
        self.create_workers()
        self.create_field()
        self.create_teams()
        self.create_queue()
        self.create_active_unit()

    @staticmethod
    def create_workers():
        Objects.tools = Tools()
        Objects.damage_counter = DamageCounter()

    @staticmethod
    def create_field():
        Objects.field = Field()

    def create_teams(self):
        self.left_team = [unit('magog', 4, 1, 45, 1), unit('magel', 8, 1, 15, 1)]
        self.right_team = [unit('sgole', 6, 12, 20, 2), unit('grelf', 9, 12, 38, 2)]

    def create_queue(self):
        Objects.queue = Queue(self.left_team, self.right_team)

    @staticmethod
    def create_active_unit():
        Objects.active_unit = ActiveUnit()

    def update_frame(self):
        self.update_round_info()
        self.active_unit_update()
        self.field_update()
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
    def field_update():
        Objects.field.field_update()

    @staticmethod
    def units_update():
        def is_animate():
            for unit_ in Objects.queue.sequence:
                if unit_.current_animation != "standing" or len(unit_.next_actions) > 0:
                    return True
            return False

        [unit_.update() for unit_ in Objects.queue.sequence + Objects.queue.dead_units]
        States.is_animate = is_animate()

    def draw_game(self):
        self.draw_field()
        self.draw_units()

    def draw_field(self):
        Objects.field.draw(self.screen)

    def draw_units(self):
        [item.draw(self.screen) for item in sorted(Objects.queue.dead_units + Objects.queue.sequence, key=lambda x: x.hex[0][0], reverse=False)]


class GameAI2:

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
