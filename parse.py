import json
import yaml
from antlr4 import *
from cppLexer import cppLexer
from cppParser import cppParser
import os

# 将语法树转换为嵌套字典
def tree_to_dict(tree, parser):
    if tree.getChildCount() == 0:
        # 如果是叶节点，直接返回文本
        return tree.getText()
    
    # 非叶节点，转换成字典
    node = {
        "type": parser.ruleNames[tree.getRuleIndex()],
        "children": [tree_to_dict(child, parser) for child in tree.getChildren()]
    }
    return node

def main():
    # 输入的表达式
    output_dir = "result"  # 输出文件夹

    source_filename = input("请输入源代码文件名: ")
    with open(source_filename, 'r', encoding='utf-8') as file:
        input_expression = file.read()

    # 获取输入文件名（不包含扩展名）
    base_filename = os.path.splitext(os.path.basename(source_filename))[0]
    
    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_dir = f"{output_dir}/{output_dir}_{base_filename}"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 创建输入流
    input_stream = InputStream(input_expression)

    # 词法分析
    lexer = cppLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # 打印 Token 流
    token_output_path = os.path.join(output_dir, f"{base_filename}_parseResult.txt")
    with open(token_output_path, 'w') as token_file:
        token_file.write("Tokens:\n")
        token_stream.fill()  # 获取所有 Token
        for token in token_stream.tokens:
            token_type_name = cppLexer.symbolicNames[token.type]  # 获取 Token 的类型名称
            token_file.write(f"{token}({token_type_name})\n")
        
    # 语法分析
    parser = cppParser(token_stream)
    tree = parser.program()

    # 将语法树转换为字典格式
    tree_dict = tree_to_dict(tree, parser)

    # 输出为 JSON 格式
    json_output_path = os.path.join(output_dir, f"{base_filename}_parseResult.json")
    with open(json_output_path, 'w') as json_file:
        json.dump(tree_dict, json_file, indent=4)

    # 输出为 YAML 格式
    yaml_output_path = os.path.join(output_dir, f"{base_filename}_parseResult.yaml")
    with open(yaml_output_path, 'w') as yaml_file:
        yaml.dump(tree_dict, yaml_file, sort_keys=False)

    print(f"Tokens, JSON, and YAML outputs have been saved to the '{output_dir}' directory.")

if __name__ == "__main__":
    main()
