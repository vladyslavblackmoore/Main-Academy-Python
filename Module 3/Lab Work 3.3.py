import math
import random

'''Generate sequence 5 integers long from range(0, 100)'''
randomsequencevalue = random.sample(range(0, 100), 5)

'''Generate random float'''
randomvaluefloat = random.random()

'''Print variables above'''
print(f'Random values: {randomsequencevalue}')
print(f'Random value Float: {randomvaluefloat}')

'''Find max element from generated sequence'''
print(f'Max element from generated sequence: {max(randomsequencevalue)}')

'''Make a floor division between max element and generated float'''
floordivision = max(randomsequencevalue) // randomvaluefloat
print(f'Floor division between max element and generated float: {floordivision}')

'''Find factorial of the result above'''
print(f'Factorial of the result above: {math.factorial(floordivision)}')
