import pygame
from events import click
from include import colorlibrary, gamevariables
pygame.init()

pygame.display.set_icon(pygame.image.load('./images/pre-icon.png')) # Sets game logo

game_title="PROJECT B | (INSERT VERSION OF GAME LATER)" # ==== TITLE NEEDS TO BE CHANGED ====
screen=pygame.display.set_mode([500, 500], pygame.RESIZABLE) # I made the window smaller and resizable 
pygame.display.set_caption(game_title)
background=(colorlibrary.background_color) # ==== BACKGROUND IS TEMP ====
framerate=60
font=pygame.font.Font("freesansbold.ttf", 16) # ==== FONT IS TEMP ====
timer = pygame.time.Clock()

def draw_task(color, y_coord, value, draw, length, speed): # ==== COULD BE RENAMED ====
    global score
    if draw and length < 200:
        length += speed
    elif length >=200:
        draw=False
        length=0
        gamevariables.score+=value
    task = pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30]) # ==== FRAME ====
    pygame.draw.rect(screen, "#000000", [75, y_coord -10, 190, 20]) # ==== LOADER ====
    pygame.draw.rect(screen, color, [70, y_coord -15, length, 30])
    value_text=font.render(str(round(value,2)), True, colorlibrary.task_text_color) # ==== TEXT IS TEMP | SHOULD BE REPLACED WITH AN IMAGE LATER ====
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
    if gamevariables.task1_owned and not gamevariables.draw_task1:
        gamevariables.draw_task1=True
    if gamevariables.task2_owned and not gamevariables.draw_task2:
        gamevariables.draw_task2=True
    if gamevariables.task3_owned and not gamevariables.draw_task3:
        gamevariables.draw_task3=True
    if gamevariables.task4_owned and not gamevariables.draw_task4:
        gamevariables.draw_task4=True
    if gamevariables.task5_owned and not gamevariables.draw_task5:
        gamevariables.draw_task5=True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN: # ==== CLICKING TASKS && BUYING TASKS ====
            if task1.collidepoint(event.pos):
                gamevariables.draw_task1 = True
            if task2.collidepoint(event.pos):
                gamevariables.draw_task2 = True
            if task3.collidepoint(event.pos):
                gamevariables.draw_task3 = True
            if task4.collidepoint(event.pos):
                gamevariables.draw_task4 = True
            if task5.collidepoint(event.pos):
                gamevariables.draw_task5 = True
            if task1_manager_buy.collidepoint(event.pos) and gamevariables.score >= gamevariables.task1_manager_cost and not gamevariables.task1_owned:
                gamevariables.task1_owned=True
                gamevariables.score -= gamevariables.task1_manager_cost
            if task2_manager_buy.collidepoint(event.pos) and gamevariables.score >= gamevariables.task2_manager_cost and not gamevariables.task2_owned:
                gamevariables.task2_owned=True
                gamevariables.score -= gamevariables.task2_manager_cost
            if task3_manager_buy.collidepoint(event.pos) and gamevariables.score >= gamevariables.task3_manager_cost and not gamevariables.task3_owned:
                gamevariables.task3_owned=True
                gamevariables.score -= gamevariables.task3_manager_cost
            if task4_manager_buy.collidepoint(event.pos) and gamevariables.score >= gamevariables.task4_manager_cost and not gamevariables.task4_owned:
                gamevariables.task4_owned=True
                gamevariables.score -= gamevariables.task4_manager_cost
            if task5_manager_buy.collidepoint(event.pos) and gamevariables.score >= gamevariables.task5_manager_cost and not gamevariables.task5_owned:
                gamevariables.task5_owned=True
                gamevariables.score -= gamevariables.task5_manager_cost
            if task1_buy.collidepoint(event.pos) and gamevariables.score >= gamevariables.task1_cost:
                gamevariables.task1_value+=.15
                gamevariables.score -= gamevariables.task1_cost
                gamevariables.task1_cost+=1
            if task2_buy.collidepoint(event.pos) and gamevariables.score >= gamevariables.task2_cost:
                gamevariables.task2_value+=.3
                gamevariables.score -= gamevariables.task2_cost
                gamevariables.task2_cost+=2
            if task3_buy.collidepoint(event.pos) and gamevariables.score >= gamevariables.task3_cost:
                gamevariables.task3_value+=.6
                gamevariables.score -= gamevariables.task3_cost
                gamevariables.task3_cost+=3
            if task4_buy.collidepoint(event.pos) and gamevariables.score >= gamevariables.task4_cost:
                gamevariables.task4_value+=1.2
                gamevariables.score -= gamevariables.task4_cost
                gamevariables.task4_cost+=4
            if task5_buy.collidepoint(event.pos) and gamevariables.score >= gamevariables.task5_cost:
                gamevariables.task5_value+=2.4
                gamevariables.score -= gamevariables.task5_cost
                gamevariables.task5_cost+=5              
        elif event.type == pygame.MOUSEBUTTONUP:
            click.clicked(pygame.mouse.get_pos()) # clicking event
        
    screen.fill(background)
    
    # ==== DRAWING TASKS ====
    task1, gamevariables.task1_length, gamevariables.draw_task1 = draw_task(colorlibrary.task_color_odd, 50, gamevariables.task1_value, gamevariables.draw_task1, gamevariables.task1_length, gamevariables.task1_speed)
    task2, gamevariables.task2_length, gamevariables.draw_task2 = draw_task(colorlibrary.task_color_even, 100, gamevariables.task2_value, gamevariables.draw_task2, gamevariables.task2_length, gamevariables.task2_speed)
    task3, gamevariables.task3_length, gamevariables.draw_task3 = draw_task(colorlibrary.task_color_odd, 150, gamevariables.task3_value, gamevariables.draw_task3, gamevariables.task3_length, gamevariables.task3_speed)
    task4, gamevariables.task4_length, gamevariables.draw_task4 = draw_task(colorlibrary.task_color_even, 200, gamevariables.task4_value, gamevariables.draw_task4, gamevariables.task4_length, gamevariables.task4_speed)
    task5, gamevariables.task5_length, gamevariables.draw_task5 = draw_task(colorlibrary.task_color_odd, 250, gamevariables.task5_value, gamevariables.draw_task5, gamevariables.task5_length, gamevariables.task5_speed)
    
    # ==== BUY BUTTONS ARE TEMP | WILL ADD BUT MENU LATER ====
    task1_buy, task1_manager_buy = draw_buttons(colorlibrary.button_color_odd, 10, gamevariables.task1_cost, gamevariables.task1_owned, gamevariables.task1_manager_cost)
    task2_buy, task2_manager_buy = draw_buttons(colorlibrary.button_color_even, 70, gamevariables.task2_cost, gamevariables.task2_owned, gamevariables.task2_manager_cost)
    task3_buy, task3_manager_buy = draw_buttons(colorlibrary.button_color_odd, 130, gamevariables.task3_cost, gamevariables.task3_owned, gamevariables.task3_manager_cost)
    task4_buy, task4_manager_buy = draw_buttons(colorlibrary.button_color_even, 190, gamevariables.task4_cost, gamevariables.task4_owned, gamevariables.task4_manager_cost)
    task5_buy, task5_manager_buy = draw_buttons(colorlibrary.button_color_odd, 250, gamevariables.task5_cost, gamevariables.task5_owned, gamevariables.task5_manager_cost)
    
    display_score = font.render("Money: $"+str(round(gamevariables.score, 2)), True, "#ffffff", "#000000") # ==== REPLACE "Money" WITH CURRENCY NAME | MAYBE REPLACE $ WITH CURRENCY IMAGE ====
    screen.blit(display_score, (400,5))
    buy_more=font.render("Buy more: ", True, "#ffffff")
    screen.blit(buy_more, (10, 315))
    buy_managers=font.render("Buy managers: ", True, "#ffffff")
    screen.blit(buy_managers, (10, 380))
    pygame.display.flip()

pygame.quit()