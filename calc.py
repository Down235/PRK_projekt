import sys
from antlr4 import *
from calc_grammarLexer import calc_grammarLexer
from calc_grammarParser import calc_grammarParser
from ErrorReporter import ErrorReporter
from CalcVisitor import CalcVisitor

def parse_stream(string):
    lines = string.splitlines()
    return lines

def make_output(correct_exprs):
    output_str = ''
    for item in correct_exprs:
        output_str += str(item) + '\n'
    return output_str

def calculate(tree):
    visitor = CalcVisitor()
    result = round(visitor.visit(tree), 4)
    print(f'Calculated: {result}')
    return result

def main(argv):
    try:
    
        input = open(argv[1]).read()
        input_list = parse_stream(input)
        lexer_listener = ErrorReporter()
        error_listener = ErrorReporter()
        valid_expr = []
        calculated = []
        for expr in input_list:
            lexer = calc_grammarLexer(InputStream(expr))
            lexer.removeErrorListeners()
            lexer.addErrorListener(lexer_listener)
            stream = CommonTokenStream(lexer)
            stream.fill()
            
            if lexer_listener.errors:
                print(expr)
                print('Token recognition error occured:')
                print(lexer_listener.errors[0])
                print('Expression won\'t be processed! Continuing...')
                lexer_listener.errors.clear()
                continue
                   
            parser = calc_grammarParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)

            tree = parser.syntax()
            print(expr)
            if error_listener.errors:
                print('Errors occured during parsing:')
                print(error_listener.errors[0])
                print('Object deleted from stream!')
                error_listener.errors.clear()
            else:
                print('Parsing completed successfully!')
                #print(tree.toStringTree(recog=parser), '\n')
                valid_expr.append(expr)
                calculated.append(calculate(tree))
                print('\\\\-------------------------------------------//')
        f = open('expr_output.txt', 'w')
        f.write(make_output(calculated) + '\n')

    except Exception as e:
        print(e)
        print('Operation aborted due to an exception.')

if __name__ == '__main__':
    main(sys.argv)
