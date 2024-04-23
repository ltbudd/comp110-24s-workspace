"""Functions that implement sorting algorithms."""

__author__ = "730648114"



def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    count: int = len(x)
    sindex: int = 0
    for i in range(count - 1):
        uindex = sindex + 1
        compare: int = x[uindex]
        while compare < x[uindex - 1] and uindex > 0:
            temp_val: int = x[uindex]
            x[uindex] = x[uindex - 1]
            x[uindex - 1] = temp_val
            uindex -= 1
        sindex += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    count: int = len(x)
    mindex: int = 0
    for i in range(count):
        mindex = i
        for e in range(i+1, count):
            if x[e] < x[mindex]:
                mindex = e
        temp_val: int = x[i]
        x[i] = x[mindex]
        x[mindex] = temp_val
    return None
