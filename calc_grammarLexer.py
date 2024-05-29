# Generated from calc_grammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,52,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,
        4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,
        9,4,9,47,8,9,11,9,12,9,48,1,9,1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,19,10,1,0,3,1,0,48,48,1,0,49,57,3,0,9,10,13,13,
        32,32,52,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,
        0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,
        0,0,1,21,1,0,0,0,3,23,1,0,0,0,5,25,1,0,0,0,7,27,1,0,0,0,9,29,1,0,
        0,0,11,31,1,0,0,0,13,33,1,0,0,0,15,35,1,0,0,0,17,40,1,0,0,0,19,46,
        1,0,0,0,21,22,5,44,0,0,22,2,1,0,0,0,23,24,5,40,0,0,24,4,1,0,0,0,
        25,26,5,41,0,0,26,6,1,0,0,0,27,28,5,43,0,0,28,8,1,0,0,0,29,30,5,
        42,0,0,30,10,1,0,0,0,31,32,7,0,0,0,32,12,1,0,0,0,33,34,7,1,0,0,34,
        14,1,0,0,0,35,36,5,105,0,0,36,37,5,110,0,0,37,38,5,118,0,0,38,39,
        5,40,0,0,39,16,1,0,0,0,40,41,5,108,0,0,41,42,5,111,0,0,42,43,5,103,
        0,0,43,44,5,40,0,0,44,18,1,0,0,0,45,47,7,2,0,0,46,45,1,0,0,0,47,
        48,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,51,6,9,0,
        0,51,20,1,0,0,0,2,0,48,1,6,0,0
    ]

class calc_grammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMA = 1
    LPAREN = 2
    RPAREN = 3
    PLUS = 4
    MLPLY = 5
    ZERO = 6
    NonZeroD = 7
    InvStart = 8
    LogStart = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'('", "')'", "'+'", "'*'", "'inv('", "'log('" ]

    symbolicNames = [ "<INVALID>",
            "COMMA", "LPAREN", "RPAREN", "PLUS", "MLPLY", "ZERO", "NonZeroD", 
            "InvStart", "LogStart", "WS" ]

    ruleNames = [ "COMMA", "LPAREN", "RPAREN", "PLUS", "MLPLY", "ZERO", 
                  "NonZeroD", "InvStart", "LogStart", "WS" ]

    grammarFileName = "calc_grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


