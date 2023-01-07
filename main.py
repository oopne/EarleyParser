from lib.earley import EarleyParser
from lib.input import InputParser
from sys import stdin

def main():
    input_parser = InputParser(stdin)
    parsed_data = input_parser.parse()
    if parsed_data == None:
        print('Invalid input format!')
        return

    word, start_nonterminal, rules = parsed_data
    earley_parser = EarleyParser(word, start_nonterminal, rules)
    print('Derivable' if earley_parser.check() else 'Underivable')


if __name__ == '__main__':
    main()
