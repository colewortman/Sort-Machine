import sys

methods = ["bubble", "insertion", "merge", "quick", "selection"]

def bubble_sort(f):

    print("bubbles!")

def insertion_sort(f):

    print("insert")

def merge_sort(f):
    
    print("merge")

def quick_sort(f):

    print("quick")

def selection_sort(f):
    
    print("select")


def main():

    if len(sys.argv) != 3 or sys.argv[1] not in methods:
        print("\nUsage: sort_machine.py [sorting method] [file]")
        print(f"Sorting methods: {", ".join(methods)}\n")
        return
    
    input_method = sys.argv[1]
    input_file = sys.argv[2]
    
    match input_method:
        case "bubble":
            bubble_sort(input_file)
        case "insertion":
            insertion_sort(input_file)
        case "merge":
            merge_sort(input_file)
        case "quick":
            quick_sort(input_file)
        case "selection":
            selection_sort(input_file)
        case _:
            print("Invalid sorting method")

if __name__ == "__main__":
    main()

