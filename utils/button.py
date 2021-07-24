from .calculate import *
from .fonts import *


class Button:
    def __init__(self, x, y, text=None, width=100, height=60, color=WHITE, text_color=BLACK, font_size=26):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font_size = font_size

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(
            win, BLACK, (self.x, self.y, self.width, self.height), 2)
        if self.text:
            button_font = get_font(self.font_size)
            text_surface = button_font.render(self.text, 1, self.text_color)
            win.blit(text_surface, (self.x + self.width /
                                    2 - text_surface.get_width()/2, self.y + self.height/2 - text_surface.get_height()/2))

    def clicked(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True
