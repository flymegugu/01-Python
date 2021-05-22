# coding=utf-8
import pygame
import time


def main():
    # 1 创建窗口
    screen = pygame.display.set_mode((324, 650), 0, 32)
    # 2 创建背景图片
    background = pygame.image.load(
        r"C:\Users\HelloY\Desktop\study\1--Python\飞机大战\1.png")
    # 3 创建一个飞机图片
    hero = pygame.image.load(
        r"C:\Users\HelloY\Desktop\study\1--Python\飞机大战\2.png")

    while True:
        screen.blit(background, (0, 0))
        screen.blit(hero, (100, 600))
        pygame.display.update()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
