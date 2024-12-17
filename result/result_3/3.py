from typing import List
def computePrefixTable(t):
    m = len(t)
    prefixTable = [0] * m
    j = 0
    i = 1
    while i < m:
        while j > 0 and t[i] != t[j]:
            j = prefixTable[j - 1]
        if t[i] == t[j]:
            j += 1
        prefixTable[i] = j
        i += 1
    return prefixTable
def kmpSearch(s, t):
    positions = []
    n = len(s)
    m = len(t)
    if m == 0:
        return positions
    prefixTable = computePrefixTable(t)
    j = 0
    i = 0
    while i < n:
        while j > 0 and s[i] != t[j]:
            j = prefixTable[j - 1]
        if s[i] == t[j]:
            j += 1
        if j == m:
            positions.append(i - m + 1)
            j = prefixTable[j - 1]
        i += 1
    return positions
def main():
    s = None
    t = None
    print("Please input a string s: ")
    s = input()
    print("Please input pattern t: ")
    t = input()
    result = kmpSearch(s, t)
    if not not result:
        print("Matched positions: ")
        i = 0
        while i < len(result):
            print(result[i])
            if i < len(result) - 1:
                print(",")
            i += 1
        print("\n")
    else:
        print("False\n")
    return 0


if __name__ == '__main__':
    main()