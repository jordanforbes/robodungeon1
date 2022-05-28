import pygame 
import os

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robo Dungeon")

#bgcolor
WHITE = (255,255,255)
BLACK =(0,0,0)

FPS = 60

BACKGROUND_IMG = pygame.image.load(os.path.join('Assets', 'bg.PNG'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMG,(600,600))

def draw_window():
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND, (0,0))
    pygame.display.update()

def main():
    clock = pygame.time.Clock() #controls refresh rate
    run = True 
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
        draw_window()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()