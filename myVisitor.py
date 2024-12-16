from typing import List, Optional
from antlr4 import *
from SymbolTable import FunctionSymbol, SymbolTable
from cppLexer import cppLexer
from cppParser import cppParser
from cppVisitor import cppVisitor
import Levenshtein

class myVisitor(cppVisitor):
    def __init__(self):
        super().__init__()
        self.current_scope = SymbolTable()  # 全局作用域
        self.indentation = 0
        self.errors = []
        self.current_function = None  # 当前正在处理的函数名
        
    def indent(self) -> str:
        return "    " * self.indentation
    
    def report_error(self, line: int, message: str, suggestion: Optional[str] = None):
        error = f"Line {line}: {message}"
        if suggestion:
            error += f"\nSuggestion: {suggestion}"
        self.errors.append(error)

    def find_similar_symbol(self, name: str) -> Optional[str]:
        """查找最相似的已定义变量名"""
        all_symbols = []
        scope = self.current_scope
        while scope:
            all_symbols.extend(scope.symbols.keys())
            scope = scope.parent

        if not all_symbols:
            return None

        # 找出最相似的变量名
        closest = min(all_symbols, 
                     key=lambda x: Levenshtein.distance(x, name))
        
        # 如果相似度足够高（距离小于3）才返回建议
        if Levenshtein.distance(closest, name) < 3:
            return closest
        return None


    def visitProgram(self, ctx: cppParser.ProgramContext):
        result = []
        
        # 访问所有子节点
        for child in ctx.children:
            if child:
                code = self.visit(child)
                if code:
                    result.append(code)

        result.append("\n")
        result.append("if __name__ == '__main__':")
        result.append("    main()")
                    
        return "\n".join(filter(None, result))

    def visitIncludeDirective(self, ctx: cppParser.IncludeDirectiveContext):
        # 将C++的include转换为Python的import
        include_file = ctx.IncludeFileName() or ctx.StringLiteral()
        if include_file:
            file_name = include_file.getText().strip('<>"')
            if file_name == "iostream":
                return "# iostream functionality is handled by print() and input()"
            elif file_name == "string":
                return "# string operations are native in Python"
            elif file_name == "vector":
                return "from typing import List"
            elif file_name == "stack":
                return "from typing import List"
        return ""

    def visitUsingNamespaceDeclaration(self, ctx: cppParser.UsingNamespaceDeclarationContext):
        # Python不需要namespace声明
        return ""
    
    def visitFunctionDefinition(self, ctx: cppParser.FunctionDefinitionContext):
        # 创建新的作用域
        parent_scope = self.current_scope
        self.current_scope = SymbolTable(parent_scope)
        
        # 获取函数信息
        return_type = self.visit(ctx.typeSpecifier())
        func_name = ctx.ID().getText()
        self.current_function = func_name
        
        # 在父作用域中定义函数
        try:
            parent_scope.define_function(func_name, return_type, [])
        except ValueError as e:
            self.report_error(ctx.start.line, str(e))

        # 处理参数
        params = []
        if ctx.parameterList():
            params = self.visit(ctx.parameterList())

        # 更新函数符号的参数列表
        func_symbol = parent_scope.resolve(func_name)
        if isinstance(func_symbol, FunctionSymbol):
            func_symbol.parameters = params

        # 构建函数定义
        func_def = f"def {func_name}({', '.join(p[0] for p in params)}):"
        
        # 处理函数体
        self.indentation += 1
        body = self.visit(ctx.compoundStatement())
        self.indentation -= 1
        
        # 恢复作用域
        self.current_scope = parent_scope
        self.current_function = None
        
        if not body.strip():
            body = self.indent() + "pass"
            
        return f"{func_def}\n{body}"

    def visitParameterList(self, ctx: cppParser.ParameterListContext):
        params = []
        for param in ctx.parameter():
            param_info = self.visit(param)
            if param_info:
                name, type_ = param_info
                try:
                    self.current_scope.define(name, type_)
                    params.append((name, type_))
                except ValueError as e:
                    self.report_error(param.start.line, str(e))
        return params

    def visitParameter(self, ctx: cppParser.ParameterContext):
        param_type = self.visit(ctx.parameterTypeSpecifier())
        param_name = ctx.ID().getText()
        return param_name, param_type

    def visitTypeSpecifier(self, ctx: cppParser.TypeSpecifierContext):
        if ctx.baseTypeSpecifier():
            return self.visit(ctx.baseTypeSpecifier())
        elif ctx.containerTypeSpecifier():
            return self.visit(ctx.containerTypeSpecifier())
        return "None"

    def visitBaseTypeSpecifier(self, ctx: cppParser.BaseTypeSpecifierContext):
        if ctx.INT() or ctx.SIZE_T():
            return "int"
        elif ctx.BOOL():
            return "bool"
        elif ctx.STRING():
            return "str"
        elif ctx.CHAR():
            return "str"
        elif ctx.DOUBLE() or ctx.FLOAT():
            return "float"
        elif ctx.VOID():
            return "None"
        elif ctx.STRING_STREAM():
            return "StringIO"
        return "Any"

    def visitContainerTypeSpecifier(self, ctx: cppParser.ContainerTypeSpecifierContext):
        base_type = self.visit(ctx.baseTypeSpecifier())
        return f"List[{base_type}]"

    def visitCompoundStatement(self, ctx: cppParser.CompoundStatementContext):
        statements = []
        for stmt in ctx.statement():
            code = self.visit(stmt)
            if code:
                if stmt.declarationStatement():
                    statements.append(code)
                else:
                    statements.append(self.indent() + code)
        
        if not statements:
            statements.append(self.indent() + "pass")
            
        return "\n".join(statements)

    def visitStatement(self, ctx: cppParser.StatementContext):
        for child in ctx.children:
            result = self.visit(child)
            if result:
                return result
        return ""

    def visitDeclarationStatement(self, ctx: cppParser.DeclarationStatementContext):
        return self.visit(ctx.variableDeclaration())
    
    def visitVariableDeclaration(self, ctx: cppParser.VariableDeclarationContext):
        type_spec = self.visit(ctx.typeSpecifier())
        
        results = []
        for init_decl in ctx.initDeclaratorList().initDeclarator():
            var_name = init_decl.ID().getText()
            
            try:
                # 检查变量类型并相应定义
                if init_decl.arraySubscript():
                    size_ctx = init_decl.arraySubscript().assignmentExpression()
                    if size_ctx:
                        size = int(size_ctx.getText())
                        self.current_scope.define_array(var_name, type_spec, size)
                        results.append(f"{self.indent()}{var_name} = [None] * {size}")
                    else:
                        self.current_scope.define_array(var_name, type_spec, 0)
                        results.append(f"{self.indent()}{var_name} = []")
                else:
                    self.current_scope.define(var_name, type_spec)
                    
                    if init_decl.initializer():
                        init_value = self.visit(init_decl.initializer())
                        self.current_scope.initialize(var_name, init_value)
                        results.append(f"{self.indent()}{var_name} = {init_value}")
                    else:
                        results.append(f"{self.indent()}{var_name} = None")
                        
            except ValueError as e:
                self.report_error(init_decl.start.line, str(e))
                continue
                
        return "\n".join(results)

    def visitInitDeclaratorList(self, ctx: cppParser.InitDeclaratorListContext):
        declarations = []
        for decl in ctx.initDeclarator():
            result = self.visit(decl)
            if result:
                declarations.append(result)
        return "\n".join(declarations)

    def visitInitDeclarator(self, ctx: cppParser.InitDeclaratorContext):
        var_name = ctx.ID().getText()
        
        if ctx.initializer():
            init_value = self.visit(ctx.initializer())
            return f"{var_name} = {init_value}"
        elif ctx.arraySubscript():
            return f"{var_name} = []"  # 初始化空列表
        else:
            return f"{var_name} = None"

    def visitInitializer(self, ctx: cppParser.InitializerContext):
        return self.visit(ctx.assignmentExpression())

    def visitExpressionStatement(self, ctx: cppParser.ExpressionStatementContext):
        return self.visit(ctx.expStatement())

    def visitExpStatement(self, ctx: cppParser.ExpStatementContext):
        if not ctx.children:
            return ""
            
        if ctx.initializer():
            return self.visit(ctx.initializer())
            
        # 处理赋值操作
        if ctx.ID():
            var_name = ctx.ID().getText()
            op = ctx.getChild(1).getText()  # 获取操作符
            value = self.visit(ctx.initializer())
            
            if op == "=":
                return f"{var_name} = {value}"
            elif op == "+=":
                return f"{var_name} += {value}"
            elif op == "-=":
                return f"{var_name} -= {value}"
                
        return ""

    def visitSelectionStatement(self, ctx: cppParser.SelectionStatementContext):
        conditions = []
        blocks = []
        
        i = 0
        while i < len(ctx.logicalExpression()):
            cond = self.visit(ctx.logicalExpression(i))
            self.indentation += 1
            block = self.visit(ctx.compoundStatement(i))
            self.indentation -= 1
            conditions.append(cond)
            blocks.append(block)
            i += 1
            
        result = []
        first = True
        for cond, block in zip(conditions, blocks):
            if first:
                result.append(f"if {cond}:")
                first = False
            else:
                result.append(f"elif {cond}:")
            result.append(block)
            
        # 处理else块
        if len(ctx.compoundStatement()) > len(conditions):
            result.append("    else:")
            self.indentation += 1
            result.append(self.visit(ctx.compoundStatement()[-1]))
            self.indentation -= 1
            
        return "\n".join(result)

    def visitIterationStatement(self, ctx: cppParser.IterationStatementContext):
        if ctx.WHILE():
            # while循环
            condition = self.visit(ctx.logicalExpression())
            self.indentation += 1
            body = self.visit(ctx.compoundStatement())
            self.indentation -= 1
            return f"while {condition}:\n{body}"
        else:
            # for循环
            init = self.visit(ctx.children[2])  # 初始化
            init = init[len(self.indent()):]  # 去除缩进
            cond = self.visit(ctx.logicalExpression())  # 条件
            incr = [self.visit(stmt) for stmt in ctx.expStatement()]  # 遍历每个元素
            
            self.indentation += 1
            body = self.visit(ctx.compoundStatement())
            if incr:
                for i in range(len(incr)):
                    body += f"\n{self.indent()}{incr[i]}"
            self.indentation -= 1

            return f"{init}\n{self.indent()}while {cond}:\n{body}"

    def visitJumpStatement(self, ctx: cppParser.JumpStatementContext):
        if not ctx.children:
            return "return"
            
        if ctx.assignmentExpression():
            value = self.visit(ctx.assignmentExpression())
            return f"return {value}"
        elif ctx.BooleanLiteral():
            return f"return {ctx.BooleanLiteral().getText().lower()}"
        elif ctx.StringLiteral():
            return f"return {ctx.StringLiteral().getText()}"
        elif ctx.NUMBER():
            return f"return {ctx.NUMBER().getText()}"
            
        return "return None"

    def visitAssignmentExpression(self, ctx: cppParser.AssignmentExpressionContext):
        if ctx.operationExpression():
            return self.visit(ctx.operationExpression())
        elif ctx.conditionalExpression():
            return self.visit(ctx.conditionalExpression())
        return ""
    
    def visitOperationExpression(self, ctx: cppParser.OperationExpressionContext):
        """访问操作表达式"""
        return self.visit(ctx.additionExpr())

    def visitLogicalExpression(self, ctx: cppParser.LogicalExpressionContext):
        if ctx.logicalOrExpr():
            return self.visit(ctx.logicalOrExpr())
        elif ctx.GET():  # 处理getline
            return f"input()"  # 简化处理
        return ""

    def visitOrExpression(self, ctx: cppParser.OrExpressionContext):
        left = self.visit(ctx.logicalOrExpr())
        right = self.visit(ctx.logicalAndExpr())
        return f"{left} or {right}"

    def visitAndExpression(self, ctx: cppParser.AndExpressionContext):
        left = self.visit(ctx.logicalAndExpr())
        right = self.visit(ctx.equalityExpr())
        return f"{left} and {right}"

    def visitEquality(self, ctx: cppParser.EqualityContext):
        left = self.visit(ctx.equalityExpr())
        right = self.visit(ctx.relationalExpr())
        op = ctx.getChild(1).getText()
        return f"{left} {op} {right}"

    def visitRelational(self, ctx: cppParser.RelationalContext):
        left = self.visit(ctx.relationalExpr())
        right = self.visit(ctx.operationExpression())
        op = ctx.getChild(1).getText()
        return f"{left} {op} {right}"

    def visitAdd(self, ctx: cppParser.AddContext):
        left = self.visit(ctx.additionExpr())
        right = self.visit(ctx.multiplicationExpr())
        return f"{left} + {right}"

    def visitSubtract(self, ctx: cppParser.SubtractContext):
        left = self.visit(ctx.additionExpr())
        right = self.visit(ctx.multiplicationExpr())
        return f"{left} - {right}"
    
    def visitToMultiplication(self, ctx: cppParser.ToMultiplicationContext):
        return self.visit(ctx.multiplicationExpr())

    def visitMultiply(self, ctx: cppParser.MultiplyContext):
        left = self.visit(ctx.multiplicationExpr())
        right = self.visit(ctx.unaryExpr())
        return f"{left} * {right}"

    def visitDivide(self, ctx: cppParser.DivideContext):
        left = self.visit(ctx.multiplicationExpr())
        right = self.visit(ctx.unaryExpr())
        return f"{left} / {right}"
    
    def visitToPrimary(self, ctx: cppParser.ToPrimaryContext):
        return self.visit(ctx.unaryExpr())

    def visitPreIncrement(self, ctx: cppParser.PreIncrementContext):
        var = self.visit(ctx.postfixExpr())
        return f"{var} += 1"

    def visitPreDecrement(self, ctx: cppParser.PreDecrementContext):
        var = self.visit(ctx.postfixExpr())
        return f"{var} -= 1"

    def visitNotExpression(self, ctx: cppParser.NotExpressionContext):
        expr = self.visit(ctx.postfixExpr())
        return f"not {expr}"
    
    def visitToPostfix(self, ctx: cppParser.ToPostfixContext):
        return self.visit(ctx.postfixExpr())

    def visitPostIncrementOrDecrement(self, ctx: cppParser.PostIncrementOrDecrementContext):
        # 在Python中后缀自增/自减需要转换为前缀形式
        expr = self.visit(ctx.primaryExpr())
        op = ctx.getChild(1).getText() if len(ctx.children) > 1 else None
        if op == "++":
            return f"{expr} += 1"
        elif op == "--":
            return f"{expr} -= 1"
        return expr

    def visitPrimaryExpr(self, ctx: cppParser.PrimaryExprContext):
        # 基本字面量
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.StringLiteral():
            return ctx.StringLiteral().getText()
        elif ctx.BooleanLiteral():
            return ctx.BooleanLiteral().getText().capitalize()
            
        # 标识符相关
        if len(ctx.children) == 1 and ctx.ID():  # 单独的标识符
            var_name = ctx.ID().getText()
            # 检查变量是否定义和初始化
            symbol = self.current_scope.resolve(var_name)
            if not symbol:
                similar = self.find_similar_symbol(var_name)
                suggestion = f"Did you mean '{similar}'?" if similar else "Make sure to declare the variable before using it."
                self.report_error(ctx.start.line,
                    f"Variable '{var_name}' is not defined.",
                    suggestion)
            return var_name
            
        # 数组访问: ID '[' argList ']'
        if len(ctx.children) == 4 and ctx.ID() and ctx.children[1].getText() == '[':
            array_name = ctx.ID().getText()
            index = self.visit(ctx.argList())
            return f"{array_name}[{index}]"
            
        # 对象方法调用: ID '.' backFunctionName '(' argList? ')'
        if ctx.backFunctionName():
            obj = ctx.ID().getText()
            func = self.visit(ctx.backFunctionName())
            args = self.visit(ctx.argList()) if ctx.argList() else ""
            
            # 转换C++方法到Python等效方法
            if func == "size" or func == "length":
                return f"len({obj})"
            elif func == "push_back":
                return f"{obj}.append({args})"
            elif func == "empty":
                return f"not {obj}"
            elif func == "top":
                return f"{obj}[-1]"
            elif func == "pop":
                return f"{obj}.pop()"
            
            return f"{obj}.{func}({args})"
            
        # 全局函数调用: frontFunctionName '(' argList? ')'
        if ctx.frontFunctionName():
            func = self.visit(ctx.frontFunctionName())
            args = self.visit(ctx.argList()) if ctx.argList() else ""
            
            # 转换C++函数到Python等效函数
            if func == "stoi":
                return f"int({args})"
            elif func == "isdigit":
                return f"{args}.isdigit()"
                
            return f"{func}({args})"
            
        # 带括号的表达式: '(' operationExpression ')'
        if ctx.operationExpression():
            return f"({self.visit(ctx.operationExpression())})"
            
        # 带括号的逻辑表达式: '(' logicalExpression ')'
        if ctx.logicalExpression():
            return f"({self.visit(ctx.logicalExpression())})"
            
        # 类型转换表达式
        if ctx.turnExpression():
            return self.visit(ctx.turnExpression())
            
        # 如果没有匹配到任何规则，访问子节点
        return self.visitChildren(ctx)

    def visitInputStream(self, ctx: cppParser.InputStreamContext):
        if ctx.GET():  # getline
            var = ctx.ID().getText()
            return f"{var} = input()"
        else:  # cin
            target = self.visit(ctx.inputStreamTarget())
            return f"{target} = input()"
            
    def visitInputStreamTarget(self, ctx: cppParser.InputStreamTargetContext):
        if ctx.RIGHT_SHIFT():  # 处理链式输入
            left = ctx.ID().getText()
            right = self.visit(ctx.inputStreamTarget())
            return f"{left} = {right}"
        return ctx.ID().getText()

    def visitOutputStream(self, ctx: cppParser.OutputStreamContext):
        target = self.visit(ctx.outputStreamTarget())
        if target is None:
            return ""
        
        if "endl" in target:
            target = target.replace("endl", "")
            return f"print({target})"
        return f"print({target})"

    def visitOutputStreamTarget(self, ctx: cppParser.OutputStreamTargetContext):
        if ctx.outExpression():
            expr = self.visit(ctx.outExpression())
            if ctx.outputStreamTarget():
                next_target = self.visit(ctx.outputStreamTarget())
                if next_target and expr:
                    final_out = expr.strip("\"") + next_target.strip("\"")
                    return f"\"{final_out}\""
            return expr
        return ""

    def visitOutExpression(self, ctx: cppParser.OutExpressionContext):
        if ctx.ENDL():
            return '"\\n"'
        elif ctx.assignmentExpression():
            return self.visit(ctx.assignmentExpression())
        return ""

    def visitBackFunctionName(self, ctx: cppParser.BackFunctionNameContext):
        if ctx.ID():
            return ctx.ID().getText()
        return ctx.BACK_FUNCTION().getText()

    def visitFrontFunctionName(self, ctx: cppParser.FrontFunctionNameContext):
        if ctx.ID():
            return ctx.ID().getText()
        return ctx.FRONT_FUNCTION().getText()

    def visitTurnExpression(self, ctx: cppParser.TurnExpressionContext):
        type_name = self.visit(ctx.typeSpecifier())
        expr = self.visit(ctx.primaryExpr())
        # 处理类型转换
        if type_name == "str":
            return f"str({expr})"
        elif type_name == "int":
            return f"int({expr})"
        elif type_name == "float":
            return f"float({expr})"
        elif type_name == "bool":
            return f"bool({expr})"
        return expr

    def visitArgList(self, ctx: cppParser.ArgListContext):
        args = []
        for expr in ctx.assignmentExpression():
            arg = self.visit(expr)
            if arg:
                args.append(arg)
        return ", ".join(args)

    def visitConditionalExpression(self, ctx: cppParser.ConditionalExpressionContext):
        if not ctx.assignmentExpression():  # 没有条件运算符
            return self.visit(ctx.logicalExpression())
            
        condition = self.visit(ctx.logicalExpression())
        true_expr = self.visit(ctx.assignmentExpression(0))
        false_expr = self.visit(ctx.assignmentExpression(1))
        
        # 转换三元运算符为Python的条件表达式
        return f"{true_expr} if {condition} else {false_expr}"