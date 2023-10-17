import pygame
pygame.init()

game_title="PROJECT B | (INSERT VERSION OF GAME LATER)" # ==== TITLE NEEDS TO BE CHANGED ====
screen=pygame.display.set_mode([500, 500], pygame.RESIZABLE) # I made the window smaller and resizable 
pygame.display.set_caption(game_title)
background=("#000000") # ==== BACKGROUND IS TEMP ====
framerate=60
font=pygame.font.Font("freesansbold.ttf", 16) # ==== FONT IS TEMP ====
timer = pygame.time.Clock()

def draw_task(color, y_coord): # ==== COULD BE RENAMED ====
    pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, color, [75, y_coord -10, 190, 20])

running=True
while running:
    timer.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        
    screen.fill(background)
    draw_task("#088F8F", 50)
    pygame.display.flip()

pygame.quit()