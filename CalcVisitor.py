import math
from calc_grammarVisitor import calc_grammarVisitor
from calc_grammarParser import calc_grammarParser

class CalcVisitor(calc_grammarVisitor):
    def visitSyntax(self, ctx: calc_grammarParser.SyntaxContext):
        result = self.visit(ctx.expr())
        return result

    def visitExpr(self, ctx: calc_grammarParser.ExprContext):
        result = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            result += self.visit(ctx.term(i))
        return result

    def visitTerm(self, ctx: calc_grammarParser.TermContext):
        result = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            result *= self.visit(ctx.factor(i))
        return result

    def visitFactor(self, ctx: calc_grammarParser.FactorContext):
        if ctx.LPAREN():
            result = self.visit(ctx.expr())
        else:
            result = self.visit(ctx.nmr())
        return result

    def visitNmr(self, ctx: calc_grammarParser.NmrContext):
        if ctx.inv():
            result = 1 / self.visit(ctx.inv().expr())
        elif ctx.log():
            result = math.log10(self.visit(ctx.log().expr()))
        else:
            number_text = ""
            if ctx.ZERO():
                number_text = "0"
            elif ctx.digits():
                number_text += self.visitDigits(ctx.digits(0))

            if ctx.COMMA():
                fractional_part = ""
                if ctx.digits(1) is not None:  # Second occurrence of digits after comma
                    fractional_part = self.visitDigits(ctx.digits(1))
                number_text += "." + fractional_part

            result = float(number_text)
        return result

    def visitDigits(self, ctx: calc_grammarParser.DigitsContext):
        result = ctx.getText()
        return result

    def visitInv(self, ctx: calc_grammarParser.InvContext):
        result = self.visit(ctx.expr())
        return result

    def visitLog(self, ctx: calc_grammarParser.LogContext):
        result = self.visit(ctx.expr())
        return result
