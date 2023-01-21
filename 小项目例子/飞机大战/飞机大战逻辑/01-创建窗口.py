# coding=utf-8
import pygame
import time


def main():
    screen = pygame.display.set_mode((324, 650), 0.32)
    background = pygame.image.load(
        r"C:\Users\HelloY\Desktop\study\1--Python\飞机大战\1.png")
    while True:
        screen.blit(background, (0, 0))
        pygame.display.update()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
