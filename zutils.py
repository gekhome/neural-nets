import math
import string

def stat_range(data):
    '''
    Computes range of data values
    '''
    sorted_data = sorted(data)
    return sorted_data[-1] - sorted_data[0]


def stat_mean(data):
    '''
    Computes the average value of data values
    '''
    return sum(data) / len(data)


def stat_std(data):
    '''
    Computes the standard deviation of data values
    '''
    sigma = 0
    mean = stat_mean(data)
    N = len(data)
    for x in data:
        sigma += (x - mean)**2
    sigma = math.sqrt(sigma/N)
    return sigma


def describe(data):
    '''
    Decribes data values by computing the range, mean
    standard deviation, minimum and maximum values
    Prints the results
    '''
    rng = stat_range(data)
    mean = stat_mean(data)
    std = stat_std(data)
    min_val = min(data)
    max_val = max(data)
    print('-'*20)
    print(f'Range:  {rng}')
    print(f'Mean :  {mean:.2f}')
    print(f'Std  :  {std:.2f}')
    print(f'Min  :  {min_val}')
    print(f'Max  :  {max_val}')
    print('-'*20)


def is_palindrome(s):
    '''
    Checks if passed string is a palindrome
    '''
    return s == s[::-1]


def gcd(a, b):
    """
    Uses Euclid's method to compute the greatest common divisor
    of m and n.
    Returns the GCD of m and n.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# use hints for types of variables
# input is int and return value int
def sum_digits(number:int) -> int:
    '''
    Sums the digits of an integer number
    '''
    if not isinstance(number, int):
        raise TypeError('Argument must be an integer.')
    
    return sum([int(c) for c in str(number)])


def print_header(title):
    print('+' + '-'*(len(title)+2) + '+')
    print('| ' + title + ' |')
    print('+' + '-'*(len(title)+2) + '+')
    print()

    
def zpad(num:int, n=2) -> str:
    '''
    Left pad a number with zeros up to length n
    Returns the number as padded string
    '''
    m = len(str(num))
    if m < n:
        return '0'*(n - m) + str(num)
    return str(num)

def hr(length=40):
    print('-'*length)

    
def count_words(file_handle, decode_it=False):
    '''
    Counts the words of a file handle
    Returns a dictionary with the histogram of the words
    '''
    counts = dict()
    for line in file_handle:
        if decode_it: 
            line = line.decode()
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    return counts