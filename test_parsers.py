from lib.earley import EarleyParser
from lib.input import InputParser


def test_input_failure1():
    with open('test_inputs/invalid_format_test1') as file:
        input_parser = InputParser(file)
        assert input_parser.parse() == None


def test_input_failure2():
    with open('test_inputs/invalid_format_test2') as file:
        input_parser = InputParser(file)
        assert input_parser.parse() == None


def test_input_failure3():
    with open('test_inputs/invalid_format_test3') as file:
        input_parser = InputParser(file)
        assert input_parser.parse() == None


def test_ok_result1():
    with open('test_inputs/test_ok1') as file:
        input_parser = InputParser(file)
        parsed_data = input_parser.parse()
        assert parsed_data != None
        word, nonterminal, rules = parsed_data
        parser = EarleyParser(word, nonterminal, rules)
        assert parser.check()


def test_ok_result2():
    with open('test_inputs/test_ok2') as file:
        input_parser = InputParser(file)
        parsed_data = input_parser.parse()
        assert parsed_data != None
        word, nonterminal, rules = parsed_data
        parser = EarleyParser(word, nonterminal, rules)
        assert parser.check()


def test_ok_result3():
    with open('test_inputs/test_ok3') as file:
        input_parser = InputParser(file)
        parsed_data = input_parser.parse()
        assert parsed_data != None
        word, nonterminal, rules = parsed_data
        parser = EarleyParser(word, nonterminal, rules)
        assert parser.check()


def test_ok_result4():
    with open('test_inputs/test_ok4') as file:
        input_parser = InputParser(file)
        parsed_data = input_parser.parse()
        assert parsed_data != None
        word, nonterminal, rules = parsed_data
        parser = EarleyParser(word, nonterminal, rules)
        assert parser.check()


def test_fail_result1():
    with open('test_inputs/test_fail1') as file:
        input_parser = InputParser(file)
        parsed_data = input_parser.parse()
        assert parsed_data != None
        word, nonterminal, rules = parsed_data
        parser = EarleyParser(word, nonterminal, rules)
        assert not parser.check()


def test_fail_result2():
    with open('test_inputs/test_fail2') as file:
        input_parser = InputParser(file)
        parsed_data = input_parser.parse()
        assert parsed_data != None
        word, nonterminal, rules = parsed_data
        parser = EarleyParser(word, nonterminal, rules)
        assert not parser.check()


def test_fail_result3():
    with open('test_inputs/test_fail3') as file:
        input_parser = InputParser(file)
        parsed_data = input_parser.parse()
        assert parsed_data != None
        word, nonterminal, rules = parsed_data
        parser = EarleyParser(word, nonterminal, rules)
        assert not parser.check()


def test_fail_result4():
    with open('test_inputs/test_fail4') as file:
        input_parser = InputParser(file)
        parsed_data = input_parser.parse()
        assert parsed_data != None
        word, nonterminal, rules = parsed_data
        parser = EarleyParser(word, nonterminal, rules)
        assert not parser.check()

