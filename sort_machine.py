import sys

methods = ["bubble", "insertion", "merge", "quick", "selection"]

def bubble_sort(nums):

    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j+1], nums[j]
    
    return nums

def insertion_sort(nums):

    return nums

def merge_sort(nums):
    
    return nums

def quick_sort(nums):

    return nums

def selection_sort(nums):
    
    return nums

def write_data(data, outf):

    with open(outf, "w") as f:
        f.write(", ".join(map(str, data)))

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
    
    match input_method:
        case "bubble":
            sorted_data = bubble_sort(data)
        case "insertion":
            sorted_data = insertion_sort(data)
        case "merge":
            sorted_data = merge_sort(data)
        case "quick":
            sorted_data = quick_sort(data)
        case "selection":
            sorted_data = selection_sort(data)
        case _:
            print("Invalid sorting method")
            return
    
    write_data(sorted_data, output_file)

if __name__ == "__main__":
    main()

