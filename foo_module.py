def func_without_mypy_errors() -> None:
    pass

def func_without_return_type_hint():
    val =  "I don't have a return type hint, so mypy should raise a warining"
    return val
