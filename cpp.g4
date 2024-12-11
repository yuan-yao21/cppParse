grammar cpp;

//------------------------
// Parser Rules
//------------------------


//TODO:加入结构体处理
program
    : (includeDirective | usingNamespaceDeclaration | functionDefinition | declarationStatement | expressionStatement )* EOF
    ; // 程序的起始规则，包括include指令、函数定义、声明语句、表达式语句，以EOF结束

includeDirective
    : '#' INCLUDE ( IncludeFileName | StringLiteral ) NEWLINE*
    ; // 处理#include指令，可以使用尖括号或引号

usingNamespaceDeclaration
    : USING NAMESPACE STD ';' NEWLINE*
    ; // 用于解析using namespace声明

functionDefinition
    : typeSpecifier ID '(' parameterList? ')' compoundStatement
    ; // 函数定义，包括返回类型、函数名、参数列表和函数体

parameterList
    : parameter (',' parameter)*
    ; // 参数列表，由一个或多个参数组成

parameter
    : parameterTypeSpecifier ID
    ; // 单个参数，包括参数类型说明符和参数名

parameterTypeSpecifier
    : typeSpecifier 
    ; // 参数类型说明符，可能包含const和引用符号



typeSpecifier
    : CONST? baseTypeSpecifier ( '&' | '*')?
    | CONST? containerTypeSpecifier ( '&' | '*')?
    ;

baseTypeSpecifier
    : INT
    | BOOL
    | STRING
    | VOID
    | CHAR
    | DOUBLE
    | FLOAT
    | SIZE_T
    | STRING_STREAM
    ;
    //| templateType
    //; // 基本类型说明符，包括基本类型、限定标识符和模板类型

containerTypeSpecifier
    : VECTOR '<' baseTypeSpecifier '>'
    | STACK '<' baseTypeSpecifier '>'
    ;// 容器类型说明符（vector、stack等标准模板库容器）

//TODO:限定 std:: 在string和cin，cout后面
qualifiedIdentifier
    : STD DOUBLE_COLON
    ; // 限定标识符，例如std::string

templateType
    : qualifiedIdentifier '<' typeSpecifier ('<' typeSpecifier '>')? '>'
    ; // 模板类型，例如std::vector<int>

compoundStatement
    : '{'? statement* '}'?
    ; // 复合语句，由大括号括起来的零个或多个语句组成

statement
    : declarationStatement
    | expressionStatement
    | selectionStatement
    | iterationStatement
    | jumpStatement
    | inputStream
    | outputStream
    ; // 语句，包括声明、表达式、选择、循环、跳转和复合语句

declarationStatement
    : variableDeclaration ';'
    ; // 声明语句，以分号结束

variableDeclaration
    : typeSpecifier initDeclaratorList
    ; // 变量声明，包括类型说明符和初始化声明符列表

initDeclaratorList
    : initDeclarator (',' initDeclarator)*
    ; // 初始化声明符列表

//TODO：对于expression和declaration加入对于等式左边的扩展
initDeclarator
    : ID arraySubscript? ('=' initializer)? 
    | ID '(' primaryExpr (',' primaryExpr)* ')'       // 特别处理stringstream的定义
    ; // 初始化声明符，包含标识符和可选的初始化器

arraySubscript
    : '[' assignmentExpression ']'
    ;

initializer
    : assignmentExpression
    ; // 初始化器，是一个赋值表达式

expressionStatement
    : expStatement ';'
    ; // 表达式语句，以分号结束，可以为空

expStatement
    : ( (ID arraySubscript? ('+=' | '-=' | '=' ) initializer) | initializer)? 
    ; // 表达式语句，以分号结束，可以为空

selectionStatement
    : 'if' '(' logicalExpression ')' compoundStatement ( 'else' 'if' '(' logicalExpression ')' compoundStatement )* ('else'  compoundStatement)?
    ; // 选择语句，包括if和可选的else

iterationStatement
    : 'while' '(' logicalExpression ')' compoundStatement
    | 'for' '(' (variableDeclaration | expStatement) ';' logicalExpression ';' expStatement ')' compoundStatement
    ; // 循环语句，包括while和for循环

jumpStatement
    : 'return' ( assignmentExpression | BooleanLiteral | StringLiteral | NUMBER) ? ';'
    ; // 跳转语句，包括return语句

assignmentExpression
    : '('? operationExpression ')'?
    | '('? conditionalExpression ')'?
    ; // 赋值表达式

logicalExpression
    : logicalOrExpr
    | GET '(' ID ',' ID ',' StringLiteral ')' //特别处理getline
    ; // 处理条件语句

logicalOrExpr
    : logicalOrExpr '||' logicalAndExpr      # OrExpression
    | logicalAndExpr                         # ToLogicalAnd
    ; // 逻辑或表达式

logicalAndExpr
    : logicalAndExpr '&&' equalityExpr       # AndExpression
    | equalityExpr                           # ToEquality
    ; // 逻辑与表达式

equalityExpr
    : equalityExpr ('==' | '!=') relationalExpr # Equality
    | relationalExpr                           # ToRelational
    ; // 等式表达式

relationalExpr
    : relationalExpr ('<=' | '>=' | '<' | '>') operationExpression # Relational
    | operationExpression                                   # ToOperation
    ; // 关系表达式


operationExpression
    : additionExpr
    ; // 处理四则运算 

additionExpr
    : additionExpr '+' multiplicationExpr  # Add
    | additionExpr '-' multiplicationExpr  # Subtract
    | multiplicationExpr                   # ToMultiplication
    ; // 加减运算

multiplicationExpr
    : multiplicationExpr '*' unaryExpr     # Multiply
    | multiplicationExpr '/' unaryExpr     # Divide
    | unaryExpr                            # ToPrimary
    ; // 乘除运算

unaryExpr
    : '++' postfixExpr                               # PreIncrement
    | '--' postfixExpr                               # PreDecrement
    | '!' postfixExpr                                # NotExpression
    | postfixExpr                                  # ToPostfix
    ;// 一元表达式

postfixExpr
    : primaryExpr ('++' | '--')?                   # PostIncrementOrDecrement
    ;// 后缀表达式

primaryExpr
    : NUMBER              
    | StringLiteral             
    | BooleanLiteral     
    | ID                                      
    | ID '[' argList ']'    
    | ID '.' backFunctionName '(' argList? ')'             
    | frontFunctionName '(' argList? ')'                    
    | '(' operationExpression ')'
    | '(' logicalExpression ')'      
    | turnExpression        
    ;// 基础表达式

backFunctionName
    : ID
    | BACK_FUNCTION
    ; // 后置函数定义名称

frontFunctionName
    : ID
    | FRONT_FUNCTION
    ; // 前置函数

turnExpression
    : typeSpecifier '(' primaryExpr ')'
    ;// 处理强转，如string(" ")

argList
    : assignmentExpression (',' assignmentExpression)*       
    ; // 参数列表

conditionalExpression
    : logicalExpression ('?' assignmentExpression ':' assignmentExpression)?
    ; // 条件表达式

inputStream
    : CIN '>>' inputStreamTarget ';'
    | GET '(' CIN ',' ID ')' ';'
    ;// 输入流语句

inputStreamTarget
    : ID                             
    | ID RIGHT_SHIFT inputStreamTarget     
    ;

outputStream
    : COUT '<<' outputStreamTarget ';'
    ;// 输出流语句

outputStreamTarget
    : outExpression                // 输出表达式
    | outExpression '<<' outputStreamTarget  // 链式输出操作
    ;

outExpression
    : ENDL                           // 输出endl
    | assignmentExpression           // 输出表达式
    ;


//----------------------------------------
// Lexer Rules
//----------------------------------------

HASH
    : '#'
    ; // 井号，用于预处理指令

INCLUDE
    : 'include'
    ; // include关键字

StringLiteral
    : '"' ( ~["\\\r\n] | '\\' . )* '"'
    | '\'' ( ~['\\\r\n] | '\\' . )* '\''
    ; // 字符串字面量，支持转义字符

IncludeFileName
    : '<' LIBRARY_FILE '>'
    ; // 包含文件名，不包括尖括号、引号和换行符

fragment LIBRARY_FILE 
            : 'iostream' 
            | 'vector' 
            | 'string' 
            | 'fstream'
            | 'algorithm'
            | 'sstream'
            | 'stack'
            | 'cctype'
            | 'map'
            ;

BACK_FUNCTION
    : 'size'
    | 'begin'
    | 'end'
    | 'push_back'
    | 'length'
    | 'push'
    | 'empty'
    | 'top'
    | 'pop'
    ;

FRONT_FUNCTION
    : 'stoi'
    | 'isdigit'
    ;

BooleanLiteral
    : 'true'
    | 'false'
    ; // 布尔字面量



// Operators and Delimiters

LEFT_SHIFT      : '<<' ;       // 输出流操作符
RIGHT_SHIFT     : '>>' ;       // 输入流操作符
EQUAL           : '==';
PLUS_EQUAL      : '+=';
MINUS_EQUAL     : '-=';
NOT_EQUAL       : '!=';
LESS_EQUAL      : '<=';
GREATER_EQUAL   : '>=';
NOT             : '!';
AND_OP          : '&&';
OR_OP           : '||';
QUESTION        : '?';
SEMICOLON       : ';';
COMMA           : ',';
DOT             : '.';
ARROW           : '->';
LPAREN          : '(';
RPAREN          : ')';
LBRACE          : '{';
RBRACE          : '}';
LBRACK          : '[';
RBRACK          : ']';
INCREMENT       : '++';
DECREMENT       : '--';
//BITWISE_AND     : '&';
BITWISE_OR      : '|';
BITWISE_XOR     : '^';
BITWISE_NOT     : '~';
DOUBLE_COLON    : '::' ;
AMPERSAND       : '&' ;
PLUS            : '+';
MINUS           : '-';
STAR            : '*';
DIV             : '/';
MOD             : '%';
ASSIGN          : '=';
LESS            : '<';
GREATER         : '>';
COLON           : ':';

// Keywords
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
FOR     : 'for';
RETURN  : 'return';
SIZE_T    : 'size_t';  
STRING_STREAM :'stringstream';
INT     : 'int';
STRING  : 'string' ;
BOOL    : 'bool';
DOUBLE  : 'double';
FLOAT   : 'float';
VOID    : 'void';
CHAR    : 'char';
VECTOR  : 'vector';
STACK   : 'stack';
CONST   : 'const';
STD     : 'std';
USING   : 'using' ;
NAMESPACE : 'namespace' ;
GET     : 'getline';
CIN     : 'cin' ;      // 标识符 cin
COUT    : 'cout' ;     // 标识符 cout
ENDL    : 'endl' ;     // 行结束标志

NUMBER  
    : '-'? [0-9]+ ('.' [0-9]+)? 
    ; // 数字

ID
    : [a-zA-Z0-9][a-zA-Z0-9_]*
    ; // 标识符，由字母、数字和下划线组成，不能以数字开头

// Whitespace and Comments
WS
    : [ \t\r\n]+ -> skip
    ; // 空白字符，跳过

COMMENT
    : '//' ~[\r\n]* -> skip
    ; // 单行注释，跳过

MULTILINE_COMMENT
    : '/*' .*? '*/' -> skip
    ; // 多行注释，跳过

NEWLINE : [\r\n]+ -> skip ;

