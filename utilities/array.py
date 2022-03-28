from random import shuffle


def expand_arr(arr, times=2):
    for time in range(times-1):
        arr += arr.copy()

    shuffle(arr)
    return arr
