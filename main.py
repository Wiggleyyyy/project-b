import pygame
from events import click
from include import colorlibrary
pygame.init()

pygame.display.set_icon(pygame.image.load('./images/pre-icon.png')) # Sets game logo

game_title="PROJECT B | (INSERT VERSION OF GAME LATER)" # ==== TITLE NEEDS TO BE CHANGED ====
screen=pygame.display.set_mode([500, 500], pygame.RESIZABLE) # I made the window smaller and resizable 
pygame.display.set_caption(game_title)
background=(colorlibrary.background_color) # ==== BACKGROUND IS TEMP ====
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
score=5000 # ==== SCORE(currency) IS TEMP ====

#draw buttons function
task1_cost=1
task1_owned=False
task1_manager_cost=100
task2_cost=2
task2_owned=False
task2_manager_cost=500
task3_cost=3
task3_owned=False
task3_manager_cost=1000
task4_cost=4
task4_owned=False
task4_manager_cost=1500
task5_cost=5
task5_owned=False
task5_manager_cost=2000

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
    value_text=font.render(str(value), True, colorlibrary.task_text_color) # ==== TEXT IS TEMP | SHOULD BE REPLACED WITH AN IMAGE LATER ====
    screen.blit(value_text, (25, y_coord -8)) # ==== TEXT IS TEMP | SHOULD BE REPLACED WITH AN IMAGE LATER ====
    return task, length, draw

def draw_buttons(color, x_coord, cost, owned, manager_cost):
    task_button = pygame.draw.rect(screen, color, [x_coord, 340, 50, 30])
    task_cost = font.render(str(round(cost, 2)), True, "#000000")
    screen.blit(task_cost, (x_coord + 6, 350))
    if not owned:
        manager_button = pygame.draw.rect(screen, color, [x_coord, 405, 50, 30])
        manager_text = font.render(str(round(manager_cost, 2)), True, "#000000")
        screen.blit(manager_text, (x_coord + 6, 410))
    else:
        manager_button = pygame.draw.rect(screen, "#000000", [x_coord, 405, 50, 30])
    return task_button, manager_button

running=True
while running:
    timer.tick(framerate)
    if task1_owned and not draw_task1:
        draw_task1=True
    if task2_owned and not draw_task2:
        draw_task2=True
    if task3_owned and not draw_task3:
        draw_task3=True
    if task4_owned and not draw_task4:
        draw_task4=True
    if task5_owned and not draw_task5:
        draw_task5=True
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
            if task1_manager_buy.collidepoint(event.pos) and score >= task1_manager_cost and not task1_owned:
                task1_owned=True
                score -= task1_manager_cost
            if task2_manager_buy.collidepoint(event.pos) and score >= task2_manager_cost and not task2_owned:
                task2_owned=True
                score -= task2_manager_cost
            if task3_manager_buy.collidepoint(event.pos) and score >= task3_manager_cost and not task3_owned:
                task3_owned=True
                score -= task3_manager_cost
            if task4_manager_buy.collidepoint(event.pos) and score >= task4_manager_cost and not task4_owned:
                task4_owned=True
                score -= task4_manager_cost
            if task5_manager_buy.collidepoint(event.pos) and score >= task5_manager_cost and not task5_owned:
                task5_owned=True
                score -= task5_manager_cost
                      
        elif event.type == pygame.MOUSEBUTTONUP:
            click.clicked(pygame.mouse.get_pos()) # clicking event
        
    screen.fill(background)
    
    task1, task1_length, draw_task1 = draw_task(colorlibrary.task_color_odd, 50, task1_value, draw_task1, task1_length, task1_speed)
    task2, task2_length, draw_task2 = draw_task(colorlibrary.task_color_even, 100, task2_value, draw_task2, task2_length, task2_speed)
    task3, task3_length, draw_task3 = draw_task(colorlibrary.task_color_odd, 150, task3_value, draw_task3, task3_length, task3_speed)
    task4, task4_length, draw_task4 = draw_task(colorlibrary.task_color_even, 200, task4_value, draw_task4, task4_length, task4_speed)
    task5, task5_length, draw_task5 = draw_task(colorlibrary.task_color_odd, 250, task5_value, draw_task5, task5_length, task5_speed)
    
    # ==== BUY BUTTONS ARE TEMP | WILL ADD BUT MENU LATER ====
    task1_buy, task1_manager_buy = draw_buttons(colorlibrary.button_color_odd, 10, task1_cost, task1_owned, task1_manager_cost)
    task2_buy, task2_manager_buy = draw_buttons(colorlibrary.button_color_even, 70, task2_cost, task2_owned, task2_manager_cost)
    task3_buy, task3_manager_buy = draw_buttons(colorlibrary.button_color_odd, 130, task3_cost, task3_owned, task3_manager_cost)
    task4_buy, task4_manager_buy = draw_buttons(colorlibrary.button_color_even, 190, task4_cost, task4_owned, task4_manager_cost)
    task5_buy, task5_manager_buy = draw_buttons(colorlibrary.button_color_odd, 250, task5_cost, task5_owned, task5_manager_cost)
    
    display_score = font.render("Money: $"+str(round(score, 2)), True, "#ffffff", "#000000") # ==== REPLACE "Money" WITH CURRENCY NAME | MAYBE REPLACE $ WITH CURRENCY IMAGE ====
    screen.blit(display_score, (400,5))
    buy_more=font.render("Buy more: ", True, "#ffffff")
    screen.blit(buy_more, (10, 315))
    buy_managers=font.render("Buy managers: ", True, "#ffffff")
    screen.blit(buy_managers, (10, 380))
    pygame.display.flip()

pygame.quit()