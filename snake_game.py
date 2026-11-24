import pygame
import sys

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

snake_color = (0, 255, 0)
food_color = (255, 0, 0)
block_size = 20

snake = [(100, 100), (80, 100), (60, 100)]
food = (300, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    for segment in snake:
        pygame.draw.rect(screen, snake_color, (segment[0], segment[1], block_size, block_size))
    pygame.draw.rect(screen, food_color, (food[0], food[1], block_size, block_size))
    pygame.display.flip()
    pygame.time.delay(100)