# coding=utf-8
import pygame
import time

from pygame.constants import KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, K_a, K_d, QUIT


def main():
    # 1 创建窗口
    screen = pygame.display.set_mode((324, 650), 0, 32)
    # 2 创建背景图片
    background = pygame.image.load(
        r"C:\Users\HelloY\Desktop\study\1--Python\飞机大战\1.png")
    # 3 创建一个飞机图片
    hero = pygame.image.load(
        r"C:\Users\HelloY\Desktop\study\1--Python\飞机大战\2.png")
    y = 600
    x = 100
    while True:
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    x -= 5
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    x += 5
                elif event.key == K_SPACE:
                    print("space")

        time.sleep(0.01)


if __name__ == "__main__":
    main()
