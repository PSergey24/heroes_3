from modules.blocks import Div, ImgAvatar, ImgBtn, Txt
from modules.settings import Settings

from copy import copy


class BlockUpdater:

    def __init__(self, buttons):
        self.buttons = buttons
        self.main = None
        self.left = None
        self.center = None
        self.right = None

        self.top_center = None
        self.bottom_center = None

    def create_info_block(self, queue, current_round):
        self.main = self.create_div(Settings.info_block_margin, Settings.height - 130, Settings.info_block_width,
                                    Settings.info_block_height, (220, 200, 0, 80))
        self.left = self.create_div(0, 0, Settings.left_ib_width, Settings.info_block_height, (255, 255, 255, 80),
                                    parent=self.main)
        self.center = self.create_div(Settings.left_ib_width, 0, Settings.center_ib_width, Settings.info_block_height,
                                      (0, 0, 155, 120), parent=self.main)
        self.right = self.create_div(Settings.left_ib_width + Settings.center_ib_width, 0, Settings.right_ib_width,
                                     Settings.info_block_height, (255, 255, 255, 80), parent=self.main)
        self.top_center = self.create_div(0, 0, Settings.center_ib_width, 80, (155, 0, 0, 80), parent=self.center)
        self.bottom_center = self.create_div(0, 80, Settings.center_ib_width, 10, (0, 155, 0, 80), parent=self.center)

        self.create_buttons()
        self.update_avatars(queue, current_round)
        return self.main

    @staticmethod
    def create_div(left, top, width, height, color, parent=None):
        div = Div(left, top, width=width, height=height, parent=parent, color=color)
        if parent:
            parent.update_children(div)
        return div

    def create_buttons(self):
        self.create_button(0, Settings.info_block_height / 2, Settings.right_ib_width / 2,
                           Settings.info_block_height / 2, "wait", parent=self.right)

        self.create_button(Settings.right_ib_width / 2, Settings.info_block_height / 2,
                           Settings.right_ib_width / 2, Settings.info_block_height / 2, "defense",
                           parent=self.right)

    def create_button(self, left, top, width, height, name, parent=None):
        img = ImgBtn(left, top, width, height, parent=parent, name=name)

        if parent:
            parent.update_children(img)
        self.buttons.append(img)

    def update_avatars(self, queue, current_round):
        i, r = 0, copy(current_round)

        for _ in range(4):
            if _ == 0:
                for a, item in enumerate(queue.current):
                    self.create_avatar(i, item)
                    i += 1
            else:
                for a, item in enumerate(queue.original):
                    self.create_avatar(i, item)
                    i += 1

            if i != 0:
                self.create_avatar_round(i, r)
                i += 1
            r += 1

    def create_avatar(self, idx, item):
        left = self.get_avatar_position(idx)

        color = (255, 0, 0)
        if item.team == 2:
            color = (0, 0, 255)

        box = self.create_div(left, 0, Settings.avatar_width, 80, color, parent=self.top_center)

        img = ImgAvatar(0, 0, height=Settings.avatar_height, width=Settings.avatar_width, parent=box,
                        name=item.character, way=f"data/move_order/{item.avatar}")
        box.update_children(img)

        bg = self.create_div(25, Settings.avatar_height, Settings.avatar_width, 16, color, parent=box)
        box.update_children(bg)

        txt = Txt(25, Settings.avatar_height, height=16, width=Settings.avatar_width, parent=box)
        txt.create_txt(str(item.count), (255, 255, 255))
        box.update_children(txt)

    def create_avatar_round(self, idx, current_round):
        left = self.get_avatar_position(idx)
        color = (100, 100, 0)

        box = self.create_div(left, 0, Settings.avatar_width, 80, color, parent=self.top_center)

        img = ImgAvatar(0, 0, height=Settings.avatar_height, width=Settings.avatar_width, parent=box,
                        name='round', way=f"data/move_order/CPrLBlk.bmp")
        box.update_children(img)

        bg = self.create_div(25, Settings.avatar_height, Settings.avatar_width, 16, color, parent=box)
        box.update_children(bg)

        txt = Txt(25, Settings.avatar_height, height=16, width=Settings.avatar_width, parent=box)
        txt.create_txt(str(current_round), (255, 255, 255))
        box.update_children(txt)

    def get_avatar_position(self, idx):
        return 0 if idx == 0 else idx * self.top_center.children[-1].width

    @staticmethod
    def switch_btn_to_active(btn):
        btn.switch_to_active()

    @staticmethod
    def switch_btn_to_not_active(btn):
        btn.switch_to_not_active()
