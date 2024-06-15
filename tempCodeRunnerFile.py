game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    screen.fill(background)
    pygame.display.update()