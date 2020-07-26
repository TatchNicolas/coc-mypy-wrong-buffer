from foo_module import func_without_return_type_hint


def func_with_return_type_hint() -> str:
    return func_without_return_type_hint
