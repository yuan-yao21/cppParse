#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std;
int main() {
    string user_input;
    cout << "Input numbers separated by commas: ";
    getline(cin, user_input);

    vector<int> numbers;
    stringstream ss(user_input);
    string temp;
    
    // 将输入字符串按逗号分割并转换为整数存入vector
    while (getline(ss, temp, ',')) {
        numbers.push_back(stoi(temp));
    }

    // 排序
    sort(numbers.begin(), numbers.end());

    // 输出排序后的结果
    cout << "Sorted numbers: ";
    for (size_t i = 0; i < numbers.size(); ++i) {
        cout << numbers[i];
        if (i < numbers.size() - 1) {
            cout << ",";
        }
    }
    cout << endl;

    return 0;
}
