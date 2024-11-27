import math

def is_perfect_square(num):
    root = math.isqrt(num)  # integer square root
    return root * root == num

def factors(i):
    ar = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            ar.append(j)
    return ar

def square_free(i):
    factors_list = factors(i)
    sf = []
    perfect_squares = []
    
    for factor in factors_list:
        if is_perfect_square(factor):
            perfect_squares.append(factor)
    
    for factor in factors_list:
        divisible_by_perfect_square = False
        for square in perfect_squares:
            if factor % square == 0:
                divisible_by_perfect_square = True
                break
        if not divisible_by_perfect_square:
            sf.append(factor)
    
    return sf

def main():
    i = int(input("Enter a number which is not divisible by a prime number greater than 19: "))
    
    result = square_free(i)
    
    if result:
        print("Square-free factors:", " ".join(map(str, result)))
    else:
        print("No square-free factors found.")

if __name__ == "__main__":
    main()
