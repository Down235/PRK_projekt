# Generated from calc_grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .calc_grammarParser import calc_grammarParser
else:
    from calc_grammarParser import calc_grammarParser

# This class defines a complete listener for a parse tree produced by calc_grammarParser.
class calc_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by calc_grammarParser#syntax.
    def enterSyntax(self, ctx:calc_grammarParser.SyntaxContext):
        pass

    # Exit a parse tree produced by calc_grammarParser#syntax.
    def exitSyntax(self, ctx:calc_grammarParser.SyntaxContext):
        pass


    # Enter a parse tree produced by calc_grammarParser#expr.
    def enterExpr(self, ctx:calc_grammarParser.ExprContext):
        pass

    # Exit a parse tree produced by calc_grammarParser#expr.
    def exitExpr(self, ctx:calc_grammarParser.ExprContext):
        pass


    # Enter a parse tree produced by calc_grammarParser#term.
    def enterTerm(self, ctx:calc_grammarParser.TermContext):
        pass

    # Exit a parse tree produced by calc_grammarParser#term.
    def exitTerm(self, ctx:calc_grammarParser.TermContext):
        pass


    # Enter a parse tree produced by calc_grammarParser#factor.
    def enterFactor(self, ctx:calc_grammarParser.FactorContext):
        pass

    # Exit a parse tree produced by calc_grammarParser#factor.
    def exitFactor(self, ctx:calc_grammarParser.FactorContext):
        pass


    # Enter a parse tree produced by calc_grammarParser#nmr.
    def enterNmr(self, ctx:calc_grammarParser.NmrContext):
        pass

    # Exit a parse tree produced by calc_grammarParser#nmr.
    def exitNmr(self, ctx:calc_grammarParser.NmrContext):
        pass


    # Enter a parse tree produced by calc_grammarParser#inv.
    def enterInv(self, ctx:calc_grammarParser.InvContext):
        pass

    # Exit a parse tree produced by calc_grammarParser#inv.
    def exitInv(self, ctx:calc_grammarParser.InvContext):
        pass


    # Enter a parse tree produced by calc_grammarParser#log.
    def enterLog(self, ctx:calc_grammarParser.LogContext):
        pass

    # Exit a parse tree produced by calc_grammarParser#log.
    def exitLog(self, ctx:calc_grammarParser.LogContext):
        pass


    # Enter a parse tree produced by calc_grammarParser#digits.
    def enterDigits(self, ctx:calc_grammarParser.DigitsContext):
        pass

    # Exit a parse tree produced by calc_grammarParser#digits.
    def exitDigits(self, ctx:calc_grammarParser.DigitsContext):
        pass


    # Enter a parse tree produced by calc_grammarParser#digit.
    def enterDigit(self, ctx:calc_grammarParser.DigitContext):
        pass

    # Exit a parse tree produced by calc_grammarParser#digit.
    def exitDigit(self, ctx:calc_grammarParser.DigitContext):
        pass



del calc_grammarParser