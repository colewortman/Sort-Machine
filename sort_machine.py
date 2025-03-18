import sys
import time

methods = ["bubble", "insertion", "merge", "quick", "selection"]



def main():

    if len(sys.argv) != 4 or sys.argv[1] not in methods:
        print("\nUsage: sort_machine.py [sorting method] [input_file] [output_file]")
        print(f"Sorting methods: {", ".join(methods)}\n")
        return
    
    input_method = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    with open(input_file, "r") as f:
        data = list(map(int, f.read().split(",")))
    
    start = time.time()

    match input_method:
        case "bubble":
            sorted_data = bubble_sort(data)
        case "insertion":
            sorted_data = insertion_sort(data)
        case "merge":
            sorted_data = merge_sort(data, 0, len(data)-1)
        case "quick":
            sorted_data = quick_sort(data)
        case "selection":
            sorted_data = selection_sort(data)
        case _:
            print("Invalid sorting method")
            return
    
    print(sorted_data)
    end = time.time()
    timeout = end - start

    write_data(sorted_data, timeout, output_file)



def bubble_sort(nums):

    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j+1], nums[j]
    
    return nums



def insertion_sort(nums):

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        
        nums[j + 1] = key

    return nums



def merge_sort(nums, low, high):

    if low < high:
        mid = (low + high) // 2

        merge_sort(nums, low, mid)
        merge_sort(nums, mid + 1, high)
        merge(nums, low, mid, high)
    
    return nums



def merge(nums, low, mid, high):

    left = nums[low:mid + 1]
    right = nums[mid + 1:high + 1]
    i = j = 0
    k = low

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



def quick_sort(nums):

    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    left = [i for i in nums if i < pivot]
    right = [j for j in nums if j > pivot]
    middle = [k for k in nums if k == pivot]

    return quick_sort(left) + middle + quick_sort(right)



def selection_sort(nums):
    
    for i in range(len(nums) - 1):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]

    return nums



def write_data(data, timeout, outf):

    with open(outf, "w") as f:
        f.write(f"Execution time: {timeout:.6f} seconds\n\n")
        f.write(", ".join(map(str, data)))



if __name__ == "__main__":
    main()

