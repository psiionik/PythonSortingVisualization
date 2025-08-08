import random

# This function swaps two elements from the array given the indexes of the elements to swap
def _swap(arr: list[int], a_index: int, b_index: int):
    temp = arr[a_index]
    arr[a_index] = arr[b_index]
    arr[b_index] = temp

# This function just picks a random pivot point within a given range of start and end values
# both inclusive
def _pick_pivot(start: int, end: int) -> int:
    return random.randint(start, end)

# This function partitions the array such that all of the elements smaller than
# the pivot index is to the left of it and all of the elements bigger than the
# pivot index is to the right of it 
def _partition(arr: list[int], start: int, end: int, pivot_index: int) -> int:
    # First swap and move the pivot element to the start of the list
    _swap(arr, start, pivot_index)
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
        if arr[curr_index] < arr[new_pivot_index]:
            _swap(arr, leftmost_bigger_index, curr_index)
            leftmost_bigger_index += 1

    # Need to calculate where the pivot index would be after partitioning
    pivot_final_index = leftmost_bigger_index - 1
    # Swap the positions back so that the pivot actually is in its rightful position
    _swap(arr, start, pivot_final_index)

    return pivot_final_index

# The main driver of the the recursive quicksort implementation.
# This algorithm is basically divided into 3 parts:
# 1. Pick Random Pivot
# 2. Partition elements according to picked pivot
# 3. Recurse on the left and right partitions of the array
# So far in this implementation, it modifies the input array in `self.data` in-place.
def _recurse(arr: list[int], start: int, end: int):
    if start >= end:
        return
    
    picked_pivot = _pick_pivot(start, end)
    final_pivot_index = _partition(arr, start, end, picked_pivot)

    _recurse(arr, start, final_pivot_index - 1)
    _recurse(arr, final_pivot_index + 1, end)

def quicksort(arr):
    _recurse(arr, 0, len(arr) - 1)
    return arr



if __name__ == "__main__":
    arr_length = 15
    arr = [i for i in range(0, 15)]
    random.shuffle(arr)
    print(quicksort(arr))