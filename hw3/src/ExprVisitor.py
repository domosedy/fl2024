# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#start.
    def visitStart(self, ctx:ExprParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#starExpr.
    def visitStarExpr(self, ctx:ExprParser.StarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#askExpr.
    def visitAskExpr(self, ctx:ExprParser.AskExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#connectExpr.
    def visitConnectExpr(self, ctx:ExprParser.ConnectExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atomExpr.
    def visitAtomExpr(self, ctx:ExprParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#orExpr.
    def visitOrExpr(self, ctx:ExprParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#plusExpr.
    def visitPlusExpr(self, ctx:ExprParser.PlusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#charExpr.
    def visitCharExpr(self, ctx:ExprParser.CharExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parenExpr.
    def visitParenExpr(self, ctx:ExprParser.ParenExprContext):
        return self.visitChildren(ctx)



del ExprParser