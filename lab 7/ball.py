import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))

game = True
x = 150
y = 150
dx = 20
dy = 20


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if y>35:
            y -= dy
    elif keys[pygame.K_DOWN]:
        if y < 565:
            y += dy
    elif keys[pygame.K_LEFT]:
        if x > 30:
            x -= dx
    elif keys[pygame.K_RIGHT]:
        if x < 565:
            x += dx

    print(x,y)
    screen.fill(pygame.Color("white"))
    pygame.draw.circle(screen, pygame.Color("black"), (x, y), 25)

    pygame.time.Clock().tick(60)
    pygame.display.update()
