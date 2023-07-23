from modules.settings import Settings


class Field:

    def __init__(self, corner, color, bold):
        self.indent = 0
        self.corner = corner
        self.color = color
        self.bold = bold
        self.is_engaged = False
        self.who_engaged = None
        self.coordinates = None
        self.position = None
        self.surf = None

        self.left = self.corner[1]
        self.right = self.corner[1] + Settings.r * 2
        self.top = self.corner[0]
        self.bottom = self.corner[0] + Settings.R * 2
