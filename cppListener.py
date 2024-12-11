# Generated from cpp.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .cppParser import cppParser
else:
    from cppParser import cppParser

# This class defines a complete listener for a parse tree produced by cppParser.
class cppListener(ParseTreeListener):

    # Enter a parse tree produced by cppParser#program.
    def enterProgram(self, ctx:cppParser.ProgramContext):
        pass

    # Exit a parse tree produced by cppParser#program.
    def exitProgram(self, ctx:cppParser.ProgramContext):
        pass


    # Enter a parse tree produced by cppParser#includeDirective.
    def enterIncludeDirective(self, ctx:cppParser.IncludeDirectiveContext):
        pass

    # Exit a parse tree produced by cppParser#includeDirective.
    def exitIncludeDirective(self, ctx:cppParser.IncludeDirectiveContext):
        pass


    # Enter a parse tree produced by cppParser#usingNamespaceDeclaration.
    def enterUsingNamespaceDeclaration(self, ctx:cppParser.UsingNamespaceDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#usingNamespaceDeclaration.
    def exitUsingNamespaceDeclaration(self, ctx:cppParser.UsingNamespaceDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:cppParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by cppParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:cppParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by cppParser#parameterList.
    def enterParameterList(self, ctx:cppParser.ParameterListContext):
        pass

    # Exit a parse tree produced by cppParser#parameterList.
    def exitParameterList(self, ctx:cppParser.ParameterListContext):
        pass


    # Enter a parse tree produced by cppParser#parameter.
    def enterParameter(self, ctx:cppParser.ParameterContext):
        pass

    # Exit a parse tree produced by cppParser#parameter.
    def exitParameter(self, ctx:cppParser.ParameterContext):
        pass


    # Enter a parse tree produced by cppParser#parameterTypeSpecifier.
    def enterParameterTypeSpecifier(self, ctx:cppParser.ParameterTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#parameterTypeSpecifier.
    def exitParameterTypeSpecifier(self, ctx:cppParser.ParameterTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:cppParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:cppParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#baseTypeSpecifier.
    def enterBaseTypeSpecifier(self, ctx:cppParser.BaseTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#baseTypeSpecifier.
    def exitBaseTypeSpecifier(self, ctx:cppParser.BaseTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#containerTypeSpecifier.
    def enterContainerTypeSpecifier(self, ctx:cppParser.ContainerTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppParser#containerTypeSpecifier.
    def exitContainerTypeSpecifier(self, ctx:cppParser.ContainerTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppParser#qualifiedIdentifier.
    def enterQualifiedIdentifier(self, ctx:cppParser.QualifiedIdentifierContext):
        pass

    # Exit a parse tree produced by cppParser#qualifiedIdentifier.
    def exitQualifiedIdentifier(self, ctx:cppParser.QualifiedIdentifierContext):
        pass


    # Enter a parse tree produced by cppParser#templateType.
    def enterTemplateType(self, ctx:cppParser.TemplateTypeContext):
        pass

    # Exit a parse tree produced by cppParser#templateType.
    def exitTemplateType(self, ctx:cppParser.TemplateTypeContext):
        pass


    # Enter a parse tree produced by cppParser#compoundStatement.
    def enterCompoundStatement(self, ctx:cppParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by cppParser#compoundStatement.
    def exitCompoundStatement(self, ctx:cppParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by cppParser#statement.
    def enterStatement(self, ctx:cppParser.StatementContext):
        pass

    # Exit a parse tree produced by cppParser#statement.
    def exitStatement(self, ctx:cppParser.StatementContext):
        pass


    # Enter a parse tree produced by cppParser#declarationStatement.
    def enterDeclarationStatement(self, ctx:cppParser.DeclarationStatementContext):
        pass

    # Exit a parse tree produced by cppParser#declarationStatement.
    def exitDeclarationStatement(self, ctx:cppParser.DeclarationStatementContext):
        pass


    # Enter a parse tree produced by cppParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:cppParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by cppParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:cppParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by cppParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:cppParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by cppParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:cppParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by cppParser#initDeclarator.
    def enterInitDeclarator(self, ctx:cppParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by cppParser#initDeclarator.
    def exitInitDeclarator(self, ctx:cppParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by cppParser#arraySubscript.
    def enterArraySubscript(self, ctx:cppParser.ArraySubscriptContext):
        pass

    # Exit a parse tree produced by cppParser#arraySubscript.
    def exitArraySubscript(self, ctx:cppParser.ArraySubscriptContext):
        pass


    # Enter a parse tree produced by cppParser#initializer.
    def enterInitializer(self, ctx:cppParser.InitializerContext):
        pass

    # Exit a parse tree produced by cppParser#initializer.
    def exitInitializer(self, ctx:cppParser.InitializerContext):
        pass


    # Enter a parse tree produced by cppParser#expressionStatement.
    def enterExpressionStatement(self, ctx:cppParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by cppParser#expressionStatement.
    def exitExpressionStatement(self, ctx:cppParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by cppParser#expStatement.
    def enterExpStatement(self, ctx:cppParser.ExpStatementContext):
        pass

    # Exit a parse tree produced by cppParser#expStatement.
    def exitExpStatement(self, ctx:cppParser.ExpStatementContext):
        pass


    # Enter a parse tree produced by cppParser#selectionStatement.
    def enterSelectionStatement(self, ctx:cppParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by cppParser#selectionStatement.
    def exitSelectionStatement(self, ctx:cppParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by cppParser#iterationStatement.
    def enterIterationStatement(self, ctx:cppParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by cppParser#iterationStatement.
    def exitIterationStatement(self, ctx:cppParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by cppParser#jumpStatement.
    def enterJumpStatement(self, ctx:cppParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by cppParser#jumpStatement.
    def exitJumpStatement(self, ctx:cppParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by cppParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:cppParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:cppParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#logicalExpression.
    def enterLogicalExpression(self, ctx:cppParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#logicalExpression.
    def exitLogicalExpression(self, ctx:cppParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#ToLogicalAnd.
    def enterToLogicalAnd(self, ctx:cppParser.ToLogicalAndContext):
        pass

    # Exit a parse tree produced by cppParser#ToLogicalAnd.
    def exitToLogicalAnd(self, ctx:cppParser.ToLogicalAndContext):
        pass


    # Enter a parse tree produced by cppParser#OrExpression.
    def enterOrExpression(self, ctx:cppParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#OrExpression.
    def exitOrExpression(self, ctx:cppParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#ToEquality.
    def enterToEquality(self, ctx:cppParser.ToEqualityContext):
        pass

    # Exit a parse tree produced by cppParser#ToEquality.
    def exitToEquality(self, ctx:cppParser.ToEqualityContext):
        pass


    # Enter a parse tree produced by cppParser#AndExpression.
    def enterAndExpression(self, ctx:cppParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#AndExpression.
    def exitAndExpression(self, ctx:cppParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#ToRelational.
    def enterToRelational(self, ctx:cppParser.ToRelationalContext):
        pass

    # Exit a parse tree produced by cppParser#ToRelational.
    def exitToRelational(self, ctx:cppParser.ToRelationalContext):
        pass


    # Enter a parse tree produced by cppParser#Equality.
    def enterEquality(self, ctx:cppParser.EqualityContext):
        pass

    # Exit a parse tree produced by cppParser#Equality.
    def exitEquality(self, ctx:cppParser.EqualityContext):
        pass


    # Enter a parse tree produced by cppParser#ToOperation.
    def enterToOperation(self, ctx:cppParser.ToOperationContext):
        pass

    # Exit a parse tree produced by cppParser#ToOperation.
    def exitToOperation(self, ctx:cppParser.ToOperationContext):
        pass


    # Enter a parse tree produced by cppParser#Relational.
    def enterRelational(self, ctx:cppParser.RelationalContext):
        pass

    # Exit a parse tree produced by cppParser#Relational.
    def exitRelational(self, ctx:cppParser.RelationalContext):
        pass


    # Enter a parse tree produced by cppParser#operationExpression.
    def enterOperationExpression(self, ctx:cppParser.OperationExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#operationExpression.
    def exitOperationExpression(self, ctx:cppParser.OperationExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#Add.
    def enterAdd(self, ctx:cppParser.AddContext):
        pass

    # Exit a parse tree produced by cppParser#Add.
    def exitAdd(self, ctx:cppParser.AddContext):
        pass


    # Enter a parse tree produced by cppParser#ToMultiplication.
    def enterToMultiplication(self, ctx:cppParser.ToMultiplicationContext):
        pass

    # Exit a parse tree produced by cppParser#ToMultiplication.
    def exitToMultiplication(self, ctx:cppParser.ToMultiplicationContext):
        pass


    # Enter a parse tree produced by cppParser#Subtract.
    def enterSubtract(self, ctx:cppParser.SubtractContext):
        pass

    # Exit a parse tree produced by cppParser#Subtract.
    def exitSubtract(self, ctx:cppParser.SubtractContext):
        pass


    # Enter a parse tree produced by cppParser#Divide.
    def enterDivide(self, ctx:cppParser.DivideContext):
        pass

    # Exit a parse tree produced by cppParser#Divide.
    def exitDivide(self, ctx:cppParser.DivideContext):
        pass


    # Enter a parse tree produced by cppParser#Multiply.
    def enterMultiply(self, ctx:cppParser.MultiplyContext):
        pass

    # Exit a parse tree produced by cppParser#Multiply.
    def exitMultiply(self, ctx:cppParser.MultiplyContext):
        pass


    # Enter a parse tree produced by cppParser#ToPrimary.
    def enterToPrimary(self, ctx:cppParser.ToPrimaryContext):
        pass

    # Exit a parse tree produced by cppParser#ToPrimary.
    def exitToPrimary(self, ctx:cppParser.ToPrimaryContext):
        pass


    # Enter a parse tree produced by cppParser#PreIncrement.
    def enterPreIncrement(self, ctx:cppParser.PreIncrementContext):
        pass

    # Exit a parse tree produced by cppParser#PreIncrement.
    def exitPreIncrement(self, ctx:cppParser.PreIncrementContext):
        pass


    # Enter a parse tree produced by cppParser#PreDecrement.
    def enterPreDecrement(self, ctx:cppParser.PreDecrementContext):
        pass

    # Exit a parse tree produced by cppParser#PreDecrement.
    def exitPreDecrement(self, ctx:cppParser.PreDecrementContext):
        pass


    # Enter a parse tree produced by cppParser#NotExpression.
    def enterNotExpression(self, ctx:cppParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#NotExpression.
    def exitNotExpression(self, ctx:cppParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#ToPostfix.
    def enterToPostfix(self, ctx:cppParser.ToPostfixContext):
        pass

    # Exit a parse tree produced by cppParser#ToPostfix.
    def exitToPostfix(self, ctx:cppParser.ToPostfixContext):
        pass


    # Enter a parse tree produced by cppParser#PostIncrementOrDecrement.
    def enterPostIncrementOrDecrement(self, ctx:cppParser.PostIncrementOrDecrementContext):
        pass

    # Exit a parse tree produced by cppParser#PostIncrementOrDecrement.
    def exitPostIncrementOrDecrement(self, ctx:cppParser.PostIncrementOrDecrementContext):
        pass


    # Enter a parse tree produced by cppParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:cppParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by cppParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:cppParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by cppParser#backFunctionName.
    def enterBackFunctionName(self, ctx:cppParser.BackFunctionNameContext):
        pass

    # Exit a parse tree produced by cppParser#backFunctionName.
    def exitBackFunctionName(self, ctx:cppParser.BackFunctionNameContext):
        pass


    # Enter a parse tree produced by cppParser#frontFunctionName.
    def enterFrontFunctionName(self, ctx:cppParser.FrontFunctionNameContext):
        pass

    # Exit a parse tree produced by cppParser#frontFunctionName.
    def exitFrontFunctionName(self, ctx:cppParser.FrontFunctionNameContext):
        pass


    # Enter a parse tree produced by cppParser#turnExpression.
    def enterTurnExpression(self, ctx:cppParser.TurnExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#turnExpression.
    def exitTurnExpression(self, ctx:cppParser.TurnExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#argList.
    def enterArgList(self, ctx:cppParser.ArgListContext):
        pass

    # Exit a parse tree produced by cppParser#argList.
    def exitArgList(self, ctx:cppParser.ArgListContext):
        pass


    # Enter a parse tree produced by cppParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:cppParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:cppParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by cppParser#inputStream.
    def enterInputStream(self, ctx:cppParser.InputStreamContext):
        pass

    # Exit a parse tree produced by cppParser#inputStream.
    def exitInputStream(self, ctx:cppParser.InputStreamContext):
        pass


    # Enter a parse tree produced by cppParser#inputStreamTarget.
    def enterInputStreamTarget(self, ctx:cppParser.InputStreamTargetContext):
        pass

    # Exit a parse tree produced by cppParser#inputStreamTarget.
    def exitInputStreamTarget(self, ctx:cppParser.InputStreamTargetContext):
        pass


    # Enter a parse tree produced by cppParser#outputStream.
    def enterOutputStream(self, ctx:cppParser.OutputStreamContext):
        pass

    # Exit a parse tree produced by cppParser#outputStream.
    def exitOutputStream(self, ctx:cppParser.OutputStreamContext):
        pass


    # Enter a parse tree produced by cppParser#outputStreamTarget.
    def enterOutputStreamTarget(self, ctx:cppParser.OutputStreamTargetContext):
        pass

    # Exit a parse tree produced by cppParser#outputStreamTarget.
    def exitOutputStreamTarget(self, ctx:cppParser.OutputStreamTargetContext):
        pass


    # Enter a parse tree produced by cppParser#outExpression.
    def enterOutExpression(self, ctx:cppParser.OutExpressionContext):
        pass

    # Exit a parse tree produced by cppParser#outExpression.
    def exitOutExpression(self, ctx:cppParser.OutExpressionContext):
        pass



del cppParser