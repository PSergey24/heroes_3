import pygame
import os
from copy import copy

from modules.settings import Settings
from modules.helper import Helper
from modules.info_updater import InfoUpdater
from modules.block_updater import BlockUpdater
from modules.queue import Queue
from unit import Angel, Elf, Lich, Mage


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((Settings.width, Settings.height))
        self.fields = []

        self.left_team = [Lich(8, 3, 15, 1), Mage(2, 5, 6, 1)]
        self.right_team = [Lich(10, 14, 17, 2), Mage(8, 13, 3, 2)]

        self.divs = None
        self.buttons = []

        self.bg = pygame.image.load(os.path.join("data/bg", "CmBkDrDd.bmp"))
        self.bg = pygame.transform.scale(self.bg, (Settings.width, Settings.height))

        self.queue = None
        self.helper = Helper()
        self.info_updater = InfoUpdater()
        self.block_updater = BlockUpdater(self.buttons)

        self.round = 1

    def run(self):
        run = True

        self.screen.blit(self.bg, (0, 0))

        self.create_fields()
        self.create_characters()
        self.generate_move_order()
        self.create_info_block()

        while run:
            self.screen.blit(self.bg, (0, 0))
            self.reset_properties()
            self.get_buttons_info()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.update_buttons_info(pos)

                    if position := self.get_cell(pos):
                        if self.helper.is_correct_step(self.fields, self.queue.current, position):
                            self.update_character_info(position)
                            self.update_avatars()
                            self.update_properties()

                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    if position := self.get_cell(pos):
                        self.update_fields_info(position)

            self.draw_info_block()
            self.draw_fields()
            self.draw_characters()

            pygame.display.update()
        pygame.quit()

    def create_fields(self):
        self.fields = self.info_updater.create_fields(self.fields)

    def create_info_block(self):
        self.divs = self.block_updater.create_info_block(self.queue, self.round)

    def reset_properties(self):
        self.reset_buttons()
        self.reset_characters()
        self.reset_queue()

    def reset_queue(self):
        if len(self.queue.current) == 0:
            self.queue.current = copy(self.queue.original)

    def reset_buttons(self):
        if len(self.queue.current) == 0:
            for btn in self.buttons:
                self.block_updater.switch_btn_to_active(btn)

    def reset_characters(self):
        if len(self.queue.current) == 0:
            for ch in self.queue.original:
                ch.btn_wait = False
                ch.btn_defense = False

    def get_buttons_info(self):
        for btn in self.buttons:
            if btn.name == 'wait':
                if self.queue.current[0].btn_wait is False:
                    self.block_updater.switch_btn_to_active(btn)
                else:
                    self.block_updater.switch_btn_to_not_active(btn)
            if btn.name == 'defense':
                if self.queue.current[0].btn_defense is False:
                    self.block_updater.switch_btn_to_active(btn)
                else:
                    self.block_updater.switch_btn_to_not_active(btn)

    def update_avatars(self):
        self.block_updater.update_avatars(self.queue, self.round)

    def update_properties(self):
        self.update_rounds()

    def update_rounds(self):
        if len(self.queue.current) == 0:
            self.round += 1

    def create_characters(self):
        self.fields = self.info_updater.create_characters(self.fields, self.left_team)
        self.fields = self.info_updater.create_characters(self.fields, self.right_team)

    def generate_move_order(self):
        move_order = self.info_updater.generate_move_order(self.left_team, self.right_team)
        self.queue = Queue(move_order)

    def get_cell(self, pos):
        for i, row in enumerate(self.fields):
            for j, cell in enumerate(row):
                if cell.left <= pos[0] < cell.right and cell.top <= pos[1] < cell.bottom:
                    return i, j
        return None

    def update_buttons_info(self, pos):
        for btn in self.buttons:
            if (btn.top <= pos[1] <= btn.top + btn.height) and (btn.left <= pos[0] <= btn.left + btn.width):
                self.update_button_click(btn)

    def update_button_click(self, btn):
        if btn.name == 'wait' and btn.isActive is True:
            self.queue.current[0].btn_wait = True
            self.queue.current.insert(self.get_wait_index(), self.queue.current.pop(0))
            self.update_avatars()
        if btn.name == 'defense' and btn.isActive is True:
            self.queue.current[0].btn_defense = True
            self.queue.current.pop(0)
            self.update_avatars()
        self.update_rounds()

    def get_wait_index(self):
        for i, item in reversed(list(enumerate(self.queue.current))):
            if item.btn_wait is False:
                return i
        return 0

    def update_character_info(self, new_point):
        self.fields, self.queue.current = self.info_updater.update_character_info(self.fields, self.queue.current,
                                                                                  new_point)

    def update_fields_info(self, point_over):
        self.fields = self.info_updater.update_fields_info(self.fields, self.queue.current, point_over)

    def draw_fields(self):
        for i in range(len(self.fields)):
            for j in range(len(self.fields[0])):
                self.fields[i][j].surf.fill(0)
                pygame.draw.polygon(self.fields[i][j].surf, self.fields[i][j].color, self.fields[i][j].position,
                                    self.fields[i][j].bold)
                self.screen.blit(self.fields[i][j].surf, (self.fields[i][j].corner[1], self.fields[i][j].corner[0]))

    def draw_characters(self):
        for item in self.left_team + self.right_team:
            item.draw(self.screen)

    def draw_info_block(self):
        def draw_child(parent):
            for child in parent.children:
                draw_child(child)
                if child.parent is not None:
                    child.draw()

        draw_child(self.divs)
        self.screen.blit(self.divs.surf, self.divs.rect)
