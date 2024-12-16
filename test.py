# iostream functionality is handled by print() and input()
from typing import List
def main():
    user_input = None
    print("Input numbers separated by commas: ")
    user_input = input()
    numbers = None
    ss = None
    temp = None
    while input():
        numbers.append(int(temp))
    sort(numbers.begin(), numbers.end())
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