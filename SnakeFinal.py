import pygame
import math
import random

pygame.init()
clock = pygame.time.Clock()
width = 800
hieght = 600
dis = pygame.display.set_mode((width, hieght))


def body(dis, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(dis, (0, 0, 200), [x, y, 10, 10])


def food_eaten(foodX, foodY, snakeX, snakeY):
    distance = math.sqrt(math.pow(foodX - snakeX, 2) +
                         (math.pow(foodY - snakeY, 2)))
    return distance


def game_loop():
    game_over = False
    running = True
    score = 0
    snakeX = 400
    snakeY = 300
    snakeX_change = 0
    snakeY_change = 0
    snake_list = []
    snake_len = 1
    foodX = random.randrange(5, 795, 10)
    foodY = random.randrange(5, 595, 10)
    font = pygame.font.Font('Headcorps.ttf', 25)
    over = pygame.font.Font('Headcorps.ttf', 64)
    tentX = 270
    textY = 250
    while running:
        if game_over:
            dis.fill((255, 255, 255))
            if score >= 100:
                win = over.render("YOU WON!", True, (255, 0, 0))
                retry = font.render(
                    "Press enter to play again", True, (255, 0, 0))
                dis.blit(win, (tentX + 10, textY))
                dis.blit(retry, (tentX - 5, textY + 70))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            game_loop()
            else:
                lose = over.render("YOU LOST!", True, (255, 0, 0))
                retry = font.render(
                    "Press enter to try again", True, (255, 0, 0))
                dis.blit(lose, (tentX, textY))
                dis.blit(retry, (tentX - 5, textY + 70))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            game_loop()
            pygame.display.update()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        snakeX_change = -5
                        snakeY_change = 0
                    if event.key == pygame.K_RIGHT:
                        snakeX_change = 5
                        snakeY_change = 0
                    if event.key == pygame.K_UP:
                        snakeY_change = -5
                        snakeX_change = 0
                    if event.key == pygame.K_DOWN:
                        snakeY_change = 5
                        snakeX_change = 0
            dis.fill((0, 150, 0))
            snake_head = []
            snake_head.append(snakeX)
            snake_head.append(snakeY)
            snake_list.append(snake_head)

            if len(snake_list) > snake_len:
                del snake_list[0]

            if food_eaten(foodX, foodY, snakeX, snakeY) <= 5:
                foodX = random.randrange(5, 795, 5)
                foodY = random.randrange(5, 595, 5)
                snake_len += 5
                score += 1

            if snake_head in snake_list[:-1]:
                game_over = True

            if score >= 100:
                game_over = True

            pygame.draw.rect(dis, (200, 0, 0), (foodX, foodY, 10, 10))
            snakeY += snakeY_change
            snakeX += snakeX_change

            if snakeX >= 799:
                snakeX = 2
            if snakeX <= 1:
                snakeX = 798
            if snakeY >= 599:
                snakeY = 2
            if snakeY <= 1:
                snakeY = 598
            score_display = font.render(
                "Score: "+str(score), True, (255, 0, 0))
            dis.blit(score_display, (5, 5))

            body(dis, snake_list)

            clock.tick(25)
            pygame.display.update()


game_loop()
