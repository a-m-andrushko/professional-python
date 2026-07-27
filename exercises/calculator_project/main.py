# Clean API access directly from the package name
from calculator import *

print(f'Addition: 1 + 2 = {addition(1, 2)}')
print(f'Subtraction: 3 - 4 = {subtraction(3, 4)}')
print(f'Multiplication: 5 x 6 = {multiplication(5, 6)}')
print(f'Division: 8 / 2 = {division(8, 2)}')
print(f'Power: 2 ^ 3 = {power(2, 3)}')
print(f'Square root of 121 = {square_root(121)}')
print(f'Factorial of 4 = {factorial(4)}')