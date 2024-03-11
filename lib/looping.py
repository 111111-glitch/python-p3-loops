#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")

def square_integers(lst):
    squared_list = []
    for num in lst:
        squared_list.append(num ** 2)
    return squared_list

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Testing the functions
if __name__ == "__main__":
    print("Countdown to New Year:")
    happy_new_year()

    print("\nSquare of integers:")
    numbers = [1, 2, 3, 4, 5]
    print(square_integers(numbers))

    print("\nFizzBuzz game:")
    fizzbuzz()
