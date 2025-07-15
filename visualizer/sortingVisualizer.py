import random

from visualizer import Visualizer

class SortingVisualizer(Visualizer):
    def __init__(self, length, frame_rate, seed = 42):
        self.data = [i for i in range(length)]
        self.number_of_operations = 0

        random.seed(seed)
        self._shuffle_data()

    def _shuffle_data(self):
        random.shuffle(self.data)
    





if __name__ == "__main__":
    print(SortingVisualizer(5, 60).data)