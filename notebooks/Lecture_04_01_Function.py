from MyFunctions.traingle import calculate_area, calculate_perimeter, calculate_hypotenuse


area = calculate_area(10, 5)
perimeter = calculate_perimeter(3, 4, 5)
hypotenuse = calculate_hypotenuse(3, 4)
hypotenuse = calculate_hypotenuse(3, '4')
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
print(f"Hypotenuse: {hypotenuse}")