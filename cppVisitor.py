# Generated from cpp.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .cppParser import cppParser
else:
    from cppParser import cppParser

# This class defines a complete generic visitor for a parse tree produced by cppParser.

class cppVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cppParser#program.
    def visitProgram(self, ctx:cppParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#includeDirective.
    def visitIncludeDirective(self, ctx:cppParser.IncludeDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#usingNamespaceDeclaration.
    def visitUsingNamespaceDeclaration(self, ctx:cppParser.UsingNamespaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:cppParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#parameterList.
    def visitParameterList(self, ctx:cppParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#parameter.
    def visitParameter(self, ctx:cppParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#parameterTypeSpecifier.
    def visitParameterTypeSpecifier(self, ctx:cppParser.ParameterTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:cppParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#baseTypeSpecifier.
    def visitBaseTypeSpecifier(self, ctx:cppParser.BaseTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#containerTypeSpecifier.
    def visitContainerTypeSpecifier(self, ctx:cppParser.ContainerTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#qualifiedIdentifier.
    def visitQualifiedIdentifier(self, ctx:cppParser.QualifiedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#templateType.
    def visitTemplateType(self, ctx:cppParser.TemplateTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#compoundStatement.
    def visitCompoundStatement(self, ctx:cppParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#statement.
    def visitStatement(self, ctx:cppParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:cppParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:cppParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:cppParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initDeclarator.
    def visitInitDeclarator(self, ctx:cppParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#arraySubscript.
    def visitArraySubscript(self, ctx:cppParser.ArraySubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#initializer.
    def visitInitializer(self, ctx:cppParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#expressionStatement.
    def visitExpressionStatement(self, ctx:cppParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#expStatement.
    def visitExpStatement(self, ctx:cppParser.ExpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#selectionStatement.
    def visitSelectionStatement(self, ctx:cppParser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#iterationStatement.
    def visitIterationStatement(self, ctx:cppParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#jumpStatement.
    def visitJumpStatement(self, ctx:cppParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:cppParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#logicalExpression.
    def visitLogicalExpression(self, ctx:cppParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#ToLogicalAnd.
    def visitToLogicalAnd(self, ctx:cppParser.ToLogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#OrExpression.
    def visitOrExpression(self, ctx:cppParser.OrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#ToEquality.
    def visitToEquality(self, ctx:cppParser.ToEqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#AndExpression.
    def visitAndExpression(self, ctx:cppParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#ToRelational.
    def visitToRelational(self, ctx:cppParser.ToRelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#Equality.
    def visitEquality(self, ctx:cppParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#ToOperation.
    def visitToOperation(self, ctx:cppParser.ToOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#Relational.
    def visitRelational(self, ctx:cppParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#operationExpression.
    def visitOperationExpression(self, ctx:cppParser.OperationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#Add.
    def visitAdd(self, ctx:cppParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#ToMultiplication.
    def visitToMultiplication(self, ctx:cppParser.ToMultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#Subtract.
    def visitSubtract(self, ctx:cppParser.SubtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#Divide.
    def visitDivide(self, ctx:cppParser.DivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#Multiply.
    def visitMultiply(self, ctx:cppParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#ToPrimary.
    def visitToPrimary(self, ctx:cppParser.ToPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#PreIncrement.
    def visitPreIncrement(self, ctx:cppParser.PreIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#PreDecrement.
    def visitPreDecrement(self, ctx:cppParser.PreDecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#NotExpression.
    def visitNotExpression(self, ctx:cppParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#ToPostfix.
    def visitToPostfix(self, ctx:cppParser.ToPostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#PostIncrementOrDecrement.
    def visitPostIncrementOrDecrement(self, ctx:cppParser.PostIncrementOrDecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:cppParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#backFunctionName.
    def visitBackFunctionName(self, ctx:cppParser.BackFunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#frontFunctionName.
    def visitFrontFunctionName(self, ctx:cppParser.FrontFunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#turnExpression.
    def visitTurnExpression(self, ctx:cppParser.TurnExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#argList.
    def visitArgList(self, ctx:cppParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:cppParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#inputStream.
    def visitInputStream(self, ctx:cppParser.InputStreamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#inputStreamTarget.
    def visitInputStreamTarget(self, ctx:cppParser.InputStreamTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#outputStream.
    def visitOutputStream(self, ctx:cppParser.OutputStreamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#outputStreamTarget.
    def visitOutputStreamTarget(self, ctx:cppParser.OutputStreamTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppParser#outExpression.
    def visitOutExpression(self, ctx:cppParser.OutExpressionContext):
        return self.visitChildren(ctx)



del cppParser