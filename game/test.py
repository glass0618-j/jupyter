import pygame
import random

pygame.init()

background = pygame.image.load("background3.png") 
pygame.display.set_caption("test pygame")
screen_width = 475
screen_height = 583
screen = pygame.display.set_mode((screen_width,screen_height))

character = pygame.image.load("character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = screen_width/2-character_width/2
character_ypos = screen_height - character_height

poo = pygame.image.load("poo2.png")
poo_size = poo.get_rect().size
poo_width = poo_size[0]
poo_height = poo_size[1]
poo_xpos = 0
poo_ypos = poo_height

start_ticks = pygame.time.get_ticks()

game_font = pygame.font.Font(None,40)

poo_speed = 1
clock = pygame.time.Clock()
character_speed = 0.5
to_x = 0
running = True
_running = True

while _running:
    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= character_speed
                if event.key == pygame.K_RIGHT:
                    to_x += character_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
        character_xpos += to_x*dt

        if character_xpos < 0:
            character_xpos = 0
        elif character_xpos > screen_width - character_width:
            character_xpos = screen_width - character_width
        if character_ypos < 0:
            character_ypos = 0
        elif character_ypos > screen_height - character_height:
            character_ypos = screen_height-character_height
        if poo_ypos >= screen_height + 70 or poo_ypos == 70:
            poo_ypos = poo_height
            poo_xpos = random.uniform(0, screen_width - character_width)
    
        poo_ypos += poo_speed
        poo_speed += 0.01

        character_rect = character.get_rect()
        character_rect.left = character_xpos
        character_rect.top = character_ypos

        poo_rect = character.get_rect()
        poo_rect.left = poo_xpos
        poo_rect.top = poo_ypos

        if character_rect.colliderect(poo_rect):
            running = False
    
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_ticks)/1000
        timer = game_font.render(str(int(elapsed_time)),True,(255,255,255))

        screen.blit(background,(0,0))
        screen.blit(character,(character_xpos,character_ypos))
        screen.blit(poo,(poo_xpos,poo_ypos))
        screen.blit(timer,(10,10))
        pygame.display.update()
    
    score_font = pygame.font.Font(None,50)
    text = score_font.render("Your score is",True,(255,255,255))
    text_rect = text.get_rect()
    timer_rect = timer.get_rect()
    screen.fill((0,0,0))
    screen.blit(timer,(10,50))
    screen.blit(text,(10,10))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _running = False

pygame.quit()
