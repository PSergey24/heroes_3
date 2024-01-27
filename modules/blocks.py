import os
import pygame
from modules.settings import Settings


class Block:

    def __init__(self, left, top, width=None, height=None, parent=None, name=None):
        self.parent = parent
        self.name = name
        self.children = []
        self.width = width
        self.height = height
        self.left = self.get_left(left)
        self.top = self.get_top(top)

    def get_left(self, left):
        return left + self.parent.left if self.parent is not None else left

    def get_top(self, top):
        return top + self.parent.top if self.parent is not None else top

    def update_children(self, child):
        self.children.append(child)


class Div(Block):

    def __init__(self, left, top, width=None, height=None, parent=None, name=None, color=None):
        super().__init__(left, top, width=width, height=height, parent=parent, name=name)
        self.rect = self.create_rect()
        self.surf = None

        self.create_surf(color)

    def create_rect(self):
        if self.parent is not None:
            return pygame.Rect((self.left - self.parent.left, self.top - self.parent.top,
                                self.width - self.parent.width, self.height - self.parent.height))
        return pygame.Rect((self.left, self.top, self.width, self.height))

    def create_surf(self, color):
        self.surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surf.fill(color)

    def draw(self):
        self.parent.surf.blit(self.surf, self.rect)


class ImgBtn(Block):

    def __init__(self, left, top, width=None, height=None, parent=None, name=None):
        super().__init__(left, top, width=width, height=height, parent=parent, name=name)
        self.surf = None
        self.is_active = True
        self.activeImg = None
        self.notActiveImg = None

        self.create_img(name)

    def create_img(self, name):
        self.activeImg = pygame.image.load(os.path.join(f"data/buttons/clean/{name}1.bmp"))
        self.activeImg = pygame.transform.scale(self.activeImg, (self.width, self.height))

        if os.path.exists(os.path.join(f"data/buttons/clean/{name}2.bmp")):
            self.notActiveImg = pygame.image.load(os.path.join(f"data/buttons/clean/{name}2.bmp"))
            self.notActiveImg = pygame.transform.scale(self.notActiveImg, (self.width, self.height))

        self.surf = self.activeImg

    def switch_to_active(self):
        self.surf = self.activeImg
        self.is_active = True

    def switch_to_not_active(self):
        self.surf = self.notActiveImg
        self.is_active = False

    def draw(self):
        self.parent.surf.blit(self.surf, (self.left - self.parent.left, self.top - self.parent.top))


class ImgAvatar(Block):

    def __init__(self, left, top, width=None, height=None, parent=None, name=None, way=None):
        super().__init__(left, top, width=width, height=height, parent=parent, name=name)
        self.surf = None
        self.width = width
        self.height = height

        self.create_img(way)

    def create_img(self, full_way):
        self.surf = pygame.image.load(os.path.join(f"{full_way}"))
        self.surf = pygame.transform.scale(self.surf, (self.width, self.height))

    def draw(self):
        self.parent.surf.blit(self.surf, (self.left - self.parent.left, self.top - self.parent.top))
        pygame.draw.rect(self.parent.surf, (250, 226, 119, 255), (0, 0, self.width, self.height), 2)


class Txt(Block):

    def __init__(self, left, top, width=None, height=None, parent=None, name=None):
        super().__init__(left, top, width=width, height=height, parent=parent, name=name)
        self.surf = None
        self.top_ = top
        self.width = width
        self.height = height

        self.txt = None

    def create_txt(self, text, color):
        self.txt = text
        self.surf = Settings.FONT.render(text, False, color)

    def draw(self):
        shift = self.get_shift()
        pygame.draw.rect(self.parent.surf, (250, 226, 119, 255), (0, self.top_ - 2, self.width, self.height + 2), 2)
        self.parent.surf.blit(self.surf, (self.left - self.parent.left + shift, self.top - self.parent.top))

    def get_shift(self):
        if len(self.txt) == 1:
            return -1
        if len(self.txt) == 2:
            return -4
        if len(self.txt) == 3:
            return -8
