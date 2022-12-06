import pygame
from services.pong_service import PongService


class GameView:
    def __init__(self, screen, bkg_color, object_color, screen_size, object_width):
        self.pong_service = PongService(
            bkg_color, object_color, screen_size, object_width)
        self.bkg_color = bkg_color
        self.object_color = object_color
        self.screen = screen
        self.screen_size = screen_size
        self.object_width = object_width

    def run(self):

        pygame.init()
        clock = pygame.time.Clock()
        while self.pong_service.running():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pong_service.stop()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.pong_service.player_move_up()
            if keys[pygame.K_DOWN]:
                self.pong_service.player_move_down()
            if keys[pygame.K_ESCAPE]:
                break

            self.pong_service.handle_game_events()
            self.pong_service.sprites().update()

            self.screen.fill(self.bkg_color)
            pygame.draw.line(self.screen, self.object_color, [self.screen_size[0]//2, 0], [
                             self.screen_size[0]//2, self.screen_size[1]-1], self.object_width//2)
            self.pong_service.sprites().draw(self.screen)
            pygame.display.flip()

            clock.tick(60)
