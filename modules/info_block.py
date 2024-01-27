from copy import copy

from modules.blocks import Div, ImgAvatar, ImgBtn, Txt
from modules.settings import Settings
from modules.states import States, Objects


class InfoBlock:

    def __init__(self):
        self.main = None
        self.left = None
        self.center = None
        self.right = None

        self.top_center = None
        self.bottom_center = None
        self.buttons = []

        self.init()

    def init(self):
        self.main = self.create_div(Settings.info_block_margin, Settings.height - 130, Settings.info_block_width, Settings.info_block_height, (220, 200, 0, 80))
        self.left = self.create_div(0, 0, Settings.left_ib_width, Settings.info_block_height, (6, 9, 5, 255), parent=self.main)
        self.center = self.create_div(Settings.left_ib_width, 0, Settings.center_ib_width, Settings.info_block_height, (0, 0, 155, 120), parent=self.main)
        self.right = self.create_div(Settings.left_ib_width + Settings.center_ib_width, 0, Settings.right_ib_width, Settings.info_block_height, (6, 9, 5, 255), parent=self.main)
        self.top_center = self.create_div(0, 0, Settings.center_ib_width, 75, (0, 0, 0, 80), parent=self.center)
        self.bottom_center = self.create_div(0, 75, Settings.center_ib_width, 15, (85, 54, 30, 255), parent=self.center)

        self.create_buttons()
        self.update_avatars()

    @staticmethod
    def create_div(left, top, width, height, color, parent=None):
        div = Div(left, top, width=width, height=height, parent=parent, color=color)
        if parent:
            parent.update_children(div)
        return div

    def create_buttons(self):
        self.create_button(0, 0, Settings.right_ib_width / 2, Settings.info_block_height / 2, "shooter", parent=self.right)
        self.create_button(0, Settings.info_block_height / 2, Settings.right_ib_width / 2, Settings.info_block_height / 2, "wait", parent=self.right)
        self.create_button(Settings.right_ib_width / 2, Settings.info_block_height / 2, Settings.right_ib_width / 2, Settings.info_block_height / 2, "defense", parent=self.right)

    def create_button(self, left, top, width, height, name, parent=None):
        img = ImgBtn(left, top, width, height, parent=parent, name=name)

        if parent:
            parent.update_children(img)
        self.buttons.append(img)

    def update_avatars(self):
        self.top_center.children.clear()
        count = 15

        max_step = len(Objects.queue.sequence)
        for i, item in reversed(list(enumerate(Objects.queue.sequence))):
            if item.is_defense is True:
                max_step -= 1

        i, step, rnd = 0, 0, copy(States.round)

        is_first = True
        queue, queue2 = copy(Objects.queue.sequence), Objects.queue.get_sequence()
        while i < count:
            while ((is_first is True and step < max_step) or (is_first is False and step < len(queue))) and i < count:
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

        color = (144, 13, 13, 255)
        if item.team == 2:
            color = (52, 70, 131, 255)

        box = self.create_div(left, 0, Settings.avatar_width, 80, color, parent=self.top_center)

        img = ImgAvatar(0, 0, height=Settings.avatar_height, width=Settings.avatar_width, parent=box, name=item.name, way=f"data/avatars/{item.name}.bmp")
        box.update_children(img)

        bg = self.create_div(25, Settings.avatar_height, Settings.avatar_width, 16, color, parent=box)
        box.update_children(bg)

        txt = Txt(25, Settings.avatar_height, height=16, width=Settings.avatar_width, parent=box)
        txt.create_txt(str(item.characteristics["current_count"]), (255, 255, 255))
        box.update_children(txt)

    def create_avatar_round(self, idx, current_round):
        left = self.get_avatar_position(idx)
        color = (100, 100, 0)

        box = self.create_div(left, 0, Settings.avatar_width, 80, color, parent=self.top_center)

        img = ImgAvatar(0, 0, height=Settings.avatar_height, width=Settings.avatar_width, parent=box, name='round', way=f"data/avatars/CPrLBlk.bmp")
        box.update_children(img)

        bg = self.create_div(25, Settings.avatar_height, Settings.avatar_width, 16, color, parent=box)
        box.update_children(bg)

        txt = Txt(25, Settings.avatar_height, height=16, width=Settings.avatar_width, parent=box)
        txt.create_txt(str(current_round), (255, 255, 255))
        box.update_children(txt)

    def get_avatar_position(self, idx):
        return 0 if idx == 0 else (idx * (self.top_center.children[-1].width + 2))

    def update(self):
        self.update_buttons()

    def update_buttons(self):
        for btn in self.buttons:
            self.update_button(btn)

    @staticmethod
    def update_button(btn):
        if btn.name == 'wait':
            if Objects.active_unit.info.is_wait is False:
                btn.switch_to_active()
            else:
                btn.switch_to_not_active()

        if btn.name == 'defense':
            if Objects.active_unit.info.is_defense is False:
                btn.switch_to_active()
            else:
                btn.switch_to_not_active()

        if btn.name == 'shooter':
            if btn.is_active and States.btn_shooter and Objects.active_unit.info.characteristics["is_shooter"] is True:
                btn.switch_to_not_active()
                States.btn_shooter = True
            elif (not btn.is_active and not States.btn_shooter and Objects.active_unit.info.characteristics["is_shooter"] is True) or Objects.active_unit.info.characteristics["is_shooter"] is False:
                btn.switch_to_active()
                States.btn_shooter = False

    def handle_click(self):
        if Objects.cursor.pixel is not None:
            for btn in self.buttons:
                if (btn.top <= Objects.cursor.pixel[1] <= btn.top + btn.height) and (btn.left <= Objects.cursor.pixel[0] <= btn.left + btn.width):
                    self.update_button_by_click(btn)

    def update_button_by_click(self, btn):
        if btn.name == 'wait' and btn.is_active is True:
            self.update_wait_by_click()
        if btn.name == 'defense' and btn.is_active is True:
            self.update_defense_by_click()
        if btn.name == 'shooter':
            self.update_shooter_by_click()

    def update_wait_by_click(self):
        self.update_queue_wait()
        self.update_avatars()

    @staticmethod
    def update_queue_wait():
        Objects.queue.handle_wait()

    def update_defense_by_click(self):
        self.update_queue_defense()
        self.update_avatars()

    @staticmethod
    def update_queue_defense():
        Objects.queue.handle_defense()

    @staticmethod
    def update_shooter_by_click():
        if Objects.queue.sequence[0].characteristics["is_shooter"] is False or (Objects.queue.sequence[0].characteristics["is_shooter"] and States.btn_shooter):
            States.btn_shooter = False
        elif Objects.queue.sequence[0].characteristics["is_shooter"] and not States.btn_shooter:
            States.btn_shooter = True

    def handle_move(self):
        self.update_avatars()

    def draw(self, screen):
        def draw_child(parent):
            for child in parent.children:
                draw_child(child)
                if child.parent is not None:
                    child.draw()

        draw_child(self.main)
        screen.blit(self.main.surf, self.main.rect)
