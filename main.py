from antlr4 import *
from cppLexer import cppLexer
from cppParser import cppParser
from myVisitor import myVisitor


def convert_cpp_to_python(cpp_code: str) -> str:
    input_stream = InputStream(cpp_code)
    lexer = cppLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = cppParser(stream)
    tree = parser.program()
    
    visitor = myVisitor()
    python_code = visitor.visit(tree)
    
    # 检查错误
    if visitor.errors:
        print("转换过程中发现以下错误：")
        for error in visitor.errors:
            print(error)
            
    return python_code

if __name__ == '__main__':
    # 输入的 C++ 代码
    cpp_code = """
    #include <iostream>
    #include <vector>
    #include <algorithm>
    #include <sstream>
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
    """
    
    python_code = convert_cpp_to_python(cpp_code)
    print(python_code)
