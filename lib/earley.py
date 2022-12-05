from collections import defaultdict

class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Situation:
    PRIME = 999983

    def __init__(self, rule, point, read_before):
        self.rule = rule
        self.point = point
        self.read_before = read_before

    def __eq__(self, other):
        return self.rule == other.rule and\
                self.point == other.point and\
                self.read_before == other.read_before

    def __hash__(self):
        return self.rule + self.point * self.PRIME +\
                self.read_before * self.PRIME * self.PRIME


class EarleyParser:
    _END_OF_STRING = -1
    _NEW_START_NONTERMINAL = -2

    def __init__(self, word, start_nonterminal, rules):
        self._rules = rules
        for rule in self._rules:
            rule.right.append(self._END_OF_STRING)
        self._word = word
        self._START_NONTERMINAL = start_nonterminal
        # D_j is a map (symbol after .) -> (situation)
        self._stages = [defaultdict(lambda: []) for i in range(len(word) + 1)]
        self._processed_situations = set()

    def __scan(self, index):
        changed = False
        for situation in self._stages[index][self._word[index]]:
            rule = situation.rule
            new_point = situation.point + 1
            new_situation = Situation(
                rule,
                new_point,
                situation.read_before,
                )
            self._stages[index + 1][self._rules[rule].right[new_point]].append(
                new_situation,
                )
            self._processed_situations.add(new_situation)
            changed = True

        return changed

    def __predict(self, index):
        changed = False
        for i in range(len(self._rules)):
            nonterminal = self._rules[i].left
            first_symbol = self._rules[i].right[0]

            j = 0
            while j < len(self._stages[index][nonterminal]):
                new_situation = Situation(i, 0, index)
                if new_situation not in self._processed_situations:
                    self._stages[index][first_symbol].append(new_situation)
                    self._processed_situations.add(new_situation)
                    changed = True
                j += 1

        return changed

    def __complete(self, index):
        changed = False
        # self._stages[index][-1] is D_index[$]
        i = 0
        while i < len(self._stages[index][self._END_OF_STRING]):
            situation = self._stages[index][self._END_OF_STRING][i]
            nonterminal = self._rules[situation.rule].left
            read_before = situation.read_before

            j = 0
            while j < len(self._stages[read_before][nonterminal]):
                before_situation = self._stages[read_before][nonterminal][j]
                rule = before_situation.rule
                new_situation = Situation(
                    rule,
                    before_situation.point + 1,
                    before_situation.read_before,
                    )
                next_symbol = self._rules[rule].right[new_situation.point]

                if new_situation not in self._processed_situations:
                    self._stages[index][next_symbol].append(new_situation)
                    self._processed_situations.add(new_situation)
                    changed = True
                j += 1

            i += 1

        return changed

    def check(self):
        new_rule = len(self._rules)
        self._rules.append(Rule(
            self._NEW_START_NONTERMINAL,
            (self._START_NONTERMINAL, self._END_OF_STRING),
            ))
        self._stages[0][self._START_NONTERMINAL].append(
            Situation(new_rule, 0, 0),
            )
        self._processed_situations.add(Situation(new_rule, 0, 0))
        
        while True:
            changed = False
            if self.__complete(0):
                changed = True
            if self.__predict(0):
                changed = True
            break
            if not changed:
                break
        
        for i in range(1, len(self._word) + 1):
            self._processed_situations.clear()
            self.__scan(i - 1)

            while True:
                changed = False
                if self.__complete(i):
                    changed = True
                if self.__predict(i):
                    changed = True

                if not changed:
                    break
        
        return Situation(new_rule, 1, 0) in self._processed_situations

