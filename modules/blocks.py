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
        self.rect = None
        self.surf = None
        self.images = None
        self.txt = None

    def get_left(self, left):
        return left + self.parent.left if self.parent is not None else left

    def get_top(self, top):
        return top + self.parent.top if self.parent is not None else top

    def update_children(self, child):
        self.children.append(child)


class Div(Block):

    def __init__(self, left, top, width=None, height=None, parent=None, name=None):
        super().__init__(left, top, width=width, height=height, parent=parent, name=None)
        self.parent = parent
        self.name = name
        self.children = []
        self.width = width
        self.height = height
        self.left = self.get_left(left)
        self.top = self.get_top(top)
        self.rect = self.create_rect()
        self.surf = None

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


class Img(Block):

    def __init__(self, left, top, width=None, height=None, parent=None, name=None):
        super().__init__(left, top, width=width, height=height, parent=parent, name=name)
        self.parent = parent
        self.name = name
        self.children = []
        self.width = width
        self.height = height
        self.left = self.get_left(left)
        self.top = self.get_top(top)
        self.surf = None
        self.images = []

    def create_img(self, full_way):
        way, name = "/".join(full_way.split('/')[:-1]), full_way.split('/')[-1]
        files = sorted(os.listdir(way))
        for file in files:
            if name in file:
                surf = pygame.image.load(os.path.join(f"{way}/{file}"))
                surf = pygame.transform.scale(surf, (self.width, self.height))
                self.images.append(surf)
        self.surf = self.images[0]

    def switch_image(self):
        self.images.append(self.images.pop(0))
        self.surf = self.images[0]

    def draw(self):
        self.parent.surf.blit(self.surf, (self.left - self.parent.left, self.top - self.parent.top))


class Txt(Block):

    def __init__(self, left, top, width=None, height=None, parent=None, name=None):
        super().__init__(left, top, width=width, height=height, parent=parent, name=None)
        self.parent = parent
        self.name = name
        self.children = []
        self.width = width
        self.height = height
        self.left = self.get_left(left)
        self.top = self.get_top(top)
        self.surf = None
        self.txt = None

    def create_txt(self, text, color):
        self.txt = text
        self.surf = Settings.FONT.render(text, True, color)

    def draw(self):
        self.parent.surf.blit(self.surf, (self.left - self.parent.left, self.top - self.parent.top))
