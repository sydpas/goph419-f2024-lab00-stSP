from goph420_lab00.operators import (
add, 
multiply, 
subtract, 
)
 

def main():
    a = 2
    b = 5
    print(f' a: {a}, b: {b} ')
    print(f'Addition: {add(a, b)}')
    print(f'Multiply: {multiply(a, b)}')
    print(f'Subtact: {subtract(a, b)}')


if __name__ == "__main__":
    main()
