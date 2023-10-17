import pygame
from events import click

pygame.init()

pygame.display.set_icon(pygame.image.load('./images/pre-icon.png')) # Sets game logo
#temp color library
background_color="#478778" # Lincoln Green
task_color_odd="#2AAA8A" # Jungle Green
task_color_even="#00A36C" # Jade

game_title="PROJECT B | (INSERT VERSION OF GAME LATER)" # ==== TITLE NEEDS TO BE CHANGED ====
screen=pygame.display.set_mode([500, 500], pygame.RESIZABLE) # I made the window smaller and resizable 
pygame.display.set_caption(game_title)
background=(background_color) # ==== BACKGROUND IS TEMP ====
framerate=60
font=pygame.font.Font("freesansbold.ttf", 16) # ==== FONT IS TEMP ====
timer = pygame.time.Clock()

def draw_task_1(color, y_coord): # ==== COULD BE RENAMED ====
    pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, color, [75, y_coord -10, 190, 20])

running=True
while running:
    timer.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONUP:
            click.clicked(pygame.mouse.get_pos()) # clicking event
        
    screen.fill(background)
    draw_task_1(task_color_odd, 50)
    draw_task_1(task_color_even, 100)
    pygame.display.flip()

pygame.quit()