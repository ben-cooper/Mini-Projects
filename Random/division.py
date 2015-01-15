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


def acc_add(x, y):
    '''(str, str) -> str
    Return the exact sum of x and y as a string.
    REQ x and y must be numeric and contain a decimal point
    >>> acc_add('0.3264387246', '20.9290482536')
    '21.2554869782'
    '''
    #checking if the input is valid
    allowed_chars = ({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'})
    if set(x).issubset(
            allowed_chars) and set(
                y).issubset(allowed_chars) and (
                    x.count('.') == 1) and y.count(
                        '.') == 1 and x[0] != '.' and y[0] != '.':
        #in order for this to work they must both be the same length
        #so we add zeros until they are the same length
        while len(x[x.index('.')+1:]) < len(y[y.index('.')+1:]):
            x += '0'
        while len(y[y.index('.')+1:]) < len(x[x.index('.')+1:]):
            y += '0'
        #we remove the decimal point to get very large numbers and
        #then we add them
        first_part = int(x[:x.index('.')]) + int(y[:y.index('.')])
        last_part = int(x[x.index('.')+1:]) + int(y[y.index('.')+1:])
        #carrying the one if necessary
        if len(str(last_part)) > len(x[x.index('.')+1:]):
            first_part += 1
            last_part = int(str(last_part)[1:])
        output = str(first_part) + '.' + str(last_part)
    else:
        output = 'Please make sure strings follow format!'
    return output


def acc_mul(x, y, prec):
    '''(str, srt, int) -> str
    Return the exact product of x and y as a string
    REQ x and y must be numeric and contain a decimal point
    >>> acc_mul("42.34274872342832478", "3.32847293842420", 9)
    '140.936693264'
    '''
    #setting the default error message
    result = "Please enter nnumeric strings with a single decimal point \
(eg. '3.0')"
    #checking if the input is valid
    allowed_chars = ({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'})
    if set(x).issubset(
            allowed_chars) and set(
                y).issubset(allowed_chars) and (
                    x.count('.') == 1) and y.count(
                        '.') == 1 and x[0] != '.' and y[0] != '.':
        #first we must convert the numbers into fractions
        #to do this we will need to multiply by a power of ten in order to
        #remove the decimal point
        magx = len(x[x.index('.')+1:])
        magy = len(y[y.index('.')+1:])
        #calculating the product of the numerator
        product = str((int(x.replace('.', '')) * int(y.replace('.', ''))))
        #adding the decimal point back in place
        result = product[:-(magx + magy)] + '.' + product[-(magx+magy):][:prec]
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
