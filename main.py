from utils import *
from game import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
buttons = create_buttons()

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(FPS)

    clicked = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            for button in buttons:
                if button.clicked(pos):
                    clicked = button.text

    draw(WIN, clicked)

pygame.quit()
