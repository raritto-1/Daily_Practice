import pygame

pygame.init()
width = int(input('Enter the width: '))
height = int(input('Enter the height: '))
screen = pygame.display.set_mode((width, height))
background = (255, 255, 255)  # White background

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    screen.fill(background)
    pygame.display.update()

pygame.quit()