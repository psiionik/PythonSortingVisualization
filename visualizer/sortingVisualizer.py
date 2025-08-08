import random
import sys

# Annoying import syntaxes based on which directory you run the program from
# Usually running this file by itself as main for testing purposes
if __name__ == "__main__":
    sys.path.append("..")
    from baseVisualizer import BaseVisualizer
    from algorithms.quicksort import quicksort
# Import in this manner for using this file as a package
else:
    from .baseVisualizer import BaseVisualizer
    from algorithms import quicksort

# ============================================================

class SortingVisualizer(BaseVisualizer):
    def __init__(self, length, frame_rate, seed = None):
        self.data = [i for i in range(length)]
        self.number_of_operations = 0

        if seed:
            random.seed(seed)

        self._shuffle_data()

    def _shuffle_data(self):
        random.shuffle(self.data)

    def quicksort_framebyframe(self):
        
        # The main driver of the the recursive quicksort implementation.
        # This algorithm is basically divided into 3 parts:
        # 1. Pick Random Pivot
        # 2. Partition elements according to picked pivot
        # 3. Recurse on the left and right partitions of the array
        # So far in this implementation, it modifies the input array in `self.data` in-place.
        def recurse(start, end):
            if start >= end:
                return
            
            picked_pivot = pick_pivot(start, end)
            final_pivot_index = partition(start, end, picked_pivot)

            recurse(start, final_pivot_index - 1)
            recurse(final_pivot_index + 1, end)

        # This function swaps two elements from the array given the indexes of the elements to swap
        def swap(a_index, b_index):
            temp = self.data[a_index]
            self.data[a_index] = self.data[b_index]
            self.data[b_index] = temp

        # This function just picks a random pivot point within a given range of start and end values
        # both inclusive
        def pick_pivot(start, end):
            return random.randint(start, end)

        # This function partitions the array such that all of the elements smaller than
        # the pivot index is to the left of it and all of the elements bigger than the
        # pivot index is to the right of it 
        def partition(start: int, end: int, pivot_index: int) -> int:
            # First swap and move the pivot element to the start of the list
            swap(start, pivot_index)
            new_pivot_index = start

            # Overall idea is that we want to be able to loop once from
            # the rest of the list and keep track of the location that COULD be the most leftmost index
            # of the partition that has elements greater than the pivot.
            # To do so, we assume that this place in the list is right after the pivot element after
            # the initial swap.
            # While scanning down the list, everytime we encounter an element that is less than our pivot,
            # we have to swap its place with this leftmost index of the bigger partition and increase that
            # leftmost index position by 1 to make room for that smaller element
            leftmost_bigger_index = start + 1

            for curr_index in range(start + 1, end + 1):
                # Only want to swap and increment the leftmost bigger index when the current element being
                # looked at is smaller than our pivot index
                if self.data[curr_index] < self.data[new_pivot_index]:
                    swap(leftmost_bigger_index, curr_index)
                    leftmost_bigger_index += 1

            # Need to calculate where the pivot index would be after partitioning
            pivot_final_index = leftmost_bigger_index - 1
            # Swap the positions back so that the pivot actually is in its rightful position
            swap(start, pivot_final_index)

            return pivot_final_index

        recurse(0, len(self.data) - 1)

    def visualize_frame(self, f):
        return f(self.data) 
    
# ============================================================

if __name__ == "__main__":
    array_length = 15
    sv = SortingVisualizer(array_length, 60, 42) 
    print(sv.data)
    sv.quicksort_framebyframe()
    print(sv.data)
