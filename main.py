import pygame
import sys


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)


class PianoKey(object):
    def __init__(self, pos, width, height, is_sharp):
        self.pos = pos
        self.width = width
        self.height = height
        self.baseColor = WHITE
        self.color = WHITE
        self.is_sharp = is_sharp

    def draw(self, screen):
        x, y = self.pos
        rect = (x, y, self.width, self.height)
        if self.is_sharp:
            pygame.draw.rect(screen, BLACK, rect, 0)
            pygame.draw.rect(screen, GRAY, rect, 1)
        else:
            pygame.draw.rect(screen, WHITE, rect, 0)
            pygame.draw.rect(screen, BLACK, rect, 1)

    def handleInput(self, input):
        pass

    def setpos(self, pos):
        self.pos = pos


class Octave(object):
    def __init__(self, pos, width=None, height=None):
        self.pos = pos

        self.keyWidth = 20
        self.keyHeight = 100

        self.length = 8
        if height:
            self.height = height
        else:
            self.height = 100
        if width:
            self.width = width
        else:
            self.width = self.keyWidth * self.length

        self.keys = []
        self.placekeys()

    def placekeys(self):
        # if keys already exist delete them
        if len(self.keys):
            self.keys = []
        # first add non sharp keys.
        x, y = self.pos
        for i in range(0, self.length):
            # keypos = (x, y + (i * self.keyWidth))
            keypos = (x + (i * self.keyWidth), y)
            key = PianoKey(keypos, self.keyWidth, self.keyHeight, 0)
            self.keys.append(key)
        # add sharp keys
        skeywidth = self.keyWidth * 0.6
        skeyheight = self.keyHeight / 3
        # position is the position of key - half the sharp keys width.
        for i in range(1, self.length):
            if i != 3 and i != 4:
                keypos = (x + (i * self.keyWidth - skeywidth / 2), y)
                key = PianoKey(keypos, skeywidth, skeyheight, 1)
                self.keys.append(key)

    def draw(self, screen):
        for key in self.keys:
            key.draw(screen)
        # key.draw(screen)
        # skey.draw(screen)
        # pass

    def handleInput(self, input):
        pass

    def getpos(self):
        return self.pos

    def getwidth(self):
        return self.width

    def getheight(self):
        return self.height

    def setpos(self, pos):
        self.pos = pos
        self.placekeys()

    def setwidth(self, width):
        self.width = width
        self.placekeys()

    def setheight(self, height):
        self.height = height
        self.placekeys()


class Piano(object):
    def __init__(self, number_octaves):
        self.num_octaves = number_octaves

    def draw(self, screen):
        pass

    def handleInput(self, input):
        pass

pygame.init()

size = width, height = (800, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("LinMesia")

clock = pygame.time.Clock()

key = PianoKey((10, 10), 20, 100, False)
skey = PianoKey((20, 10), 20, 50, True)

octave = Octave((0, 0))
octave.setpos((0, height - octave.getheight()))
octavetwo = Octave((octave.getwidth(), height - octave.getheight()))


if __name__ == "__main__":
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                octave.handleInput(event)
            elif event.type == pygame.KEYUP:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        screen.fill(GRAY)
        octave.draw(screen)
        octavetwo.draw(screen)
        pygame.display.flip()
        clock.tick(60)
