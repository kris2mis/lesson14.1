# index :    0 1 2 3 4 5  6  7  8  9  10
# elements:  0 1 1 2 3 5  8  13 21 34 55

def fibonacci(index):
    if index < 2:
        return index

    return fibonacci(index - 1) + fibonacci(index - 2)


def main():
    index = int(input("Input index: "))
    element = fibonacci(index)

    msg = f"fibonacci [{index}] --> {element}."

    print(msg)


main()