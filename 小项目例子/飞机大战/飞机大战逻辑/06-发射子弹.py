# coding=utf-8
import pygame
import time

from pygame.constants import KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, K_a, K_d, QUIT


class HeroPlan(object):
    def __init__(self, screen_temp) -> None:
        super().__init__()
        self.x = 210
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load(
            r"C:\Users\HelloY\Desktop\study\1--Python\飞机大战\picture\hero1.png")
        self.bullet_list = []
# 创建一个飞机图片

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        # 使用飞机类中的screen，反正都是用于和屏幕建立连接
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

# 子弹


class Bullet(object):
    def __init__(self, screen_temp, x, y) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load(
            r"C:\Users\HelloY\Desktop\study\1--Python\飞机大战\picture\bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


def key_control(hero_temp):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                hero_temp.move_right()
            elif event.key == K_SPACE:
                print("space")
                hero_temp.fire()


def main():
    # 1 创建窗口

    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 2 创建背景图片
    background = pygame.image.load(
        r"C:\Users\HelloY\Desktop\study\1--Python\飞机大战\picture\background.png")
    # 3 创建飞机对象
    hero = HeroPlan(screen)
    while True:
        screen.blit(background, (0, 0))
        hero.display()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
