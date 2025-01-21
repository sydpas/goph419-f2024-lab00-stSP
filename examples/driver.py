import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# this is to run python examples/driver.py in the terminal
# python can't find src/functions/ because examples/ isn't in the main search path
# this tells python where to look for src


from src.functions.operators import (
    add,
    multiply,
)


def main():
    a = 2
    b = 5
    print(f'Addition: {add(a, b)}')
    print(f'Multiply: {multiply(a, b)}')


if __name__ == "__main__":
    main()
