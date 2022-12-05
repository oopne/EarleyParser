from lib.earley import EarleyParser
from lib.input_output import InputParser
from sys import stdin

def main():
    input_parser = InputParser(stdin)
    word, start_nonterminal, rules = input_parser.parse()
    earley_parser = EarleyParser(word, start_nonterminal, rules)
    print(earley_parser.check())


if __name__ == '__main__':
    main()
