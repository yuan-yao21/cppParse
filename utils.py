from colorama import init


# 定义打印颜色函数
init(autoreset=True)
def print_red(text):
    print("\033[31m" + text + "\033[0m")
def print_green(text):
    print("\033[32m" + text + "\033[0m")
def print_yellow(text):
    print("\033[33m" + text + "\033[0m")
def print_blue(text):
    print("\033[34m" + text + "\033[0m")
def print_magenta(text):
    print("\033[35m" + text + "\033[0m")
def print_cyan(text):
    print("\033[36m" + text + "\033[0m")


# 定义C++关键字集合
cpp_keywords = {
    "alignas", "alignof", "and", "and_eq", "asm", "atomic_cancel", "atomic_commit", 
    "atomic_noexcept", "auto", "bitand", "bitor", "bool", "break", "case", 
    "catch", "char", "char16_t", "char32_t", "class", "compl", "concept", 
    "const", "consteval", "constexpr", "constinit", "continue", "decltype", 
    "default", "delete", "do", "double", "dynamic_cast", "else", "enum", "explicit", 
    "export", "extern", "false", "float", "for", "friend", "goto", "if", 
    "inline", "int", "long", "mutable", "namespace", "new", "noexcept", "not", 
    "not_eq", "nullptr", "operator", "or", "or_eq", "private", "protected", "public", 
    "register", "reinterpret_cast", "requires", "return", "short", "signed", 
    "sizeof", "static", "static_assert", "static_cast", "struct", "switch", "synchronized", 
    "template", "this", "throw", "true", "try", "typedef", "typeid", "typename", 
    "union", "unsigned", "using", "virtual", "void", "volatile", "wchar_t", "while"
}
