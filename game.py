import pygame
import os

from modules.settings import Settings
from modules.info_updater import InfoUpdater
from modules.block_updater import BlockUpdater
from unit import Angel, Elf, Lich, Mage


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((Settings.width, Settings.height))
        self.fields = []

        self.left_team = [Lich(8, 3, 15, 1), Mage(2, 5, 6, 1)]
        self.right_team = [Lich(10, 14, 17, 2), Mage(8, 13, 3, 2)]
        self.move_order = []

        self.bg = pygame.image.load(os.path.join("data/bg", "CmBkDrDd.bmp"))
        self.bg = pygame.transform.scale(self.bg, (Settings.width, Settings.height))

        self.info_updater = InfoUpdater()
        self.block_updater = BlockUpdater()

    def run(self):
        run = True

        self.screen.blit(self.bg, (0, 0))
        self.create_fields()

        self.create_characters()
        self.generate_move_order()


        while run:
            self.screen.blit(self.bg, (0, 0))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)

                    # if self.rect_left.collidepoint(event.pos):
                    #     print("left")

                    # if self.rect_main.collidepoint(event.pos):
                    #     print("main")
                    #
                    #     if self.rect_left.collidepoint(event.pos):
                    #         print("left")
                    #     else:
                    #         print("not left")

                    pos = pygame.mouse.get_pos()
                    if position := self.get_cell(pos):
                        self.update_character_info(position)

                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    if position := self.get_cell(pos):
                        self.update_fields_info(position)

            self.draw_fields()
            self.draw_characters()
            self.create_info_block()

            pygame.display.update()
        pygame.quit()

    def create_fields(self):
        self.fields = self.info_updater.create_fields(self.fields)

    def create_info_block(self):
        self.block_updater.create_info_block(self.screen, self.move_order)

    def create_characters(self):
        self.fields = self.info_updater.create_characters(self.fields, self.left_team)
        self.fields = self.info_updater.create_characters(self.fields, self.right_team)

    def generate_move_order(self):
        self.move_order = self.info_updater.generate_move_order(self.move_order, self.left_team, self.right_team)

    def get_cell(self, pos):
        for i, row in enumerate(self.fields):
            for j, cell in enumerate(row):
                if cell.left <= pos[0] < cell.right and cell.top <= pos[1] < cell.bottom:
                    return i, j
        return None

    def update_character_info(self, new_point):
        self.fields, self.move_order = self.info_updater.update_character_info(self.fields, self.move_order, new_point)

    def update_fields_info(self, point_over):
        self.fields = self.info_updater.update_fields_info(self.fields, self.move_order, point_over)

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

