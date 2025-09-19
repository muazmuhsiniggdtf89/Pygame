import pygame

# Initialize Pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game screen")


GREY = (58, 58, 58)


image = pygame.transform.scale(pygame.image.load("Game screen.png"), (500, 500))
image_rect = image.get_rect(center=(250, 250))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GREY)              
    screen.blit(image, image_rect)
    pygame.display.flip()          

pygame.quit()
