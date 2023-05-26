import pygame

class Game:

    def __init__(self):
        self.width = 800
        self.height = 800
        self.white_colour = (255, 255, 255)

        self.game_window = pygame.display.set_mode((self.width, self.height))

        background_image = pygame.image.load('assets/background.png')
        self.background = pygame.transform.scale(background_image, (self.width, self.height))

        treasure = pygame.image.load('assets/treasure.png')
        self.treasure = pygame.transform.scale(treasure, (50, 50))

        self.clock = pygame.time.Clock()

    def draw_objects(self):
        self.game_window.fill(self.white_colour)

        self.game_window.blit(self.background, (0, 0))
        self.game_window.blit(self.treasure, (self.width/2.1, 25))

        pygame.display.update()

    def run_game_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
            self.draw_objects()
            self.clock.tick(60)