from typing import List
import io
def main():
    user_input = None
    print("Input numbers separated by commas: ")
    user_input = input()
    numbers = []
    ss = user_input.split(',')
    temp = None
    for temp in ss:
        numbers.append(int(temp))
    numbers.sort()
    print("Sorted numbers: ")
    i = 0
    while i < len(numbers):
        print(numbers[i])
        if i < len(numbers) - 1:
            print(",")
        i += 1
    print("\n")
    return 0


if __name__ == '__main__':
    main()