#include <iostream>
#include <stack>
#include <cctype>
#include <string>
#include <sstream>
using namespace std;
int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

int applyOp(int a, int b, char op) {
    if (op == '+') {
        return a + b;
    } else if (op == '-') {
        return a - b;
    } else if (op == '*') {
        return a * b;
    } else if (op == '/') {
        return a / b;
    }

    return 0;
}

int evaluate(const string& expression) {
    stack<int> values;
    stack<char> ops;
    string s = expression;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') continue;

        if (s[i] == '(') {
            ops.push(s[i]);
        } else if (isdigit(s[i])) {
            int val = 0;
            while (i < s.length() && isdigit(s[i])) {
                val = (val * 10) + (s[i] - '0');
                i++;
            }
            values.push(val);
            i--;
        } else if (s[i] == ')') {
            while (!ops.empty() && ops.top() != '(') {
                int val2 = values.top();
                values.pop();

                int val1 = values.top();
                values.pop();

                char op = ops.top();
                ops.pop();

                values.push(applyOp(val1, val2, op));
            }

            // pop opening brace.
            if (!ops.empty()) ops.pop();
        } else {
            while (!ops.empty() && precedence(ops.top()) >= precedence(s[i])) {
                int val2 = values.top();
                values.pop();

                int val1 = values.top();
                values.pop();

                char op = ops.top();
                ops.pop();

                values.push(applyOp(val1, val2, op));
            }

            ops.push(s[i]);
        }
    }

    while (!ops.empty()) {
        int val2 = values.top();
        values.pop();

        int val1 = values.top();
        values.pop();

        char op = ops.top();
        ops.pop();

        values.push(applyOp(val1, val2, op));
    }

    return values.top();
}

int main() {
    string expression;
    cout << "Enter an expression: ";
    getline(cin, expression);
    cout << "The result is: " << evaluate(expression) << endl;
    return 0;
}
