import pygame

from pygame.locals import *
from cloth import Cloth

def update_fps():
	fps = f"FPS: {str(int(clock.get_fps()))}"
	return text_render(fps)

def text_render(string):
    return font.render(string, 1, pygame.Color("white"))
 
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
 
gameOn = True
update_count = 0

cloth = Cloth(200,10,20,20,20)
cloth.generate_points()

while gameOn:
    clock.tick(120)
    update_count+=1

    left, middle, right = pygame.mouse.get_pressed()
    if left:
        cloth.mouse_click(pygame.mouse.get_pos())
    if not left:
        cloth.mouse_reset()

    #Create background
    screen.fill((0,0,0))

    #Update fps
    screen.blit(update_fps(), (10,0))
    screen.blit(text_render(f"Frame #: {update_count}"), (10,30))
    
    cloth.update(clock.get_time()/1000)

    for stick in cloth.sticks:
        pygame.draw.line(screen, (120,120,255), (stick[0][0], stick[0][1]), (stick[1][0], stick[1][1]))

    # Update the display using flip
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False
            pygame.quit()
            continue

pygame.quit()