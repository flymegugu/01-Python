# coding=utf-8
import pygame
import time

from pygame.constants import KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, K_a, K_d, QUIT


class HeroPlan(object):
    def __init__(self, screen_temp) -> None:
        super().__init__()
        self.x = 100
        self.y = 600
        self.screen = screen_temp
        self.image = pygame.image.load(
            r"C:\Users\HelloY\Desktop\study\1--Python\飞机大战\2.png")
# 创建一个飞机图片

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def key_control(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    self.move_left()
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    self.move_right()
                elif event.key == K_SPACE:
                    print("space")


def main():
    # 1 创建窗口
    screen = pygame.display.set_mode((324, 650), 0, 32)
    # 2 创建背景图片
    background = pygame.image.load(
        r"C:\Users\HelloY\Desktop\study\1--Python\飞机大战\1.png")
    # 3 创建飞机对象
    hero = HeroPlan(screen)
    while True:
        screen.blit(background, (0, 0))
        hero.display()
        pygame.display.update()
        hero.key_control()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
