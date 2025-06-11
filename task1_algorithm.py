def main():
    # Part 1: Number check
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("That's not a valid integer.")
        return

    if n > 7:
        print("Hello")

    # Part 2: Name check
    name = input("Enter a name: ")
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

    # Part 3: Array of numbers
    raw = input("Enter integers separated by spaces: ")
    try:
        numbers = list(map(int, raw.split()))
    except ValueError:
        print("Please enter only integers.")
        return

    # Filter and print multiples of 3
    print("Array elements that are multiples of 3:")
    for x in numbers:
        if x % 3 == 0:
            print(x)


if __name__ == "__main__":
    main()
