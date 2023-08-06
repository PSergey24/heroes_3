import os
import pygame

from modules.settings import Settings, States
from modules.helper import Helper
from modules.info_updater import InfoUpdater
from modules.block_updater import BlockUpdater
from modules.queue import Queue
from unit import Lich, Mage


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((Settings.width, Settings.height))
        self.bg = pygame.image.load(os.path.join("data/bg", "CmBkDrDd.bmp"))
        self.bg = pygame.transform.scale(self.bg, (Settings.width, Settings.height))

        self.cursor = None
        self.divs = None

        self.left_team = [Lich(8, 3, 15, 1), Mage(2, 5, 6, 1)]
        self.right_team = [Lich(8, 6, 17, 2), Mage(2, 7, 3, 2)]

        self.helper = Helper()
        self.info_updater = InfoUpdater()
        self.block_updater = BlockUpdater()

        self.point_attack = None
        self.whom_attack = None

    def run(self):
        run = True

        self.screen.blit(self.bg, (0, 0))
        self.create_cursor()
        self.create_fields()
        self.create_characters()
        self.generate_move_order()
        self.create_info_block()

        while run:
            self.screen.blit(self.bg, (0, 0))
            self.reset_properties()
            self.update_cursor()
            self.update_buttons()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEMOTION and States.is_animate is False:
                    pos = pygame.mouse.get_pos()
                    if position := self.get_cell(pos):
                        self.update_cursor_info(position, pos)
                        self.update_fields_info(position)

                if event.type == pygame.MOUSEBUTTONDOWN and States.is_animate is False:
                    pos = pygame.mouse.get_pos()
                    self.update_buttons_by_click(pos)

                    if position := self.get_cell(pos):
                        if action := self.helper.is_correct_step(position, self.whom_attack):
                            print(f"action: {action}")
                            self.update_character_info(position, action)
                            self.update_avatars()

                if States.is_animate is True:
                    self.update_default_fields()

            self.draw_cursor()
            self.draw_info_block()
            self.draw_fields()
            self.draw_characters()

            pygame.display.update()
        pygame.quit()

    def create_cursor(self):
        self.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom000.png"))
        pygame.mouse.set_cursor(pygame.cursors.Cursor((15, 0), self.cursor))

    def create_fields(self):
        self.info_updater.create_fields()

    def create_characters(self):
        self.info_updater.create_characters(self.left_team)
        self.info_updater.create_characters(self.right_team)

    def generate_move_order(self):
        States.queue = Queue(self.info_updater.generate_move_order(self.left_team, self.right_team))

    def create_info_block(self):
        self.divs = self.block_updater.create_info_block()

    def reset_properties(self):
        if len(States.queue.current) == 0:
            self.block_updater.reset_buttons()
            States.queue.reset_characters()
            States.queue.reset_queue()
            self.update_rounds()

    @staticmethod
    def update_rounds():
        States.round += 1

    def update_cursor(self):
        pos = pygame.mouse.get_pos()
        if not (Settings.start_battle_filed[1] <= pos[0] <= Settings.start_battle_filed[1] + Settings.n_columns * 2 * Settings.r and Settings.start_battle_filed[0] <= pos[1] <= Settings.height - 140) or States.is_animate is True:
            self.cursor = pygame.image.load(os.path.join(f"data/rcom/clean/Crcom000.png"))

    def update_buttons(self):
        self.block_updater.update_buttons()

    def update_buttons_by_click(self, pos):
        self.block_updater.update_buttons_by_click(pos)

    def update_avatars(self):
        self.block_updater.update_avatars()

    @staticmethod
    def get_cell(pos):
        for i, row in enumerate(States.fields):
            for j, cell in enumerate(row):
                if cell.left <= pos[0] < cell.right and cell.top <= pos[1] < cell.bottom:
                    return i, j
        return None

    def update_character_info(self, new_point, action):
        if action == 'moving':
            States.queue.current[0].change_animation('moving')
            self.info_updater.update_character_position(new_point)
            States.queue.current[0].change_animation('standing')
        if action == 'attack_straight':
            States.queue.current[0].change_animation('moving')
            self.info_updater.update_character_position(self.point_attack)
            States.queue.current[0].change_animation('attack_straight', who_next=self.whom_attack, what_next='getting_hit')
            States.queue.current[0].change_animation('standing')
        States.queue.current.pop(0)

    def update_cursor_info(self, point_over, coordinates):
        self.point_attack, self.whom_attack, self.cursor = self.info_updater.update_cursor_info(States.fields, point_over, coordinates)

    def update_fields_info(self, point_over):
        self.info_updater.update_fields_info(point_over)

    def update_default_fields(self):
        self.info_updater.update_default_fields()

    def draw_fields(self):
        for i in range(len(States.fields)):
            for j in range(len(States.fields[0])):
                States.fields[i][j].surf.fill(0)
                pygame.draw.polygon(States.fields[i][j].surf, States.fields[i][j].color, States.fields[i][j].position,
                                    States.fields[i][j].bold)
                self.screen.blit(States.fields[i][j].surf, (States.fields[i][j].corner[1], States.fields[i][j].corner[0]))

    def draw_characters(self):
        for item in self.left_team + self.right_team:
            item.draw(self.screen)

    def draw_cursor(self):
        pygame.mouse.set_cursor(pygame.cursors.Cursor((15, 0), self.cursor))

    def draw_info_block(self):
        def draw_child(parent):
            for child in parent.children:
                draw_child(child)
                if child.parent is not None:
                    child.draw()

        draw_child(self.divs)
        self.screen.blit(self.divs.surf, self.divs.rect)
