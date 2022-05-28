import pygame
import os 

WIDTH, HEIGHT = 600, 600 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("basic rpg")

FPS = 60

def draw_window():
    pygame.display.update()
    
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