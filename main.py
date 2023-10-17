import pygame
pygame.init()

game_title="PROJECT B | (INSERT VERSION OF GAME LATER)" # ==== TITLE NEEDS TO BE CHANGED ====
screen=pygame.display.set_mode([1920, 1080])
pygame.display.set_caption(game_title)
background=("#000000") # ==== BACKGROUND IS TEMP ====
framerate=60
font=pygame.font.Font("freesansbold.ttf", 16) # ==== FONT IS TEMP ====
timer = pygame.time.Clock()

running=True
while running:
    timer.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        
    screen.fill(background)
    pygame.display.flip()

pygame.quit()