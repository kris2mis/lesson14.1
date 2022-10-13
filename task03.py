# 5 = 5 * 4 * 3 * 2 * 1
# f(5!) = 5 * f(4!)
# f(4!) = 3 * f(3!)
# ...
# f(0!)= 1

def factorial(number):
    if number <= 1:
        return 1

    return number * factorial(number - 1)
