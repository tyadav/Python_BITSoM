def _check_number(*values):
    if not all(isinstance(v, (int, float)) for v in values):
        raise TypeError("arguments must be int or float")

def calculate_area(base, height):
    _check_number(base, height)
    return 0.5 * float(base) * float(height)

def calculate_perimeter(side1, side2, side3):
    _check_number(side1, side2, side3)
    return float(side1) + float(side2) + float(side3)

def calculate_hypotenuse(base, height):
    _check_number(base, height)
    return (float(base) ** 2 + float(height) ** 2) ** 0.5
