import pytest
from valid_parentheses import validateParentheses


def test_valid_simple_parentheses():
    assert validateParentheses("()") == True
    assert validateParentheses("[]") == True
    assert validateParentheses("{}") == True


def test_valid_multiple_parentheses():
    assert validateParentheses("()[]{}") == True
    assert validateParentheses("([])") == True
    assert validateParentheses("{[]}") == True
    assert validateParentheses("{{{}}}") == True


def test_invalid_parentheses():
    assert validateParentheses("(]") == False
    assert validateParentheses("([)]") == False
    assert validateParentheses("{[}") == False
    assert validateParentheses("((") == False


def test_empty_string():
    assert validateParentheses("") == True


def test_single_character():
    assert validateParentheses("(") == False
    assert validateParentheses("]") == False
    assert validateParentheses("{") == False


def test_nested_parentheses():
    assert validateParentheses("((()))") == True
    assert validateParentheses("{[()]}") == True
    assert validateParentheses("[{()}]") == True
