class Sorting:
    '''
    In this I have implemented following sorting algorithms.
        1. Selection Sort
        1. Bubble Sort
        1. Insertion Sort
        1. Quick Sort
        1. Merge Sort
    '''

    def __init__(self):
        pass

    def selection_sort(self, arr):
        '''Find min_index and swap(i, min_index), perform sorting from left'''
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]

    def bubble_sort(self, arr):
        '''Compare each element and swap if (i)th ele is smaller than (i+1)th
        element,perform sorting by putting the heaviest element to the 
        rightmost position in each iteration'''
        size = len(arr)
        for i in range(size-1):
            swapped = False
            for j in range(size-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True    
            if not swapped:
                break

    def insertion_sort(self, arr):
        '''Efficient algorithm, Online, Adaptive, Stable, Inplace,
        Place the element into sorted array using anchor'''
        for i in range(len(arr)-1):
            j = i + 1
            anchor = arr[j]
            while j > 0 and anchor < arr[j-1]:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = anchor

    def quick_sort(self, arr, start, end):
        '''It is based on divide and conquer stategy.
        It fixed the postion of pivot element to the righ position.
        It is a recursive algorithm.
        It calls itself untill array becomes sorted.
        Partition Scheme:
        1. Hoare Partition Scheme(Original):
            It takes 0th elemet as pivot.
        2. Lomuto Partition Sceheme:
            It takes mid or rightmost element as pivot.
        '''
        if start < end:
            pi = self.partition(arr, start, end)
            self.quick_sort(arr, start, pi-1)   # left partition
            self.quick_sort(arr, pi+1, end)     # right partition

    def partition(self, arr, start, end):
        '''Fix the position of pivot element to its right position
         is called patition.'''
        pivot_index = start
        pivot = arr[pivot_index]

        while start < end:
            while start < len(arr) and arr[start] <= pivot:
                start += 1

            while arr[end] > pivot:
                end -= 1

            if start < end:
                arr[start], arr[end] = arr[end], arr[start]
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
        return end

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return

        mid  = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        self.merge_sort(left)
        self.merge_sort(right)
        self.merge_two_sorted_list(left, right, arr)

    def merge_two_sorted_list(self, left, right, arr):
        len_left = len(left)
        len_right = len(right)
        i = j = k = 0

        while i < len_left and j < len_right:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len_left:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len_right:
            arr[k] = right[j]
            j += 1
            k += 1


# driver code
if __name__ == '__main__':
    while True:
        # try:
            obj = Sorting()
            arr = list(map(int, input('Enter array elements: ').split(' ')))
            # obj.selection_sort(arr)
            # obj.bubble_sort(arr)
            # obj.insertion_sort(arr)
            
            # calling quick sort
            # obj.quick_sort(arr, 0, len(arr)-1)

            # calling merge sort
            obj.merge_sort(arr)
            print(arr)

        # except Exception as ex:
        #     print(f'\nError: {ex}\n')
