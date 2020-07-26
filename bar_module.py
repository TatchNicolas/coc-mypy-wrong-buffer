"""
importing a function with a mypy error

This is a comment but it shows the mypy error in foo_module
"""
from foo_module import func_without_return_type_hint


def func_with_return_type_hint() -> str:
    return func_without_return_type_hint
