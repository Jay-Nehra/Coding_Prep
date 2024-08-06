from QuickSort import quicksort  

def test_quicksort():
    assert quicksort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort([2, 1]) == [1, 2]
    assert quicksort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8]
    assert quicksort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert quicksort([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert quicksort([3, -1, 2, -10, 0]) == [-10, -1, 0, 2, 3]
