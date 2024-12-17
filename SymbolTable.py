from typing import Dict, Optional, Union, List

# Symbol 类型定义
class Symbol:
    def __init__(self, name: str, type_: str, initialized: bool = False, value: Optional[Union[int, float, str, None]] = None):
        self.name = name
        self.type = type_
        self.initialized = initialized
        self.value = value
    
    def __repr__(self):
        return f"Symbol(name={self.name}, type={self.type}, initialized={self.initialized}, value={self.value})"


# 类型扩展，支持函数类型、指针、数组等
class FunctionSymbol(Symbol):
    def __init__(self, name: str, return_type: str, parameters: List[str], initialized: bool = False):
        super().__init__(name, return_type, initialized)
        self.parameters = parameters  # 参数列表

    def __repr__(self):
        return f"Symbol(name={self.name}, type={self.type}, initialized={self.initialized}, value={self.value}, parameters={self.parameters})"


class PointerSymbol(Symbol):
    def __init__(self, name: str, base_type: str, initialized: bool = False):
        super().__init__(name, f"Pointer to {base_type}", initialized)


class ArraySymbol(Symbol):
    def __init__(self, name: str, base_type: str, size: int, initialized: bool = False):
        super().__init__(name, f"Array of {base_type}[{size}]", initialized)
        self.size = size


# SymbolTable 类，管理符号表
class SymbolTable:
    def __init__(self, parent=None):
        self.symbols: Dict[str, Symbol] = {}
        self.parent = parent
        if parent:
            self.lib = parent.lib
        else:
            self.lib = []
        
    def define(self, name: str, type_: str, symbol_type: str = "variable") -> None:
        """定义新符号，并检查是否有重复定义"""
        if self.is_defined(name):
            raise ValueError(f"Symbol '{name}' is already defined in the current scope.")

        if symbol_type == "variable":
            self.symbols[name] = Symbol(name, type_)
        elif symbol_type == "function":
            self.symbols[name] = FunctionSymbol(name, type_, [])
        elif symbol_type == "pointer":
            self.symbols[name] = PointerSymbol(name, type_)
        elif symbol_type == "array":
            # 假设默认数组大小为10
            self.symbols[name] = ArraySymbol(name, type_, 10)
        else:
            raise ValueError(f"Unknown symbol type '{symbol_type}'")

    def resolve(self, name: str) -> Optional[Symbol]:
        """解析符号，如果找不到则向上查找父作用域"""
        symbol = self.symbols.get(name)
        if symbol:
            return symbol
        if self.parent:
            return self.parent.resolve(name)
        return None

    def is_defined(self, name: str) -> bool:
        """检查符号是否已定义"""
        return name in self.symbols or (self.parent and self.parent.is_defined(name))
    
    def initialize(self, name: str, value: Union[int, float, str]) -> None:
        """初始化符号"""
        symbol = self.resolve(name)
        if symbol:
            symbol.value = value
            symbol.initialized = True
        else:
            raise ValueError(f"Symbol '{name}' is not defined.")

    def define_function(self, name: str, return_type: str, parameters: List[str]) -> None:
        """定义函数符号"""
        self.define(name, return_type, "function")
        function_symbol = self.symbols[name]
        function_symbol.parameters = parameters

    def define_pointer(self, name: str, base_type: str) -> None:
        """定义指针符号"""
        self.define(name, base_type, "pointer")

    def define_array(self, name: str, base_type: str, size: int) -> None:
        """定义数组符号"""
        self.symbols[name] = ArraySymbol(name, base_type, size)

    def define_lib(self, name: str) -> None:
        """定义库函数"""
        self.lib.append(name)

    def resolve_lib(self, name: str) -> bool:
        """检查是否为库函数"""
        return name in self.lib
