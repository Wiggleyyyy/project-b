import pygame

pygame. init()

WIDTH=500
HEIGHT=500
screen=pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("TITLE")
fps=60
timer = pygame.time.Clock()

menu=False

font= pygame.font.Font("freesansbold.ttf", 24)

def draw_game():
    menu_btn=pygame.draw.rect(screen, "light gray", [230 , 450, 260, 40], 0, 5)
    pygame.draw.rect(screen, "dark gray", [230, 450, 260, 40], 5, 5)
    text=font.render("menu", True, "black")
    screen.blit(text, (245, 457))
    if menu_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        menu= True
    else:
        menu=False
    return menu

def draw_menu():
    pygame.draw.rect(screen, "white", [100, 100, 300, 300])
    # exit menu button
    menu_btn=pygame.draw.rect(screen, "light gray", [120 , 350, 260, 40], 0, 5)
    pygame.draw.rect(screen, "dark gray", [120, 350, 260, 40], 5, 5)
    text=font.render("exit menu", True, "black")
    screen.blit(text, (135, 357))
    if menu_btn.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        menu= False
    else:
        menu=True
    return menu


run=True
while run:
    screen.fill("#000000")
    timer.tick(fps)

    if menu:
        menu= draw_menu()
    else:
        menu = draw_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            
    pygame.display.flip()
pygame.quit()