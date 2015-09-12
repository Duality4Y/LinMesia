import sys
import fluidsynth
import pygame

pygame.display.init()

size = screen_width, screen_height = (800, 700)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

soundfont = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
fs = fluidsynth.Synth()
fs.start()

sfid = fs.sfload(soundfont)
fs.program_select(0, sfid, 0, 0)

midinum = 60

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quiting")
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                midinum += 1
            elif event.key == pygame.K_DOWN:
                midinum -= 1
            elif event.key == pygame.K_LEFT:
                midinum -= 10
            elif event.key == pygame.K_RIGHT:
                midinum += 10
            else:
                fs.noteon(0, midinum, 30)
            print("midinum %d" % (midinum))
            print("down")
        elif event.type == pygame.KEYUP:
            fs.noteoff(0, midinum)
            print("up")
    clock.tick(20)
print("exiting loop")

print("quiting pygame")
pygame.quit()

print("synth deleting.")
fs.delete()

sys.exit(0)

# while(1):
#     fs.noteon(0, 60, 30)
#     fs.noteon(0, 67, 30)
#     fs.noteon(0, 76, 30)

#     time.sleep(1.0)

#     fs.noteoff(0, 60)
#     fs.noteoff(0, 67)
#     fs.noteoff(0, 76)

#     time.sleep(1.0)
