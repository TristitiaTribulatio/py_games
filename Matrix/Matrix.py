import pygame
from random import randint, randrange, choice

class Matrix:
    def __init__(self):
        self.RESOLUTION, self.FPS, self.FONT = 1500, 15, 30
        self.katakana, self.coord = [chr(int('0x30a0', 16) + i) for i in range(96)], []

    def run(self):
        pygame.init()
        font_letter = pygame.font.Font("NotoSansJP.otf", self.FONT, bold=True, italic=True)
        screen, clock = pygame.display.set_mode([self.RESOLUTION, self.RESOLUTION // 2]), pygame.time.Clock()
        for i in range(self.RESOLUTION // self.FONT):
            self.coord.append([i * self.FONT, -(randint(1, 50) * self.FONT), randint(10, 20)])
        while True:
            screen.fill(pygame.Color('black'))
            for i in range(len(self.coord)):
                for j in range(self.coord[i][2]):
                    render_letter = font_letter.render(choice(self.katakana), True, (0, randrange(160, 250), 0))
                    screen.blit(render_letter, (self.coord[i][0], self.coord[i][1] + (j * self.FONT)))
                self.coord[i][1] += 12
                if self.coord[i][1] > (self.RESOLUTION // 2): self.coord[i][1] = -(randint(20, 50) * self.FONT)

            pygame.display.flip()
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: exit()

if __name__ == "__main__": Matrix().run()