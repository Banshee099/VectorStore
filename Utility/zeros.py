
def zeros(shape):
    if isinstance(shape, int):
        return [0 for _ in range(shape)]
    elif isinstance(shape, tuple) and len(shape) == 2:
        rows, cols = shape
        return [[0 for _ in range(cols)] for _ in range(rows)]
    else:
        raise ValueError("Shape must be an integer or a tuple of two integers (rows, cols).")
