## **Bubble Sort**:

This is a simple comparison-based algorithm.
It works by repeatedly swapping the adjacent elements if they are in the wrong order.
This process repeats from the beginning of the array until no more swaps are needed.

```
# bubble_sort
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
```

## **Selection Sort**:

This is also a comparison-based algorithm. It divides the input into a sorted and an unsorted region.
It repeatedly selects the smallest (or largest) element from the unsorted region and moves it to the sorted region.

```
# selection_sort
def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
```

## **Insertion Sort**:

This algorithm builds a sorted array one item at a time.
It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

```
# insertion_sort
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
```

## **Merge Sort**:

This is a divide-and-conquer algorithm. It works by dividing the unsorted list into n sub lists, each containing one
element, and then repeatedly merges sub lists to produce new sorted sub lists until there is only one sublist remaining.

```
# merge_sort
def merge_sort(nums):
    if len(nums) <= 1:
        return
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(nums, left, right)


def merge(nums, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1
```

## **Quick Sort**:

This is also a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array and
partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
The sub-arrays are then recursively sorted.

```
# quick_sort
def quick_sort(nums, low=0, high=None):
    if high is None:
        high = len(nums) - 1
    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort(nums, low, pivot_index)
        quick_sort(nums, pivot_index + 1, high)


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    while True:
        while nums[low] < pivot:
            low += 1
        while nums[high] > pivot:
            high -= 1
        if low >= high:
            return high
        nums[low], nums[high] = nums[high], nums[low]
```

## **Bucket Sort**:

This is a distribution sort. It works by distributing the elements of an array into a number of buckets.
Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the
bucket sort algorithm.

```
# bucket_sort
def bucket_sort(nums):
    if not nums:
        return
    min_val, max_val = min(nums), max(nums)
    bucket_range = (max_val - min_val) / len(nums)
    count_list = [[] for _ in range(len(nums) + 1)]
    for num in nums:
        count_list[int((num - min_val) // bucket_range)].append(num)
    nums.clear()
    for count in count_list:
        if count:
            count.sort()
            nums.extend(count)
```

## **Heap Sort**:

This is a comparison-based algorithm. It works by visualizing the elements of the array as a special kind of complete
binary tree called a heap.

```
# heap_sort
def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
```

## **Radix Sort**:

This is a non-comparative integer sorting algorithm. It works by grouping keys by the individual digits which share the
same significant position and value.

```
#  radix sort
def counting_sort(nums, digit):
    size = len(nums)
    output = [0] * size
    count = [0] * 10
    for i in range(size):
        index = nums[i] // digit
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        index = nums[i] // digit
        output[count[int(index % 10)] - 1] = nums[i]
        count[int(index % 10)] -= 1
        i -= 1
    for i in range(size):
        nums[i] = output[i]


def radix_sort(nums):
    max_num = max(nums)
    digit = 1
    while max_num // digit > 0:
        counting_sort(nums, digit)
        digit *= 10
```