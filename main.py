import pygame
import sys


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)


class PianoKey(object):
    def __init__(self, pos, width, height, is_sharp):
        self.pos = pos
        self.width = width
        self.height = height
        self.is_sharp = is_sharp

    def draw(self, screen):
        x, y = self.pos
        rect = (x, y, self.width, self.height)
        if self.is_sharp:
            pygame.draw.rect(screen, BLACK, rect, 0)
        else:
            pygame.draw.rect(screen, WHITE, rect, 0)
            pygame.draw.rect(screen, BLACK, rect, 2)


class Octave(object):
    def __init__(self, pos, width, height):
        self.pos = pos
        self.height = height

    def draw(self, screen):
        pass


class Piano(object):
    def __init__(self, number_octaves):
        self.num_octaves = number_octaves

    def draw(self, screen):
        pass

pygame.init()

size = width, height = (800, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("LinMesia")

clock = pygame.time.Clock()

key = PianoKey((10, 10), 20, 100, False)
skey = PianoKey((20, 10), 20, 50, True)

if __name__ == "__main__":
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                pass
            elif event.type == pygame.KEYUP:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        screen.fill(GRAY)
        key.draw(screen)
        skey.draw(screen)
        pygame.display.flip()
        clock.tick(60)
