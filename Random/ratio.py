class rational():
    def __init__(self, numerator, denominator):
        self._denom = denominator
        self._numer = numerator

    def __repr__(self):
        return repr(self._numer) + '/' + repr(self._denom)

    def __add__(self, other):
        if isinstance(other, int):
            other = rational(other, 1)
        if self._numer == 0:
            return other
        new_nume = (int(self._numer) * int(other._denom) +
                    int(other._numer) * int(self._denom))
        new_deno = self._denom * other._denom
        return rational(new_nume, new_deno)

    def __sub__(self, other):
        return self + other * -1

    def __mul__(self, other):
        if isinstance(other, int):
            other = rational(other, 1)
        return rational(self._numer * other._numer, self._denom * other._denom)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = rational(other, 1)
        return self * rational(other._denom, other._numer)


def acc_div(x, y, prec):
    '''(float, float, int) -> str
    Return the quotient of x and y (x /y) with prec number of decimal places.
    >>> acc_div(5, 7, 32)
    '0.71428571428571428571428571428571'
    '''
    #computing digits before decimal point
    output = str(int(x // y)) + '.'
    #computing digits after decimal point
    for i in range(1, prec+1):
        output += str((10**(i-1)*x % y)/y)[2]
    return output


def factorial(n):
    '''
    (int) -> int
    Return the factorial of n
    >>> factorial(4)
    24
    '''
    return 1 if n <= 1 else n * factorial(n-1)


def compute_pi(n):
    '''
    (int) -> str
    Return a string representation of the approximation of pi calculated after
    n terms
    REQ n >= 1
    '''
    #initializing
    result = rational(0, 0)
    for i in range(0, 2*n, 2):
        numerator = 4 * (-1) ** (i/2)
        denominator = (2+i) * (3+i) * (4+i)
        result += rational(numerator, denominator)
    return result + 3

if __name__ == '__main__':
    x = compute_pi(1000)
    print(acc_div(x._numer, x._denom, 30))
