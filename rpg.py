import pygame
import os 

WIDTH, HEIGHT = 600, 600 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("basic rpg")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

MENU = pygame.Rect(WIDTH//2, 20, 10, 400)

FPS = 60

def draw_window():
    pygame.display.update()
    pygame.draw.rect(WIN, RED, MENU)
    
def main():
    clock = pygame.time.Clock()
    run = True  
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
        draw_window() 
    
    pygame.quit()
    
if __name__== "__main__":
    main()  