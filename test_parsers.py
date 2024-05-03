from lib.earley import EarleyParser
from lib.input import InputParser

def input_failure(path):
    with open(path) as file:
        input_parser = InputParser(file)
        assert input_parser.parse() == None

def test_input_failure1():
    input_failure('test_inputs/invalid_format_test1')


def test_input_failure2():
    input_failure('test_inputs/invalid_format_test2')


def test_input_failure3():
    input_failure('test_inputs/invalid_format_test3')


def ok_or_not_result(path, desired_result):
    with open(path) as file:
        input_parser = InputParser(file)
        parsed_data = input_parser.parse()
        assert parsed_data != None
        word, nonterminal, rules = parsed_data
        parser = EarleyParser(word, nonterminal, rules)
        assert parser.check() == desired_result


def test_ok_result1():
    ok_or_not_result('test_inputs/test_ok1', True)


def test_ok_result2():
    ok_or_not_result('test_inputs/test_ok2', True)


def test_ok_result3():
    ok_or_not_result('test_inputs/test_ok3', True)


def test_ok_result4():
    ok_or_not_result('test_inputs/test_ok4', True)


def test_fail_result1():
    ok_or_not_result('test_inputs/test_fail1', False)


def test_fail_result2():
    ok_or_not_result('test_inputs/test_fail2', False)


def test_fail_result3():
    ok_or_not_result('test_inputs/test_fail3', False)


def test_fail_result4():
    ok_or_not_result('test_inputs/test_fail4', False)

