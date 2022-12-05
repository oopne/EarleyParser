from lib.earley import Rule

class InputParser:
    def __init__(self, file):
        self.__input = file.readline

    def welcome_message(self):
        print('Please, enter your grammar and word to check.')
        print('Format for the word: "term1""term2""term3"...')
        print('Format for start nonterminal: <nonterm>')
        print('Rule format:')
        print('<nonterm1>=<nonterm2>"term1""term2"<nonterm2>...')
        print('Put word on the 1st line, ')
        print('Nonterminals and terminals can be any strings without ", <, >.')
        print('On the last line type End')

    def __parse_word(self, word):
        if not word:
            return None

        result = []
        terminal = False
        characters = []

        for letter in word:
            if terminal:
                if letter != '"':
                    characters.append(letter)
                else:
                    result.append(''.join(characters))
                    characters.clear()
                    terminal = False
            else:
                if letter == '"':
                    terminal = True
                else:
                    return None
         
        if terminal:
            return None

        return result

    def __parse_nonterminal(self, nonterminal):
        if len(nonterminal) < 3:
            return None
        if nonterminal[0] != '<' or nonterminal[-1] != '>':
            return None
        if nonterminal.count('<') > 1 or nonterminal.count('>') > 1 or \
            nonterminal.count('"') > 0:
            return None

        return nonterminal[1 : -1]

    def __parse_rule(self, rule):
        delim_position = rule.find('=')
        left_part = self.__parse_nonterminal(rule[0 : delim_position])
        if left_part == None:
            return None
        
        terminal = False
        nonterminal = False
        characters = []
        right_part = []
        for i in range(delim_position + 1, len(rule)):
            if terminal:
                if rule[i] == '"':
                    right_part.append(''.join(characters))
                    characters.clear()
                    terminal = False
                else:
                    characters.append(rule[i])
            elif nonterminal:
                if rule[i] == '>':
                    right_part.append(''.join(characters))
                    characters.clear()
                    nonterminal = False
                else:
                    characters.append(rule[i])
            else:
                if rule[i] == '"':
                    terminal = True
                elif rule[i] == '<':
                    nonterminal = True
                else:
                    return None

        if terminal or nonterminal:
            return None

        return Rule(left_part, right_part)

    def __normalize_string(self, string):
        if len(string) > 0 and string[-1] == '\n':
            string = string[:-1]
        return string

    def parse(self):
        word = self.__normalize_string(self.__input())
        word = self.__parse_word(word)
        start_nonterminal = self.__normalize_string(self.__input())
        start_nonterminal = self.__parse_nonterminal(start_nonterminal)
        rules = []
        while True:
            rule = self.__normalize_string(self.__input())
            if rule == 'End':
                break
            rules.append(self.__parse_rule(rule))

        return (word, start_nonterminal, rules)

