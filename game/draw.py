from utils import *
from .gol import GameOfLife

gol = GameOfLife()


def draw_grid(win):
    grid = gol.next_generation()

    for i in range(1, ROWS + 1):
        for j in range(1, COLS + 1):
            if grid[i][j]:
                pygame.draw.rect(win, BLACK, (j * PIXEL_SIZE, i *
                                              PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    pygame.draw.line(win, BLACK, (0, HEIGHT - TOOLBAR_HEIGHT + LINE_TOP_PADDING),
                     (WIDTH, HEIGHT - TOOLBAR_HEIGHT + LINE_TOP_PADDING), 4)


buttons = [
]


def create_buttons():
    buttons_props = [
        {
            "text": "Random",
            "width": 100
        },
        {
            "text": "Glider Gun",
            "width": 120
        },
        {
            "text": "Infinite Growth 1",
            "width": 150
        },
        {
            "text": "Infinite Growth 2",
            "width": 150
        },
        {
            "text": "Infinite Growth 3",
            "width": 150
        }
    ]
    x = 0
    for button in buttons_props:
        buttons.append(Button(x + BUTTON_SPACING, BUTTON_Y,
                       text=button["text"], width=button["width"]))
        x += BUTTON_SPACING + button["width"]
    return buttons


def draw_buttons(win):
    for button in buttons:
        button.draw(win)


def draw(win, clicked):
    if clicked:
        gol.change_template(clicked)
    win.fill(BG_COLOR)
    draw_grid(win)
    draw_buttons(win)
    pygame.display.update()
