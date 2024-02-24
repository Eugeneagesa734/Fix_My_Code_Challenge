#!/usr/bin/python3

"""
FizzBuzz
Logic shift in the event that (i % 3) == 0 and (i % 5) == 0:
    """
import sys

def fizzbuzz(n):
    """
    Fizzbuzz function to output numbers between 1 and n, with space appart.

    - Print "Fizz" in place of the number for multiples of three, and "Buzz" in place of the number for multiples of five.

    - Print "FizzBuzz" for numbers that are multiples of three and five.

    """
if n < 1:
    return

tmp_result = []
for i in range(1, n + 1):
    if (i % 3) == 0 and (i % 5) == 0:
        tmp_result.append("FIZZbUZZ")
    elif (i % 3) == 0:
        tmp_result.append("FIZZ")
    elif (i % 5) == 0:
        tmp_result.append("buzz")
    else:
        tmp_result.append(str(i))
        print(" ".join(tmp_result))

        if __name__ == '__main__':
            if len(sys.arvg) <= 1:
                print("Missing number")
                print("Usage: ./0-fizzbuzz.py .<number>")
                print("Example: ./0-fizzbuzz.py 89")
                sys.exit(1)

                number = int(sys.argv[1])
                fizzbuzz(number)


