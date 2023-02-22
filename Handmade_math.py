def factorial(x):  # recursive calculation of factorial
    if x < 0:
        raise Exception("Sorry, no numbers below zero for factorials")
    if x == 0:
        return 1
    if x == 1:
        return 1
    else:
        return factorial(x-1)*x


def cos(x, n=10):  # Calculation of cos(x) using taylor series with n(default = 10) elements
    result = 0
    for i in range(0, n+1):
        result += ((-1)**i) * ((x**(2*i))/(factorial(2*i)))
    return result


if __name__ == '__main__':
    print(cos(5))
