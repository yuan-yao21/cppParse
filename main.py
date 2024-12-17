from antlr4 import *
from cppLexer import cppLexer
from cppParser import cppParser
from myVisitor import myVisitor
import os


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
        print("Errors detected during translation are as follows:\n")
        for error in visitor.errors:
            print(error)
            
    return python_code

def main():
    file_symbol = "sim"

    cpp_file_path = f'./test/{file_symbol}.cpp'
    if not os.path.exists(cpp_file_path):
        print(f"Error: File {cpp_file_path} does not exist.")
        return
    
    with open(cpp_file_path, 'r', encoding='utf-8') as cpp_file:
        cpp_code = cpp_file.read()
        

    python_code = convert_cpp_to_python(cpp_code)


    output_dir = f'./result/result_{file_symbol}'
    os.makedirs(output_dir, exist_ok=True)


    python_file_path = os.path.join(output_dir, f'{file_symbol}.py')
    with open(python_file_path, 'w', encoding='utf-8') as python_file:
        python_file.write(python_code)

    python_file_path_2 = './test.py'
    with open(python_file_path_2, 'w', encoding='utf-8') as python_file:
        python_file.write(python_code)
    
    print(f"\nTranslation has finished, python code is saved in {output_dir}")

if __name__ == '__main__':
    main()
