"""
*5. Напишите программу для подсчета количества символов (частоты символов) в строке (игнорируя регистр букв).
Пример:
Input: 'Oh, it is Python'
Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
"""

s = "Oh, it is Python"
s = s.lower()
a = {let: s.count(let) for let in s}
print(a)