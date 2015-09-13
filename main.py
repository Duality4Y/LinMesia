import pygame
from pygame.locals import *
import sys
import fluidsynth


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

size = width, height = (800, 700)
pygame.display.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("LinMesia")

clock = pygame.time.Clock()

soundfont = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
fs = fluidsynth.Synth()
fs.start()

sfid = fs.sfload(soundfont)
fs.program_select(0, sfid, 0, 0)


class PianoKey(object):
    def __init__(self, pos, width, height, is_sharp, keymap=None):
        self.pos = pos
        self.width = width
        self.height = height

        self.hitColor = GREEN
        if(is_sharp):
            self.normColor = BLACK
        else:
            self.normColor = WHITE
        self.color = self.normColor

        self.is_sharp = is_sharp
        self.keymap = keymap
        self.channel = 0
        self.note = 60
        self.velocity = 30
        self.synth = fs

    def draw(self, screen):
        x, y = self.pos
        rect = (x, y, self.width, self.height)
        if self.is_sharp:
            pygame.draw.rect(screen, self.color, rect, 0)
            pygame.draw.rect(screen, BLACK, rect, 1)
        else:
            pygame.draw.rect(screen, self.color, rect, 0)
            pygame.draw.rect(screen, BLACK, rect, 1)

    def handleInput(self, input):
        if event.type == pygame.KEYDOWN:
            if event.key == self.keymap:
                self.color = self.hitColor
                self.synth.noteon(self.channel, self.note, self.velocity)
                print("key pressed: %d" % (self.keymap))
                print("Channel: %d, Note: %d, Velocity: %d")
        elif event.type == pygame.KEYUP:
            if event.key == self.keymap:
                self.color = self.normColor
                print("key released: %d" % (self.keymap))

    def setpos(self, pos):
        self.pos = pos


class Octave(object):
    def __init__(self, pos, width=140, height=100, length=7):
        self.pos = pos

        self.height = height
        self.width = width
        self.keyWidth = width / 7
        self.keyHeight = height

        self.length = 7

        # map to values. last 5 are sharps
        self.keymap = ['a', 's', 'd', 'f', 'g', 'h', 'j',
                       'w', 'e', 't', 'y', 'u']
        for i, value in enumerate(self.keymap):
            self.keymap[i] = ord(value)

        self.keys = {}
        self.placekeys()

    def placekeys(self):
        # if keys already exist delete them
        if len(self.keys):
            self.keys = []
        # keep track on which keys we are.
        keynum = 0
        # first add non sharp keys.
        x, y = self.pos
        for i in range(0, self.length):
            # keypos = (x, y + (i * self.keyWidth))
            keypos = (x + (i * self.keyWidth), y)
            print(keynum)
            key = PianoKey(keypos, self.keyWidth, self.keyHeight, 0,
                           self.keymap[keynum])
            self.keys[keynum] = key
            keynum += 1
            # self.keys.append(key)

        # add sharp keys, note last 5 keys are sharps
        skeywidth = self.keyWidth * 0.6
        skeyheight = (self.keyHeight / 2) + 8
        # position is the position of key - half the sharp keys width.
        for i in range(1, self.length):
            if i != 3:
                keypos = (x + (i * self.keyWidth - skeywidth / 2), y)
                key = PianoKey(keypos, skeywidth, skeyheight, 1,
                               self.keymap[keynum])
                self.keys[keynum] = key
                keynum += 1
                # self.keys.append(key)

    def draw(self, screen):
        for key in self.keys:
            self.keys[key].draw(screen)
        # key.draw(screen)
        # skey.draw(screen)
        # pass

    def handleInput(self, input):
        for key in self.keys:
            self.keys[key].handleInput(input)

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


key = PianoKey((10, 10), 20, 100, False)
skey = PianoKey((20, 10), 20, 50, True)

octaveHeight = int(140)
octave = Octave((0, height - octaveHeight), 200, octaveHeight)
# octavetwo = Octave((octave.getwidth(), height - octave.getheight()))

if __name__ == "__main__":
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                octave.handleInput(event)
            elif event.type == pygame.KEYUP:
                octave.handleInput(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        screen.fill(GRAY)
        octave.draw(screen)
        # octavetwo.draw(screen)
        pygame.display.flip()
        clock.tick(20)
