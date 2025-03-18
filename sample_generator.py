import random


def main():

    while True:
        try:
            size = int(input("\nEnter amount of random numbers to be generated: "))
            while size <= 0:
                size = int(input("Must be a positive integer: "))
            break
        except ValueError:
            print("Invalid number")
    
    numbers = [str(random.randint(0, 100)) for _ in range(size)]
    with open("sample.txt", "w") as f:
        f.write(", ".join(numbers))

if __name__ == "__main__":
    main()
    