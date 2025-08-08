from abc import ABC, abstractmethod

class BaseVisualizer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def visualize_frame(self, f):
        pass