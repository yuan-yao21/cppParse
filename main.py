import json
import yaml
from antlr4 import *
from cppLexer import cppLexer
from cppParser import cppParser
from myVisitor import myVisitor
from parse import tree_to_dict
from utils import print_green, print_red
import os


file_symbol = "1"


def convert_cpp_to_python(cpp_code: str) -> str:
    output_dir = "result"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_dir = f"{output_dir}/{output_dir}_{file_symbol}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 创建输入流
    input_stream = InputStream(cpp_code)

    # 词法分析
    lexer = cppLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # 打印 Token 流
    token_output_path = os.path.join(output_dir, f"{file_symbol}_parseResult.txt")
    with open(token_output_path, 'w') as token_file:
        token_file.write("Tokens:\n")
        stream.fill()
        for token in stream.tokens:
            token_type_name = cppLexer.symbolicNames[token.type]
            token_file.write(f"{token}({token_type_name})\n")

    # 语法分析
    parser = cppParser(stream)
    tree = parser.program()

    # 将语法树转换为字典格式
    tree_dict = tree_to_dict(tree, parser)

    # 输出为 JSON 格式
    json_output_path = os.path.join(output_dir, f"{file_symbol}_parseResult.json")
    with open(json_output_path, 'w') as json_file:
        json.dump(tree_dict, json_file, indent=4)

    # 输出为 YAML 格式
    yaml_output_path = os.path.join(output_dir, f"{file_symbol}_parseResult.yaml")
    with open(yaml_output_path, 'w') as yaml_file:
        yaml.dump(tree_dict, yaml_file, sort_keys=False)

    print_green(f"Tokens, JSON, and YAML outputs have been saved to the '{output_dir}' directory.\n")
    
    # 生成 Python 代码
    visitor = myVisitor()
    python_code = visitor.visit(tree)
    
    ifRight = True
    # 检查错误
    if visitor.errors:
        ifRight = False
        print_red("Errors detected during translation are as follows:\n")
        for error in visitor.errors:
            print_red(error)
            
    return python_code, ifRight


def main():
    cpp_file_path = f'./test/{file_symbol}.cpp'
    if not os.path.exists(cpp_file_path):
        print(f"Error: File {cpp_file_path} does not exist.")
        return
    
    with open(cpp_file_path, 'r', encoding='utf-8') as cpp_file:
        cpp_code = cpp_file.read()
        

    python_code, ifRight = convert_cpp_to_python(cpp_code)
    if not ifRight:
        return

    output_dir = f'./result/result_{file_symbol}'
    os.makedirs(output_dir, exist_ok=True)


    python_file_path = os.path.join(output_dir, f'{file_symbol}.py')
    with open(python_file_path, 'w', encoding='utf-8') as python_file:
        python_file.write(python_code)

    python_file_path_2 = './test.py'
    with open(python_file_path_2, 'w', encoding='utf-8') as python_file:
        python_file.write(python_code)
    
    print_green(f"\nTranslation has finished, python code is saved in {output_dir}")


if __name__ == '__main__':
    main()
