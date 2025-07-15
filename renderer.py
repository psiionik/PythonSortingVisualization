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

