import pygame


pygame.init()


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


rect = pygame.Rect(0, 0, 120, 100)
rect.center = (320, 240)


font = pygame.font.Font(None, 60)  
text = font.render("Hello, Pygame!", True, BLACK)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)                 
    pygame.draw.rect(screen, BLUE, rect)  
    screen.blit(text, (200, 50))       
    pygame.display.flip()

pygame.quit()

