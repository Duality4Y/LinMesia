
import sys
import os
import pygame
from pygame.locals import *
from mingus.containers import Note
from mingus.midi import fluidsynth


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

fluidsynth.init("/usr/share/sounds/sf2/FluidR3_GM.sf2", "alsa")
fluidsynth.set_instrument(0, 0)

# banknum = 0
# # presetnum sets the instrument
# presetnum = 0
# channel = 0

# soundfont = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
# fs = fluidsynth.Synth()
# fs.start()

# sfid = fs.sfload(soundfont)
# fs.program_select(channel, sfid, banknum, presetnum)

sharpBasePos = [1, 3, 6, 8, 10]
noteBasePos = [0, 2, 4, 5, 7, 9, 11]


class PianoKey(object):
    def __init__(self, pos, width, height, is_sharp, note, keymap=None):
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
        self.note = note
        self.velocity = 100
        self.synth = fluidsynth

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
                # self.synth.noteon(self.channel, self.note, self.velocity)
                self.synth.play_Note(Note(self.note), self.channel,
                                     self.velocity)
                print("key pressed: %d" % (self.keymap))
                print("Channel: %d, Note: %d, Velocity: %d" %
                      (self.channel, self.note, self.velocity))
        elif event.type == pygame.KEYUP:
            if event.key == self.keymap:
                self.color = self.normColor
                # self.synth.noteoff(self.channel, self.note)
                self.synth.stop_Note(self.note, self.channel)
                print("key released: %d" % (self.keymap))

    def setpos(self, pos):
        self.pos = pos


class Octave(object):
    def __init__(self, pos=(0, 0), width=140, height=100, length=7, kmap=None):
        self.pos = pos

        self.height = height
        self.width = width
        self.keyWidth = width / 7
        self.keyHeight = height

        self.length = 7
        self.octaveStart = 60

        # map notes onto correct values.
        self.sharpNotes = []
        for i in sharpBasePos:
            self.sharpNotes.append(self.octaveStart + i)
        print(self.sharpNotes)

        self.notes = []
        for i in noteBasePos:
            self.notes.append(self.octaveStart + i)
        print(self.notes)

        # map to values. last 5 are sharps
        if not kmap:
            self.keymap = ['a', 's', 'd', 'f', 'g', 'h', 'j',
                           'w', 'e', 't', 'y', 'u']
        else:
            self.keymap = kmap
        for i, value in enumerate(self.keymap):
            self.keymap[i] = ord(value)

        self.keys = {}
        self.setupkeys()

    def setupkeys(self):
        # if keys already exist delete them
        if len(self.keys):
            self.keys = []
        # setup keys and give them thier notes and keymaps.
        # keep track on which keys we are.
        keynum = 0
        # first add non sharp keys.
        x, y = self.pos
        for i in range(0, self.length):
            # keypos = (x, y + (i * self.keyWidth))
            keypos = (x + (i * self.keyWidth), y)
            key = PianoKey(keypos, self.keyWidth, self.keyHeight, 0,
                           self.notes[i], self.keymap[keynum])
            self.keys[keynum] = key
            keynum += 1

        # add sharp keys, note last 5 keys are sharps
        skeywidth = self.keyWidth * 0.6
        skeyheight = (self.keyHeight / 2) + 8
        # keep track of note position for sharp note mapping
        note_pos = 0
        # position is the position of key - half the sharp keys width.
        for i in range(1, self.length):
            if i != 3:
                keypos = (x + (i * self.keyWidth - skeywidth / 2), y)
                key = PianoKey(keypos, skeywidth, skeyheight, 1,
                               self.sharpNotes[note_pos], self.keymap[keynum])
                self.keys[keynum] = key
                keynum += 1
                note_pos += 1

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

    def getOctaveStart(self):
        return self.octaveStart

    def setpos(self, pos):
        self.pos = pos
        self.setupkeys()

    def setwidth(self, width):
        self.width = width
        self.setupkeys()

    def setheight(self, height):
        self.height = height
        self.setupkeys()

    def setOctaveStart(self, start):
        self.octaveStart = start
        self.setupKeys()


class Piano(object):
    def __init__(self, start=0, numOctaves=1, screen=None):
        self.start = start
        self.numOctaves = numOctaves

        if screen:
            self.screen = screen

            width, height = self.screen.get_size()
            self.screenWidth = width
            self.screenHeight = height

            self.octaves = []
            octaveHeight = 100
            octaveWidth = self.screenWidth / numOctaves
            # Octave(self, pos, width=140, height=100, length=7, kmap=None)
            for i in range(0, self.numOctaves):
                if(not len(self.octaves)):
                    self.octaves.append(Octave((0, self.screenHeight - 100)))
                else:
                    x, y = self.octaves[i - 1].getpos()
                    self.octaves.append(Octave())
        else:
            self.octaves = None

    def draw(self, screen):
        for octave in self.octaves:
            octave.draw(screen)

    def handleInput(self, events):
        for octave in self.octaves:
            octave.handleInput(events)

# octaveHeight = int(140)
# octave = Octave((0, height - octaveHeight), 200, octaveHeight)
# octavetwo = Octave((octave.getwidth(), height - octave.getheight()))

piano = Piano(start=24, numOctaves=1, screen=screen)

if __name__ == "__main__":
    os.nice(19)
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    presetnum += 1
                elif event.key == pygame.K_DOWN:
                    presetnum -= 1
                # fs.program_select(channel, sfid, banknum, presetnum)
                piano.handleInput(event)
            elif event.type == pygame.KEYUP:
                piano.handleInput(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        screen.fill(GRAY)
        piano.draw(screen)
        pygame.display.flip()
        clock.tick(20)
