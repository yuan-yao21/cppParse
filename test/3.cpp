#include <iostream>
#include <vector>
#include <string>
using namespace std;
// 生成部分匹配表（前缀表）
vector<int> computePrefixTable(const string& t) {
    int m = t.length();
    vector<int> prefixTable(m, 0);
    int j = 0;

    for (int i = 1; i < m; ++i) {
        while (j > 0 && t[i] != t[j]) {
            j = prefixTable[j - 1];
        }
        if (t[i] == t[j]) {
            ++j;
        }
        prefixTable[i] = j;
    }

    return prefixTable;
}

// KMP 算法查找匹配位置
vector<int> kmpSearch(const string& s, const string& t) {
    vector<int> positions;
    int n = s.length();
    int m = t.length();

    if (m == 0) {
        return positions;
    }  // 空模板串直接返回

    vector<int> prefixTable = computePrefixTable(t);
    int j = 0;

    for (int i = 0; i < n; ++i) {
        while (j > 0 && s[i] != t[j]) {
            j = prefixTable[j - 1];
        }
        if (s[i] == t[j]) {
            ++j;
        }
        if (j == m) {
            positions.push_back(i - m + 1);  // 找到匹配起始位置
            j = prefixTable[j - 1];
        }
    }

    return positions;
}

int main() {
    string s, t;
    cout << "Please input a string s: ";
    cin >> s;
    cout << "Please input pattern t: ";
    cin >> t;

    vector<int> result = kmpSearch(s, t);

    if (!result.empty()) {
        cout << "Matched positions: ";
        for (size_t i = 0; i < result.size(); ++i) {
            cout << result[i];
            if (i < result.size() - 1) {
                cout << ",";
            }
        }
        cout << endl;
    } else {
        cout << "False" << endl;
    }

    return 0;
}
