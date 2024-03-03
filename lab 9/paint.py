import pygame

pygame.init()

width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint")
white = (255, 255, 255)
screen.fill(white)  # Заливаем фон цветом

palette_colors = [
    (0, 0, 0),  # Черный
    (255, 165, 0),  # Оранжевый
    (255, 0, 0),  # Красный
    (0, 255, 0),  # Зеленый
    (0, 0, 255),  # Синий
    (255, 255, 0),  # Желтый
    (0, 255, 255),  # Голубой (Циан)
    (255, 0, 255),  # Пурпурный (Маджента)
]

current_color = palette_colors[0]  # Текущий цвет для рисования
last_pos_cursor = None  # Последняя позиция курсора
num_colors = len(palette_colors)
palette_width = width // num_colors
palette_height = 30
changer_of_color = False
eraser = False
thickness = 5

drawing_circle = False
start_pos_circle = None
circle_radius = 0
drawing_rectangle = False
start_pos_rectangle = None
drawing_square = False
start_pos_square = None
drawing_triangle = False
start_pos_triangle = None
drawing_right_triangle = False
start_pos_right_triangle = None
drawing_rhombus = False
start_pos_rhombus = None


def draw_palette():
    for i, color in enumerate(palette_colors):
        pygame.draw.rect(screen, color, (i * palette_width, height - palette_height, palette_width, palette_height))


def draw_line(pos):
    global last_pos_cursor
    if last_pos_cursor is not None:
        pygame.draw.line(screen, current_color, last_pos_cursor, pos, thickness)
    last_pos_cursor = pos


game = True
while game:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                current_color = white
                thickness = 50
            elif event.key == pygame.K_c:
                drawing_circle = True
            elif event.key == pygame.K_r:
                drawing_rectangle = True
            elif event.key == pygame.K_MINUS:
                if thickness > 2:
                    thickness -= 2
            elif event.key == pygame.K_EQUALS:
                if thickness <= 17:
                    thickness += 2
            elif event.key == pygame.K_s:
                drawing_square = True
            elif event.key == pygame.K_t:
                drawing_triangle = True
            elif event.key == pygame.K_y:
                drawing_right_triangle = True
            elif event.key == pygame.K_h:
                drawing_rhombus = True


            elif event.key == pygame.K_0:
                screen.fill(white)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_y < height - palette_height:
                last_pos_cursor = pygame.mouse.get_pos()
            else:
                changer_of_color = True
            if drawing_circle and start_pos_circle is None:
                start_pos_circle = pygame.mouse.get_pos()
            elif drawing_rectangle and start_pos_rectangle is None:
                start_pos_rectangle = pygame.mouse.get_pos()
            elif drawing_square and start_pos_square is None:
                start_pos_square = pygame.mouse.get_pos()
            elif drawing_triangle and start_pos_triangle is None:
                start_pos_triangle = pygame.mouse.get_pos()
            elif drawing_right_triangle and start_pos_right_triangle is None:
                start_pos_right_triangle = pygame.mouse.get_pos()
            elif drawing_rhombus and start_pos_rhombus is None:
                start_pos_rhombus = pygame.mouse.get_pos()


        elif event.type == pygame.MOUSEBUTTONUP:
            last_pos_cursor = None
            drawing_circle = False
            drawing_rectangle = False
            start_pos_circle = None
            start_pos_rectangle = None
            drawing_square = False
            start_pos_square = None
            drawing_triangle = False
            start_pos_triangle = None
            drawing_right_triangle = False
            start_pos_right_triangle = None
            drawing_rhombus = False
            start_pos_rhombus = None

    if pygame.mouse.get_pressed()[0] and not (
            drawing_rectangle or drawing_circle or drawing_triangle or drawing_square or drawing_right_triangle or drawing_rhombus):  # Если зажата левая кнопка мыши
        draw_line(pygame.mouse.get_pos())

    if changer_of_color:
        current_color = palette_colors[mouse_x // palette_width]
        thickness = 5
        changer_of_color = False

    if pygame.mouse.get_pressed()[0] and drawing_circle and start_pos_circle is not None:
        end_pos_circle = pygame.mouse.get_pos()
        circle_radius = int(((end_pos_circle[0] - start_pos_circle[0]) ** 2 + (
                    end_pos_circle[1] - start_pos_circle[1]) ** 2) ** 0.5)  # Вычисляем радиус
        pygame.draw.circle(screen, current_color, start_pos_circle, circle_radius)
    if pygame.mouse.get_pressed()[0] and drawing_square and start_pos_square is not None:
        end_pos_square = pygame.mouse.get_pos()
        square_size = max(abs(end_pos_square[0] - start_pos_square[0]), abs(end_pos_square[1] - start_pos_square[
            1]))  # убираем с конечных x and y начальные и в их модуле находим макс для размеров
        pygame.draw.rect(screen, current_color, (start_pos_square[0], start_pos_square[1], square_size, square_size))

    if pygame.mouse.get_pressed()[0] and drawing_rectangle:
        end_pos_rectangle = pygame.mouse.get_pos()  # Рассчитываем координаты и размеры прямоугольника
        rect_x = min(start_pos_rectangle[0], end_pos_rectangle[0])
        rect_y = min(start_pos_rectangle[1], end_pos_rectangle[1])
        rect_width = abs(end_pos_rectangle[0] - start_pos_rectangle[0])
        rect_height = abs(end_pos_rectangle[1] - start_pos_rectangle[1])
        pygame.draw.rect(screen, current_color, (rect_x, rect_y, rect_width, rect_height))
        previous_rect_x = rect_x
        previous_rect_y = rect_y
    if pygame.mouse.get_pressed()[0] and drawing_triangle and start_pos_triangle is not None:
        end_pos_triangle = pygame.mouse.get_pos()
        side_length = int(((end_pos_triangle[0] - start_pos_triangle[0]) ** 2 + (
                end_pos_triangle[1] - start_pos_triangle[1]) ** 2) ** 0.5)
        # Высота равностороннего треугольника
        height_triangle = (side_length * (3 ** 0.5)) / 2
        # Вершины треугольника
        vertex1 = start_pos_triangle
        vertex2 = (start_pos_triangle[0] + side_length, start_pos_triangle[1])
        vertex3 = (start_pos_triangle[0] + side_length / 2, start_pos_triangle[1] - height_triangle)

        pygame.draw.polygon(screen, current_color, [vertex1, vertex2, vertex3])

    if pygame.mouse.get_pressed()[0] and drawing_right_triangle and start_pos_right_triangle is not None:
        end_pos_right_triangle = pygame.mouse.get_pos()
        side_length_x = abs(start_pos_right_triangle[0]-end_pos_right_triangle[0])
        side_length_y = abs(start_pos_right_triangle[1]-end_pos_right_triangle[1])
        vertex_1 = start_pos_right_triangle
        vertex_2 = (start_pos_right_triangle[0]+side_length_x,start_pos_right_triangle[1])
        vertex_3 = (start_pos_right_triangle[0],start_pos_right_triangle[1]-side_length_y)
        pygame.draw.polygon(screen,current_color,[vertex_1,vertex_2,vertex_3])

    if pygame.mouse.get_pressed()[0] and drawing_rhombus and start_pos_rhombus is not None:
        end_pos_rhombus = pygame.mouse.get_pos()
        diagonal_length = int(((end_pos_rhombus[0] - start_pos_rhombus[0]) ** 2 + (
                    end_pos_rhombus[1] - start_pos_rhombus[1]) ** 2) ** 0.5) / 2
        vertex_1 = (start_pos_rhombus[0], start_pos_rhombus[1] - diagonal_length)
        vertex_2 = (start_pos_rhombus[0] + diagonal_length, start_pos_rhombus[1])
        vertex_3 = (start_pos_rhombus[0], start_pos_rhombus[1] + diagonal_length)
        vertex_4 = (start_pos_rhombus[0] - diagonal_length, start_pos_rhombus[1])
        pygame.draw.polygon(screen, current_color, [vertex_1, vertex_2, vertex_3, vertex_4])




    draw_palette()
    pygame.display.update()
    pygame.time.Clock().tick(60)
