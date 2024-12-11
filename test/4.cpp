#include <iostream>
#include <vector>
#include <stack>
#include <cctype>
#include <string>
#include <map>

using namespace std;

bool isOperator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

bool isHigherPrecedence(char op1, char op2) {
    return precedence(op1) > precedence(op2);
}

string infixToPostfix(const string& infix) {
    stack<char> operators;
    string postfix = "";
    bool mayBeUnary = true;  
    // Assume the first operator can be unary

    for (int i = 0; i < infix.size(); i++) {
        char c = infix[i];

        if (isspace(c)) {
            continue;
        } else if (isdigit(c)) {
            postfix += c;
            while (i + 1 < infix.size() && isdigit(infix[i + 1])) {
                postfix += infix[++i];
            }
            postfix += " ";
            mayBeUnary = false;
        } else if (c == '(') {
            operators.push(c);
            mayBeUnary = true;  
            // Next operator could be unary
        } else if (c == ')') {
            while (!operators.empty() && operators.top() != '(') {
                postfix += operators.top() + string(" ");
                operators.pop();
            }
            operators.pop();  // Remove '('
            mayBeUnary = false;
        } else if (isOperator(c)) {
            if (mayBeUnary && c == '-') {
                // Handle unary minus
                postfix += "0 ";
                operators.push('-');
            } else {
                while (!operators.empty() && precedence(operators.top()) >= precedence(c) && operators.top() != '(') {
                    postfix += operators.top() + string(" ");
                    operators.pop();
                }
                operators.push(c);
            }
            mayBeUnary = true;  // Next operator could be unary (if this was a binary operator)
        }
    }

    while (!operators.empty()) {
        postfix += operators.top() + string(" ");
        operators.pop();
    }
    return postfix;
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

int evaluatePostfix(const string& postfix) {
    stack<int> values;
    int i = 0;
    while (i < postfix.size()) {
        if (isspace(postfix[i])) {
            i++;
            continue;
        }
        else if (isdigit(postfix[i])) {
            int val = 0;
            while (i < postfix.size() && isdigit(postfix[i])) {
                val = val * 10 + (postfix[i] - '0');
                i++;
            }
            values.push(val);
        } else if (isOperator(postfix[i])) {
            int val2 = values.top(); values.pop();
            int val1 = values.top(); values.pop();
            values.push(applyOp(val1, val2, postfix[i]));
            i++;
        }
    }
    return values.top();
}

int main() {
    string expression;
    cout << "Enter an expression: ";
    getline(cin, expression);
    string postfix = infixToPostfix(expression);
    cout << "Postfix expression: " << postfix << endl;
    int result = evaluatePostfix(postfix);
    cout << "The result is: " << result << endl;
    return 0;
}
