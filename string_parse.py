import unittest
from collections import Counter


def valid_brackets(input_str):
    """
    Given an input will loop each character by incrementing on an open bracket
    and decrementing on a closing bracket.
    
    When the result is 0 all brackets are balanced and the string in valid. 
    
    Its naive in the sense that it doesn't validate the order of the open/close brackets.
    
    :param input_str: 
    :return: bool 
    """
    balance = 0

    for x in input_str:
        if x == '[':
            balance += 1
        if x == ']':
            balance -= 1

    return balance == 0


def valid_brackets_extended(input_str):
    """
    Given an input will balance multiple brackets.
    
    Uses a map of open to close brackets, and a reverse of that map for close to open.
    
    Using a Counter to save a boilerplate `k in counts` code.
      
    Like before, it loops each character in the sequence incrementing the open brackets but
    in this version we have a bit more control over closing brackets, so it will only decrement
    if the relevant open bracket in a positive. That should give correct False result if a close
    is before its opener when otherwise a '}{' input would be valid.
    
    :param input_str: 
    :return: bool
    """
    bracket_map = {
        '[': ']',
        '{': '}',
        '(': ')',
        '<': '>'
    }
    reverse_map = {v: k for k, v in bracket_map.items()}

    counters = Counter()

    for n, x in enumerate(input_str):
        # Count open
        if x in bracket_map:
            counters[x] += 1

        # Count close
        if x in reverse_map:
            # Only count with opened brackets, tests the ordering
            if counters[reverse_map[x]] > 0:
                counters[reverse_map[x]] -= 1

    return len([o for o, c in counters.items() if c != 0]) == 0


class BracketTestCase(unittest.TestCase):
    """
    Testing simple version of valid brackets
    """
    def test_brackets_valid(self):
        input_str = '[][][][]'
        self.assertTrue(valid_brackets(input_str))

    def test_brackets_nested_valid(self):
        input_str = '[[]]'
        self.assertTrue(valid_brackets(input_str))

    def test_brackets_invalid(self):
        input_str = '[]]]'
        self.assertFalse(valid_brackets(input_str))

    def test_brackets_nested_invalid(self):
        input_str = '[[]]['
        self.assertFalse(valid_brackets(input_str))


class BracketExtendedTestCase(unittest.TestCase):
    """
    Testing the extended version of valid brackets
    """

    def test_bracket_order_true(self):
        input_str = '{}'
        self.assertTrue(valid_brackets_extended(input_str))

    def test_bracket_order_false(self):
        input_str = '}{'
        self.assertFalse(valid_brackets_extended(input_str))

    def test_brackets_extended_valid(self):
        input_str = '([])'
        self.assertTrue(valid_brackets_extended(input_str))

    def test_brackets_extended_invalid(self):
        input_str = '<[}{][[[]]>'
        self.assertFalse(valid_brackets_extended(input_str))


if __name__ == '__main__':
    unittest.main()
