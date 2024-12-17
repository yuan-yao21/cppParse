def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
def main():
    user_input = None
    result = 1 if (3 > 2) else -1
    print("Enter a string to check if it is a palindrome: ")
    user_input = input()
    if isPalindrome(user_input):
        print("True\n")
    else:
        print("False\n")
    print("True" if isPalindrome(user_input) else "False\n")
    return 0


if __name__ == '__main__':
    main()