import pygame
from random import randint

pygame.init()

width, height = 600, 600
previous_key = pygame.K_UP  # начальное направление
speed_of_snake = 5  # скорость перемещение х у для элементов Snake
size_of_segments = 20
segments = [(width // 2, height // 2)]
apples = []
rect_of_head = pygame.Rect(0, 0, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
game_over = pygame.image.load("game_over.png")
font = pygame.font.SysFont("vrinda", 50)
score = 0
last_score = 0

game = True
loser = False


class Snake:
    def __init__(self, segment):
        self.speed = speed_of_snake
        self.segment = segment  # массив с кортежами для каждого элемента змеи начиная с головы
        self.length = 2  # начальная длина змеи
        self.direction = pygame.K_UP  # начальное направление змеи

    def move(self):
        global rect_of_head, loser
        x, y = self.segment[0]  # начальные координаты змеи до движение
        new_head = 0
        if self.direction == pygame.K_UP:
            new_head = (x, y - self.speed)  # координаты для головы меняются
        elif self.direction == pygame.K_DOWN:
            new_head = (x, y + self.speed)
        elif self.direction == pygame.K_LEFT:
            new_head = (x - self.speed, y)
        elif self.direction == pygame.K_RIGHT:
            new_head = (x + self.speed, y)

        rect_of_head = pygame.Rect(new_head, (size_of_segments, size_of_segments))
        self.segment.insert(0, new_head)  # добавляю новые координаты головы а старые координаты превращаются в его тело
        if len(self.segment) != self.length:  # если в длине сегмента по сути сбор голов не равен реальной длине змеи то значит она не сьела яблоко
            self.segment.pop()  # и соответственно надо убрать самую первую голову а значит хвост данной змеи

    def grow(self):
        self.length += 1

    def draw(self):
        for segmenta in self.segment:  # рисую каждый элемент в сегмент а значит каждый блок змеи начиная с головы
            pygame.draw.rect(screen, pygame.Color("Green"),
                             pygame.Rect(segmenta[0], segmenta[1], size_of_segments, size_of_segments))


class Apple:
    def __init__(self, segments):
        collision = True
        while collision:
            collision = False
            self.x = randint(size_of_segments, width - size_of_segments)
            self.y = randint(size_of_segments, height - size_of_segments)
            self.rect = pygame.Rect(self.x, self.y, size_of_segments, size_of_segments)
            for segment in segments:
                if self.rect.colliderect(pygame.Rect(segment[0], segment[1], size_of_segments, size_of_segments)):
                    collision = True
                    break

        apples.append(self)

    def draw(self):
        pygame.draw.rect(screen, pygame.Color("Red"), self.rect)


snake = Snake(segments)


def lose():
    global segments, snake, previous_key, apples, score, speed_of_snake,last_score
    segments = [(width // 2, height // 2)]
    previous_key = pygame.K_UP
    score_text = font.render(f"{score // 2}", True, (255, 255, 255))
    score = 0
    last_score=0
    snake = Snake(segments)
    apples = []
    screen.blit(game_over, (0, 0))
    screen.blit(score_text, (292, 280))
    speed_of_snake = 5


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
        elif event.type == pygame.KEYDOWN:
            if not loser:
                if event.key == pygame.K_UP and previous_key != pygame.K_DOWN:
                    previous_key = pygame.K_UP
                    snake.direction = pygame.K_UP
                elif event.key == pygame.K_DOWN and previous_key != pygame.K_UP:
                    previous_key = pygame.K_DOWN
                    snake.direction = pygame.K_DOWN
                elif event.key == pygame.K_LEFT and previous_key != pygame.K_RIGHT:
                    previous_key = pygame.K_LEFT
                    snake.direction = pygame.K_LEFT
                elif event.key == pygame.K_RIGHT and previous_key != pygame.K_LEFT:
                    previous_key = pygame.K_RIGHT
                    snake.direction = pygame.K_RIGHT
            elif loser:
                if event.key == pygame.K_SPACE:
                    loser = False

    if not loser:
        screen.fill(pygame.Color("Black"))
        if not apples:
            apples.append(Apple(snake.segment))  # Теперь добавляем экземпляр класса Apple в список
        for ap in apples:
            ap.draw()
            if ap.rect.colliderect(rect_of_head):
                apples.remove(ap)  # Удаляем яблоко из списка
                snake.grow()
                score += 1

        if (rect_of_head.right > width or rect_of_head.left < 0 or
                rect_of_head.bottom > height or rect_of_head.top < 0):
            loser = True
            lose()

        if score % 20 == 0 and last_score != score:
            last_score = score
            snake.speed += 2

        snake.move()
        if not loser:  # без него он рисует и змейка остается когда игра уже закончилась
            snake.draw()

    pygame.display.update()
    pygame.time.Clock().tick(60)
