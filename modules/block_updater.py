from modules.blocks import Div, Img
from modules.settings import Settings


class BlockUpdater:

    def __init__(self):
        self.main = None
        self.left = None
        self.center = None
        self.right = None

    def create_info_block(self, screen, move_order):
        self.main = self.create_div(Settings.info_block_margin, Settings.height - 130, Settings.info_block_width,
                                    Settings.info_block_height, (220, 200, 0, 80))
        self.left = self.create_div(0, 0, Settings.left_ib_width, Settings.info_block_height, (255, 255, 255, 80),
                                    parent=self.main)
        self.center = self.create_div(Settings.left_ib_width, 0, Settings.center_ib_width, Settings.info_block_height,
                                      (0, 0, 155, 80), parent=self.main)
        self.right = self.create_div(Settings.left_ib_width + Settings.center_ib_width, 0, Settings.right_ib_width,
                                     Settings.info_block_height, (255, 255, 255, 80), parent=self.main)

        self.create_buttons()
        self.create_avatars(move_order)

        self.main.surf.blit(self.right.surf, self.right.rect)
        self.main.surf.blit(self.center.surf, self.center.rect)
        self.main.surf.blit(self.left.surf, self.left.rect)
        screen.blit(self.main.surf, self.main.rect)

    @staticmethod
    def create_div(left, top, width, height, color, parent=None):
        div = Div(left, top, width, height, parent=parent)
        div.create_surf(color)
        return div

    def create_buttons(self):
        self.create_button(0, Settings.info_block_height / 2, Settings.right_ib_width / 2,
                           Settings.info_block_height / 2, "data/buttons/clean/wait", parent=self.right)

        self.create_button(Settings.right_ib_width / 2, Settings.info_block_height / 2,
                           Settings.right_ib_width / 2, Settings.info_block_height / 2, "data/buttons/clean/defense",
                           parent=self.right)

    @staticmethod
    def create_button(left, top, width, height, full_way, parent=None):
        img = Img(left, top, width, height, parent=parent)
        img.create_img(full_way)
        parent.surf.blit(img.surf, (left, top))

    def create_avatars(self, move_order):
        for i, item in enumerate(move_order):
            self.create_avatar(i, item)

    def create_avatar(self, idx, item):
        left = self.get_avatar_position(idx)
        img = Img(left + 2, 0, height=Settings.avatar_height, width=Settings.avatar_width, parent=self.center)
        img.create_img(f"data/move_order/{item.avatar}")
        self.center.update_children(img)
        self.center.surf.blit(img.surf, (left + 2, 0))

    def get_avatar_position(self, idx):
        return 0 if idx == 0 else idx * self.center.children[-1].width
