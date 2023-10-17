import pygame
from events import click
pygame.init()

pygame.display.set_icon(pygame.image.load('./images/pre-icon.png')) # Sets game logo

#temp color library
background_color="#478778" #Lincoln Green
task_color_odd="#2AAA8A" # Jungle Green
task_color_even="#00A36C" # Jade
task_text_color="#355E3B" # Hunter Green

game_title="PROJECT B | (INSERT VERSION OF GAME LATER)" # ==== TITLE NEEDS TO BE CHANGED ====
screen=pygame.display.set_mode([500, 500], pygame.RESIZABLE) # I made the window smaller and resizable 
pygame.display.set_caption(game_title)
background=(background_color) # ==== BACKGROUND IS TEMP ====
framerate=60
font=pygame.font.Font("freesansbold.ttf", 16) # ==== FONT IS TEMP ====
timer = pygame.time.Clock()

#game variables
task1_value=1
task2_value=2
task3_value=3
task4_value=4
task5_value=5
draw_task1=False
draw_task2=False
draw_task3=False
draw_task4=False
draw_task5=False
task1_length=0
task2_length=0
task3_length=0
task4_length=0
task5_length=0
task1_speed=5
task2_speed=4
task3_speed=3
task4_speed=2
task5_speed=1
score=0 # ==== SCORE(currency) IS TEMP ====

def draw_task(color, y_coord, value, draw, length, speed): # ==== COULD BE RENAMED ====
    global score
    if draw and length < 200:
        length += speed
    elif length >=200:
        draw=False
        length=0
        score+=value
    task = pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30]) # ==== FRAME ====
    pygame.draw.rect(screen, "#000000", [75, y_coord -10, 190, 20]) # ==== LOADER ====
    pygame.draw.rect(screen, color, [70, y_coord -15, length, 30])
    value_text=font.render(str(value), True, task_text_color) # ==== TEXT IS TEMP | SHOULD BE REPLACED WITH AN IMAGE LATER ====
    screen.blit(value_text, (25, y_coord -8)) # ==== TEXT IS TEMP | SHOULD BE REPLACED WITH AN IMAGE LATER ====
    return task, length, draw

running=True
while running:
    timer.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN: # ==== CLICKING TASKS ====
            if task1.collidepoint(event.pos):
                draw_task1 = True
            if task2.collidepoint(event.pos):
                draw_task2 = True
            if task3.collidepoint(event.pos):
                draw_task3 = True
            if task4.collidepoint(event.pos):
                draw_task4 = True
            if task5.collidepoint(event.pos):
                draw_task5 = True
                      
        elif event.type == pygame.MOUSEBUTTONUP:
            click.clicked(pygame.mouse.get_pos()) # clicking event
        
    screen.fill(background)
    task1, task1_length, draw_task1 = draw_task(task_color_odd, 50, task1_value, draw_task1, task1_length, task1_speed)
    task2, task2_length, draw_task2 = draw_task(task_color_even, 100, task2_value, draw_task2, task2_length, task2_speed)
    task3, task3_length, draw_task3 = draw_task(task_color_odd, 150, task3_value, draw_task3, task3_length, task3_speed)
    task4, task4_length, draw_task4 = draw_task(task_color_even, 200, task4_value, draw_task4, task4_length, task4_speed)
    task5, task5_length, draw_task5 = draw_task(task_color_odd, 250, task5_value, draw_task5, task5_length, task5_speed)
    pygame.display.flip()

pygame.quit()