from modules.blocks import Div, ImgAvatar, ImgBtn, Txt
from modules.settings import Settings, States

from copy import copy


class BlockUpdater:

    def __init__(self):
        self.buttons = []
        self.main = None
        self.left = None
        self.center = None
        self.right = None

        self.top_center = None
        self.bottom_center = None

    def create_info_block(self):
        States.main = self.create_div(Settings.info_block_margin, Settings.height - 130, Settings.info_block_width,
                                      Settings.info_block_height, (220, 200, 0, 80))
        self.left = self.create_div(0, 0, Settings.left_ib_width, Settings.info_block_height, (255, 255, 255, 80),
                                    parent=States.main)
        self.center = self.create_div(Settings.left_ib_width, 0, Settings.center_ib_width, Settings.info_block_height,
                                      (0, 0, 155, 120), parent=States.main)
        self.right = self.create_div(Settings.left_ib_width + Settings.center_ib_width, 0, Settings.right_ib_width,
                                     Settings.info_block_height, (255, 255, 255, 80), parent=States.main)
        self.top_center = self.create_div(0, 0, Settings.center_ib_width, 80, (155, 0, 0, 80), parent=self.center)
        self.bottom_center = self.create_div(0, 80, Settings.center_ib_width, 10, (0, 155, 0, 80), parent=self.center)

        self.create_buttons()
        self.update_avatars()

    @staticmethod
    def create_div(left, top, width, height, color, parent=None):
        div = Div(left, top, width=width, height=height, parent=parent, color=color)
        if parent:
            parent.update_children(div)
        return div

    def create_buttons(self):
        self.create_button(0, 0, Settings.right_ib_width / 2,
                           Settings.info_block_height / 2, "shooter", parent=self.right)

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

    def update_avatars(self):
        count = 15

        max_step = len(States.queue.current)
        for i, item in reversed(list(enumerate(States.queue.current))):
            if item.btn_defense is True:
                max_step -= 1

        i, step, rnd = 0, 0, copy(States.round)

        is_first = True
        queue, queue2 = copy(States.queue.current), States.queue.get_order()
        while i < count:
            while ((is_first is True and step < max_step) or
                   (is_first is False and step < len(queue))) and i < count:
                current = step % len(queue)
                self.create_avatar(i, queue[current])
                step, i = step+1, i+1

            if i != 0:
                self.create_avatar_round(i, rnd)
                i += 1

            is_first, queue = False, queue2
            step, rnd = 0, rnd+1

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

    def update_buttons(self):
        for btn in self.buttons:
            if btn.name == 'wait':
                if States.queue.current[0].btn_wait is False:
                    btn.switch_to_active()
                else:
                    btn.switch_to_not_active()
            if btn.name == 'defense':
                if States.queue.current[0].btn_defense is False:
                    btn.switch_to_active()
                else:
                    btn.switch_to_not_active()
            if btn.name == 'shooter':
                if btn.isActive and States.queue.current[0].is_shooter is True:
                    btn.switch_to_not_active()
                    States.btn_shooter = True
                elif btn.isActive is False and States.queue.current[0].is_shooter is False:
                    btn.switch_to_active()
                    States.btn_shooter = False

    def update_buttons_by_click(self):
        for btn in self.buttons:
            if (btn.top <= States.point_over[1] <= btn.top + btn.height) and \
                    (btn.left <= States.point_over[0] <= btn.left + btn.width):
                self.update_button_by_click(btn)

    def update_button_by_click(self, btn):
        if btn.name == 'wait' and btn.isActive is True:

            States.queue.current[0].btn_wait = True
            States.queue.current.insert(self.get_wait_index(), States.queue.current.pop(0))
            self.update_avatars()
        if btn.name == 'defense' and btn.isActive is True:
            States.step += 1

            States.queue.current[0].btn_defense, States.queue.current[0].btn_wait = True, True
            States.queue.current.append(States.queue.current.pop(0))
            self.update_avatars()
        if btn.name == 'shooter':
            if btn.isActive:
                btn.switch_to_not_active()
            else:
                btn.switch_to_active()

    @staticmethod
    def get_wait_index():
        for i, item in reversed(list(enumerate(States.queue.current))):
            if item.btn_wait is False:
                return i
        return 0
