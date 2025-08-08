import pygame

class Renderer():
    def __init__(self, width, height, is_hardware_accel):
        pygame.display.init()
        self.width = width
        self.height = height
        self.is_hardware_accel = is_hardware_accel
        self.window = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF if self.is_hardware_accel else 0)

    def fill_screen(self):
        self.window.fill("purple")

    def draw_rectangle(self):
        red = (255, 0, 0)
        blue = (0, 0, 255)
        pygame.draw.rect(self.window, red, (100, 100, 200, 150))
        pygame.draw.rect(self.window, blue, pygame.Rect(400, 200, 150, 100), 5)

