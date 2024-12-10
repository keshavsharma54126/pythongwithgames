import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000,800
PLAYER_WIDTH =50
PLAYER_HEIGHT =50
PLAYER_VEL=10

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space dodge")

BG = pygame.transform.scale(pygame.image.load("aDRySb.png"),(WIDTH,HEIGHT))
PLAYER_IMAGE = pygame.image.load("playerimage.png").convert_alpha()
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

FONT = pygame.font.SysFont("comicsans",20)

def draw(player_rect,elapsed_time):
    WIN.blit(BG, (0, 0))
    WIN.blit(PLAYER_IMAGE, player_rect)
    time_text = FONT.render(f"Time:{round(elapsed_time)}s",1,"white")
    WIN.blit(time_text,(10,10))
    pygame.display.update()

def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time=0

    while run:
        clock.tick(60)
        elapsed_time = time.time()-start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL+PLAYER_WIDTH<=WIDTH :
            player.x += PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y+ PLAYER_VEL+PLAYER_HEIGHT <= HEIGHT:
            player.y+=PLAYER_VEL
        if keys[pygame.K_UP] and player.y-PLAYER_VEL >=0:
            player.y-=PLAYER_VEL

        draw(player,elapsed_time)

    pygame.quit()

if __name__ == "__main__":
    main()