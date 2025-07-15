from abc import ABC, abstractmethod
import pygame

class Scene(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def load_scene(self):
        pass

class InitialScene(Scene):
    def __init__(self):
        ...

    def load_scene(self):
        ...

class OneDimensionalArrayScene(Scene):
    def __init__(self, array_size):
        self.array_size = array_size
        self.objects = []

    def load_scene(self):
        self.objects.append(pygame.surface.Surface())