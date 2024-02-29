# bubble_sort
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


# selection_sort
def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


# insertion_sort
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key


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


#  counting_sort
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


if __name__ == '__main__':
    def switch_case(value):
        if value == 0:
            print('bubble sort >>')
            list_ = [9, 2, 3, 6, 7, 1, 4]
            print(list_)
            bubble_sort(list_)
            print(list_)
        elif value == 1:
            print('selection_sort >>')
            list_ = [9, 2, 3, 6, 7, 1, 4]
            print(list_)
            selection_sort(list_)
            print(list_)
        elif value == 2:
            print('insertion_sort >>')
            list_ = [9, 2, 3, 6, 7, 1, 4]
            print(list_)
            insertion_sort(list_)
            print(list_)
        elif value == 3:
            print('merge_sort >>')
            list_ = [9, 2, 3, 6, 7, 1, 4]
            print(list_)
            merge_sort(list_)
            print(list_)
        elif value == 4:
            print('quick_sort >>')
            list_ = [9, 2, 3, 6, 7, 1, 4]
            print(list_)
            quick_sort(list_)
            print(list_)
        elif value == 5:
            print('bucket_sort >>')
            list_ = [9, 2, 3, 6, 7, 1, 4]
            print(list_)
            bucket_sort(list_)
            print(list_)
        elif value == 6:
            print('heap_sort >>')
            list_ = [9, 2, 3, 6, 7, 1, 4]
            print(list_)
            heap_sort(list_)
            print(list_)
        else:
            print('radix_sort >>')
            list_ = [9, 2, 3, 6, 7, 1, 4]
            print(list_)
            radix_sort(list_)
            print(list_)


    for i in range(8):
        switch_case(i)
