import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров окна
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Размер ячейки и скорость змейки
cell_size = 20
snake_speed = 15

# Функция отрисовки змейки
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], cell_size, cell_size))

# Функция игры
def game():
    clock = pygame.time.Clock()
    game_over = False

    # Инициализация координат головы змейки
    x = width // 2
    y = height // 2

    # Инициализация начальной длины змейки и ее движения
    snake = [[x, y]]
    snake_length = 1
    direction = "right"

    # Инициализация координат красного яблока
    apple_x = random.randint(0, width - cell_size) // cell_size * cell_size
    apple_y = random.randint(0, height - cell_size) // cell_size * cell_size

    # Инициализация счетчика
    score = 0
    font = pygame.font.Font(None, 36)

    while not game_over:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Изменение направления движения змейки
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "down":
                    direction = "up"
                elif event.key == pygame.K_DOWN and direction != "up":
                    direction = "down"
                elif event.key == pygame.K_LEFT and direction != "right":
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    direction = "right"

        # Обновление координат головы змейки
        if direction == "up":
            y -= cell_size
            if y < 0:
                y = height - cell_size
        elif direction == "down":
            y += cell_size
            if y >= height:
                y = 0
        elif direction == "left":
            x -= cell_size
            if x < 0:
                x = width - cell_size
        elif direction == "right":
            x += cell_size
            if x >= width:
                x = 0

        # Проверка столкновения головы змейки с хвостом
        if [x, y] in snake[1:]:
            game_over = True

        # Проверка столкновения головы змейки с яблоком
        if x == apple_x and y == apple_y:
            # Увеличение длины змейки
            snake_length += 1

            # Генерация новых координат для яблока
            apple_x = random.randint(0, width - cell_size) // cell_size * cell_size
            apple_y = random.randint(0, height - cell_size) // cell_size * cell_size

            # Увеличение счетчика
            score += 1

        # Обновление координат змейки
        snake.insert(0, [x, y])
        if len(snake) > snake_length:
            snake.pop()

        # Заливка фона
        screen.fill(black)

        # Отрисовка змейки и яблока
        draw_snake(snake)
        pygame.draw.rect(screen, red, (apple_x, apple_y, cell_size, cell_size))

        # Отрисовка счетчика
        score_text = font.render("Score: " + str(score), True, white)
        screen.blit(score_text, (10, 10))

        # Обновление экрана
        pygame.display.flip()

        # Ограничение скорости змейки
        clock.tick(snake_speed)

    # Вывод сообщения о конце игры
    game_over_text = font.render("Game Over. Press Enter to Play Again", True, white)
    game_over_text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
    screen.blit(game_over_text, game_over_text_rect)
    pygame.display.flip()

    # Ожидание нажатия клавиши для перезапуска игры
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Перезапуск игры
                game()

# Запуск игры
game()