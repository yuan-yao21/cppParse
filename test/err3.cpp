#include <iostream>
#include <string>
using namespace std;

int main() {
    int alpha = 3.14;  // 错误1，尝试将浮点数赋值给整型变量
    int x = "Hello";  // 错误2，尝试将字符串赋值给整型变量
    string s = 3.14;  // 错误3，尝试将浮点数赋值给字符串变量
    int abc = 3;
    string asdf = abc;  // 错误4，尝试将整型变量赋值给字符串变量
    string str = "hello";
    int num = str;  // 错误5，尝试将字符串赋值给整型变量
    return 0;
}
