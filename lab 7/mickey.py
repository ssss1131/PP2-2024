import pygame, datetime

pygame.init()
clock = pygame.image.load("mickeyclock.jpeg")
size = clock.get_rect()  # тут 4 комплектующих 0 0 и его размеры по x and y
screen = pygame.display.set_mode((size[2], size[3]))
pygame.display.set_caption("Mickey clock")
fps = pygame.time.Clock()

sechand = pygame.image.load("sechand.png").convert_alpha()  # чуть быстрее альфа нужна так как у нас формат пнг
minhand = pygame.image.load("minhand.png").convert_alpha()
minhand_rect = minhand.get_rect()
minhand_rect.topleft = (size[2] // 2 - 210, size[3] // 2 - 90)
sechand_rect = sechand.get_rect()
sechand_rect.topleft = (size[2] // 2 - 275, size[3] // 2 - 70)

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            game = False
    screen.blit(clock, (0, 0))
    now = datetime.datetime.now()
    #print(now.minute)
    angle_minhand =-((now.minute+1) * 6) +90
    angle_sechand =-(now.second * 6) +90

    rotated_minhand = pygame.transform.rotate(minhand, angle_minhand)
    rotated_rect_minhand = rotated_minhand.get_rect()
    rotated_rect_minhand.center = minhand_rect.center
    topleft_x_minhand = minhand_rect.topleft[0] - (rotated_rect_minhand.width - minhand_rect.width) / 2
    topleft_y_minhand = minhand_rect.topleft[1] - (rotated_rect_minhand.height - minhand_rect.height) / 2

    rotated_sechand = pygame.transform.rotate(sechand, angle_sechand)
    rotated_rect_sechand = rotated_sechand.get_rect()
    rotated_rect_sechand.center = sechand_rect.center
    topleft_x_sechand = sechand_rect.topleft[0] - (rotated_rect_sechand.width - sechand_rect.width) / 2
    topleft_y_sechand = sechand_rect.topleft[1] - (rotated_rect_sechand.height - sechand_rect.height) / 2

    screen.blit(rotated_minhand, (topleft_x_minhand, topleft_y_minhand))
    screen.blit(rotated_sechand, (topleft_x_sechand, topleft_y_sechand))

    fps.tick(60)

    pygame.display.update()
