from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from calc_grammarLexer import calc_grammarLexer
from calc_grammarParser import calc_grammarParser

class ErrorReporter(ErrorListener):
    def __init__(self):
        super(ErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, message, e):
        self.errors.append(f'Error on line {line}, column {column}: {message}')
