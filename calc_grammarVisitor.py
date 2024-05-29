# Generated from calc_grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .calc_grammarParser import calc_grammarParser
else:
    from calc_grammarParser import calc_grammarParser

# This class defines a complete generic visitor for a parse tree produced by calc_grammarParser.

class calc_grammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calc_grammarParser#syntax.
    def visitSyntax(self, ctx:calc_grammarParser.SyntaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calc_grammarParser#expr.
    def visitExpr(self, ctx:calc_grammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calc_grammarParser#term.
    def visitTerm(self, ctx:calc_grammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calc_grammarParser#factor.
    def visitFactor(self, ctx:calc_grammarParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calc_grammarParser#nmr.
    def visitNmr(self, ctx:calc_grammarParser.NmrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calc_grammarParser#inv.
    def visitInv(self, ctx:calc_grammarParser.InvContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calc_grammarParser#log.
    def visitLog(self, ctx:calc_grammarParser.LogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calc_grammarParser#digits.
    def visitDigits(self, ctx:calc_grammarParser.DigitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calc_grammarParser#digit.
    def visitDigit(self, ctx:calc_grammarParser.DigitContext):
        return self.visitChildren(ctx)



del calc_grammarParser