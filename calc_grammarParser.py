# Generated from calc_grammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,74,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,1,1,1,1,5,1,25,8,1,10,1,12,1,28,
        9,1,1,2,1,2,1,2,5,2,33,8,2,10,2,12,2,36,9,2,1,3,1,3,1,3,1,3,1,3,
        3,3,43,8,3,1,4,1,4,1,4,3,4,48,8,4,1,4,1,4,1,4,3,4,53,8,4,1,4,1,4,
        3,4,57,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,4,7,68,8,7,11,7,12,
        7,69,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,6,7,73,0,18,
        1,0,0,0,2,21,1,0,0,0,4,29,1,0,0,0,6,42,1,0,0,0,8,56,1,0,0,0,10,58,
        1,0,0,0,12,62,1,0,0,0,14,67,1,0,0,0,16,71,1,0,0,0,18,19,3,2,1,0,
        19,20,5,0,0,1,20,1,1,0,0,0,21,26,3,4,2,0,22,23,5,4,0,0,23,25,3,4,
        2,0,24,22,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,3,
        1,0,0,0,28,26,1,0,0,0,29,34,3,6,3,0,30,31,5,5,0,0,31,33,3,6,3,0,
        32,30,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,5,1,0,
        0,0,36,34,1,0,0,0,37,38,5,2,0,0,38,39,3,2,1,0,39,40,5,3,0,0,40,43,
        1,0,0,0,41,43,3,8,4,0,42,37,1,0,0,0,42,41,1,0,0,0,43,7,1,0,0,0,44,
        47,5,6,0,0,45,46,5,1,0,0,46,48,3,14,7,0,47,45,1,0,0,0,47,48,1,0,
        0,0,48,57,1,0,0,0,49,52,3,14,7,0,50,51,5,1,0,0,51,53,3,14,7,0,52,
        50,1,0,0,0,52,53,1,0,0,0,53,57,1,0,0,0,54,57,3,10,5,0,55,57,3,12,
        6,0,56,44,1,0,0,0,56,49,1,0,0,0,56,54,1,0,0,0,56,55,1,0,0,0,57,9,
        1,0,0,0,58,59,5,8,0,0,59,60,3,2,1,0,60,61,5,3,0,0,61,11,1,0,0,0,
        62,63,5,9,0,0,63,64,3,2,1,0,64,65,5,3,0,0,65,13,1,0,0,0,66,68,3,
        16,8,0,67,66,1,0,0,0,68,69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,
        15,1,0,0,0,71,72,7,0,0,0,72,17,1,0,0,0,7,26,34,42,47,52,56,69
    ]

class calc_grammarParser ( Parser ):

    grammarFileName = "calc_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'('", "')'", "'+'", "'*'", "<INVALID>", 
                     "<INVALID>", "'inv('", "'log('" ]

    symbolicNames = [ "<INVALID>", "COMMA", "LPAREN", "RPAREN", "PLUS", 
                      "MLPLY", "ZERO", "NonZeroD", "InvStart", "LogStart", 
                      "WS" ]

    RULE_syntax = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3
    RULE_nmr = 4
    RULE_inv = 5
    RULE_log = 6
    RULE_digits = 7
    RULE_digit = 8

    ruleNames =  [ "syntax", "expr", "term", "factor", "nmr", "inv", "log", 
                   "digits", "digit" ]

    EOF = Token.EOF
    COMMA=1
    LPAREN=2
    RPAREN=3
    PLUS=4
    MLPLY=5
    ZERO=6
    NonZeroD=7
    InvStart=8
    LogStart=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SyntaxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(calc_grammarParser.ExprContext,0)


        def EOF(self):
            return self.getToken(calc_grammarParser.EOF, 0)

        def getRuleIndex(self):
            return calc_grammarParser.RULE_syntax

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSyntax" ):
                listener.enterSyntax(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSyntax" ):
                listener.exitSyntax(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSyntax" ):
                return visitor.visitSyntax(self)
            else:
                return visitor.visitChildren(self)




    def syntax(self):

        localctx = calc_grammarParser.SyntaxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_syntax)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.expr()
            self.state = 19
            self.match(calc_grammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calc_grammarParser.TermContext)
            else:
                return self.getTypedRuleContext(calc_grammarParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(calc_grammarParser.PLUS)
            else:
                return self.getToken(calc_grammarParser.PLUS, i)

        def getRuleIndex(self):
            return calc_grammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = calc_grammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.term()
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 22
                self.match(calc_grammarParser.PLUS)
                self.state = 23
                self.term()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calc_grammarParser.FactorContext)
            else:
                return self.getTypedRuleContext(calc_grammarParser.FactorContext,i)


        def MLPLY(self, i:int=None):
            if i is None:
                return self.getTokens(calc_grammarParser.MLPLY)
            else:
                return self.getToken(calc_grammarParser.MLPLY, i)

        def getRuleIndex(self):
            return calc_grammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = calc_grammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.factor()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 30
                self.match(calc_grammarParser.MLPLY)
                self.state = 31
                self.factor()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(calc_grammarParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(calc_grammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(calc_grammarParser.RPAREN, 0)

        def nmr(self):
            return self.getTypedRuleContext(calc_grammarParser.NmrContext,0)


        def getRuleIndex(self):
            return calc_grammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = calc_grammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(calc_grammarParser.LPAREN)
                self.state = 38
                self.expr()
                self.state = 39
                self.match(calc_grammarParser.RPAREN)
                pass
            elif token in [6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.nmr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NmrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZERO(self):
            return self.getToken(calc_grammarParser.ZERO, 0)

        def COMMA(self):
            return self.getToken(calc_grammarParser.COMMA, 0)

        def digits(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calc_grammarParser.DigitsContext)
            else:
                return self.getTypedRuleContext(calc_grammarParser.DigitsContext,i)


        def inv(self):
            return self.getTypedRuleContext(calc_grammarParser.InvContext,0)


        def log(self):
            return self.getTypedRuleContext(calc_grammarParser.LogContext,0)


        def getRuleIndex(self):
            return calc_grammarParser.RULE_nmr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNmr" ):
                listener.enterNmr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNmr" ):
                listener.exitNmr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNmr" ):
                return visitor.visitNmr(self)
            else:
                return visitor.visitChildren(self)




    def nmr(self):

        localctx = calc_grammarParser.NmrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_nmr)
        self._la = 0 # Token type
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(calc_grammarParser.ZERO)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 45
                    self.match(calc_grammarParser.COMMA)
                    self.state = 46
                    self.digits()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.digits()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 50
                    self.match(calc_grammarParser.COMMA)
                    self.state = 51
                    self.digits()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.inv()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.log()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def InvStart(self):
            return self.getToken(calc_grammarParser.InvStart, 0)

        def expr(self):
            return self.getTypedRuleContext(calc_grammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(calc_grammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return calc_grammarParser.RULE_inv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInv" ):
                listener.enterInv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInv" ):
                listener.exitInv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInv" ):
                return visitor.visitInv(self)
            else:
                return visitor.visitChildren(self)




    def inv(self):

        localctx = calc_grammarParser.InvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inv)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(calc_grammarParser.InvStart)
            self.state = 59
            self.expr()
            self.state = 60
            self.match(calc_grammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LogStart(self):
            return self.getToken(calc_grammarParser.LogStart, 0)

        def expr(self):
            return self.getTypedRuleContext(calc_grammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(calc_grammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return calc_grammarParser.RULE_log

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog" ):
                listener.enterLog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog" ):
                listener.exitLog(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog" ):
                return visitor.visitLog(self)
            else:
                return visitor.visitChildren(self)




    def log(self):

        localctx = calc_grammarParser.LogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_log)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(calc_grammarParser.LogStart)
            self.state = 63
            self.expr()
            self.state = 64
            self.match(calc_grammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DigitsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calc_grammarParser.DigitContext)
            else:
                return self.getTypedRuleContext(calc_grammarParser.DigitContext,i)


        def getRuleIndex(self):
            return calc_grammarParser.RULE_digits

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigits" ):
                listener.enterDigits(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigits" ):
                listener.exitDigits(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDigits" ):
                return visitor.visitDigits(self)
            else:
                return visitor.visitChildren(self)




    def digits(self):

        localctx = calc_grammarParser.DigitsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_digits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.digit()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6 or _la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZERO(self):
            return self.getToken(calc_grammarParser.ZERO, 0)

        def NonZeroD(self):
            return self.getToken(calc_grammarParser.NonZeroD, 0)

        def getRuleIndex(self):
            return calc_grammarParser.RULE_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDigit" ):
                listener.enterDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDigit" ):
                listener.exitDigit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDigit" ):
                return visitor.visitDigit(self)
            else:
                return visitor.visitChildren(self)




    def digit(self):

        localctx = calc_grammarParser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_digit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





