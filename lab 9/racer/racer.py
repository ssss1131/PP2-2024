# убрал момент где road speed при проигрыше остается тем же


import random
import pygame

pygame.init()

width, height = 800, 800  # ширина и высота экрана
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer")
game = True  # для цикла while

gg = pygame.image.load("blue.png")
gg_rect = gg.get_rect()
gg.set_colorkey((255, 255, 255))
gg = gg.convert_alpha()
yellow_car = pygame.image.load("yellow.png")
white_car = pygame.image.load("red_2.png")
red_car = pygame.image.load("red.png")
yellow_2_car=pygame.image.load("yellow_2.png")
yellow_car.set_colorkey((255, 255, 255))  # это чтобы убрать задний белый фон
white_car.set_colorkey((255, 255, 255))
red_car.set_colorkey((255, 255, 255))
yellow_2_car.set_colorkey((255, 255, 255))
yellow_2_car=yellow_2_car.convert_alpha()
yellow_car = yellow_car.convert_alpha()  # это чтобы то что я убрал цвет зафиксировать тип
white_car = white_car.convert_alpha()
red_car = red_car.convert_alpha()
losed = pygame.image.load("loser.png")

coin_2 = pygame.image.load("coin_2.png")
coin_2_rect = coin_2.get_rect()
coin_5 = pygame.image.load("coin_5.png")
coin_5.set_colorkey((255, 255, 255))
coin_5 = coin_5.convert_alpha()
coin_5_rect = coin_5.get_rect()

road = pygame.image.load("road.png")
road_pos_1 = 0  # позиция первого это типа основная картинка
road_pos_2 = -height  # это уже как бы в два раза выше и он следует сразу за road_pos_1
road_speed = 5  # скорость перемещение бг

others = [yellow_car, white_car, red_car,yellow_2_car]
others_rect = [others[0].get_rect(), others[1].get_rect(),
               others[2].get_rect(),others[3].get_rect()]  # ну этим можно узнать их размеры по x and y
font = pygame.font.SysFont("vrinda", 50)  # загружаю его шрифт и размер
last_speed_increase_score = 0  # чтобы вызвать функцию level только один раз когда очки будут кратны 10
last_speed_increase_score_coins = 0

gg_x = 150  # координаты по x в начале игры
speed_of_gg = 18  # скорость перемещение гг
timer_for_target = True  # таймер чтобы после исчезновение а значит обнуление массива target он становится true и снова работает а если target не пустой то он false
speed_y = 15  # скорость перемещение врагов
speed_x = 15
speed_for_coin = 6
targets = []  # массив обьектов класса
score = 0  # очки сколько раз targets обнулялся
score_coins = 0
loser = False  # индикатор проигрыша
list_of_coin_2 = []  # лист с всеми обьектами класса Coin
list_of_coin_5 = []
timer_for_coins_2 = 100  # таймер чтобы не миллион раз появлялся
timer_for_coins_5 = 200


class Target:  # класс для создание обьекта врага
    def __init__(self, car):
        global timer_for_target
        car_image = others[car]
        self.car = car_image  # его фотка которая рандомно выбирается из массива фоток
        self.py = -100  # начальные координаты тачки
        self.px = random.randint(0, width - others_rect[car][2])  # координаты по ч х рандомно
        self.x = others_rect[car][2]  # присваеваю размер чтобы при столкновений знать
        self.y = others_rect[car][3]

        targets.append(self)
        timer_for_target = False

    def update(self):
        global timer_for_target, score, speed_y
        self.py += speed_y
        self.rect = pygame.Rect(self.px, self.py, self.x, self.y)
        if self.py > 800:
            targets.remove(self)
            timer_for_target = True  # когда таргетс пустой я сразу же делаю возможность чтобы снова создать новый обьект
            score += 1
            speed_y += 0.5
        screen.blit(self.car, (self.px, self.py))


# class SpecialTarget(Target):
#     def __init__(self, car):
#         super().__init__(car)  # чтобы наследовал все инициализации в родители не охота дублировать код
#         self.direction_x = random.choice([-1, 1])  # Направление движения по X: -1 (влево), 1 (вправо)
#         self.speed_x = random.randint(10, 20)  # Скорость движения по X
#
#     def update(self):
#         global timer_for_target, score
#         self.py += speed_y
#         self.px += self.direction_x * self.speed_x
#         # Изменение направления при достижении краев экрана
#         if self.px <= 0 or self.px + self.x >= width:
#             self.direction_x *= -1
#         self.rect = pygame.Rect(self.px, self.py, self.x, self.y)
#         if self.py > 800:
#             targets.remove(self)
#             timer_for_target = True
#             score += 1
#             speed_y += 0.5
#         screen.blit(self.car, (self.px, self.py))



class Coin:  # класс для создание монеток
    def __init__(self, lists, rect,
                 image):  # передается его лист его размеры и его фотка, лучше так чем делать два класса например
        self.coin_image = image
        self.x = rect[2]  # это размеры картинки по x
        self.y = rect[3]
        self.px = random.randint(0, width - self.x)  # отнимаю чтобы за границы игры не ушел
        self.py = -100
        lists.append(self)

    def update(self, lists):
        self.py += speed_for_coin
        self.rect = pygame.Rect(self.px, self.py, self.x, self.y)
        if self.py > height:
            lists.remove(self)
        screen.blit(self.coin_image, (self.px, self.py))


def lose():  # тут обнуляю все значение на изначальные, на самом деле мог бы создать какой то txt файл с изначальными мбмбмб
    global loser, targets, gg_x, timer_for_target, score, \
        speed_y, speed_of_gg, list_of_coin_5, list_of_coin_2, score_coins, road_speed,speed_x
    loser = True
    screen.blit(losed, (0, 0))
    targets = []
    gg_x = 400
    timer_for_target = True
    score_text = font.render(f"{score}", True, (150, 250, 123))
    screen.blit(score_coin_text,
                (width // 2 - score_coin_text.get_rect()[2] // 2, 456 + score_coin_text.get_rect()[3] + 40))
    screen.blit(score_text, (460, 456))
    score = 0
    score_coins = 0
    speed_y = 15
    speed_x = 15
    speed_of_gg = 18
    list_of_coin_5 = []
    list_of_coin_2 = []
    pygame.mixer.Sound("sound_when_collided.wav").play(0)
    road_speed = 5


def level():
    global speed_y, speed_of_gg, road_speed, speed_for_coin
    speed_y += 3
    speed_of_gg += 4
    road_speed += 3
    speed_for_coin += 1


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
            loser = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  #
                loser = False
                targets = []
                timer_for_target = True
                score = 0
                score_coins = 0
    if not loser:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if gg_x > 0:
                gg_x -= speed_of_gg  # если он не ушел за границу то двигаю налево
        elif keys[pygame.K_RIGHT]:
            if gg_x < width - gg_rect[2]:
                gg_x += speed_of_gg  # если не ушел за границу направо двигает
        gg_rect.x = gg_x  # меняю координаты rect of gg на нынешние чтобы colliderect работал корректно
        gg_rect.y = 600
        road_pos_1 += road_speed
        road_pos_2 += road_speed

        # Перемещение изображений дороги обратно наверх, если они полностью исчезли из поля зрения
        if road_pos_1 >= height:
            road_pos_1 = -height
        if road_pos_2 >= height:
            road_pos_2 = -height

        # Отрисовка дороги
        screen.blit(road, (0, road_pos_1))
        screen.blit(road, (0, road_pos_2))
        score_coin_text = font.render(f"Coins:{score_coins}", True, (0, 150, 50))
        screen.blit(score_coin_text, (width - score_coin_text.get_rect()[2] - 5, score_coin_text.get_rect()[3] - 15))
        screen.blit(gg, (gg_x, 600))
        if timer_for_target:
            t = Target(random.randint(0, 2))
        for target in targets:
            target.update()  # меняю координаты таргетов и бличу
            if gg_rect.colliderect(target):  # столкновение гг и таргетов
                lose()
        if score % 10 == 0 and score != last_speed_increase_score:  # апаю лвл если он кратен 10и и не равен последнему апу чтобы избежать много апание лвлов за раз до 11очка например
            level()
            last_speed_increase_score = score
        if timer_for_coins_2 == 50:
            c = Coin(list_of_coin_2, coin_2_rect, coin_2)
            timer_for_coins_2 = random.randint(200, 400)
        elif timer_for_coins_5 == 0:
            d = Coin(list_of_coin_5, coin_5_rect, coin_5)
            timer_for_coins_5 = 1000

        for coins in list_of_coin_2:
            coins.update(list_of_coin_2)
            if gg_rect.colliderect(coins):
                list_of_coin_2.remove(coins)
                score_coins += 2
        for coins in list_of_coin_5:
            coins.update(list_of_coin_5)
            if gg_rect.colliderect(coins):
                list_of_coin_5.remove(coins)
                score_coins += 5
        timer_for_coins_2 -= 1
        timer_for_coins_5 -= 1
        if score_coins % 10 == 0 and score_coins != last_speed_increase_score_coins:  # апаю лвл если он кратен 10и и не равен последнему апу чтобы избежать много апание лвлов за раз до 11очка например
            level()
            last_speed_increase_score_coins = score_coins

    pygame.time.Clock().tick(60)
    pygame.display.update()
