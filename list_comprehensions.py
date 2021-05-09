def run():
    # [element for element in iterable if condition]
    squares = [i**2 for i in range(1, 101) if i % 3 !=3]
    print(squares)

    numbers = [i for i in range(1, 10000) if i % 36 == 0]
    print(numbers)

if __name__ == '__main__':
    run()