from abc import ABC, abstractmethod

class Visualizer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def visualize_frame(self, f):
        pass