#include <iostream>
#include <string>
using namespace std;

int add1(int a, int b) {
    return "hello";  // 错误，返回值类型不匹配
}

int add2(int a, int b) {
    string s = "hello";
    return s;    // 错误，返回值类型不匹配
}

void add_void(int a, int b) {
    int adds = a + b;
    return adds;  // 错误，void函数不能有返回值
}

int main() {
    return 0;
}
