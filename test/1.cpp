#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
bool isPalindrome(const string& s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main() {
    string input;
    int result = (3> 2) ? 1 : -1;
    cout << "Enter a string to check if it is a palindrome: ";
    cin >> input;
    if (isPalindrome(input)) {
        cout << "True" << endl;
    } else {
        cout << "False" << endl;
    }
    cout << (isPalindrome(input) ? "True" : "False") << endl;
    return 0;
}
