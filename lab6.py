import math

def factorial(x):

    if x == 0 or x == 1:
        return 1

    return x * factorial(x - 1)


def sine_x(x, n):

    x_rad = math.radians(x)

    sine_term = lambda k: ((-1) ** k * (x_rad ** (2 * k + 1))) / factorial(2 * k + 1)

    result = 0
    for k in range(n):
        result += sine_term(k)

    return result


global_result = 0


def calculate_series(n):

    global global_result

    if n == 0:
        return

    global_result += 1 / (n * (n + 1))
    calculate_series(n - 1)

def main():
    print("Factorial Tests:")
    test_values = [0, 1, 5, 7]
    for val in test_values:
        print(f"Factorial of {val}: {factorial(val)}")
    
    print("\nSine Series Tests:")
    angles = [30, 45, 60]
    terms = [3, 5, 7]
    for angle in angles:
        for term in terms:
            print(f"Sine of {angle} degrees with {term} terms: {sine_x(angle, term)}")

    print("\nGlobal Variable Series Test:")
    global global_result
    global_result = 0
    n = 5
    calculate_series(n)
    print(f"Result for {n} terms: {global_result}")

import math

if __name__ == "__main__":
    main()
