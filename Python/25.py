import string

def print_rangoli(size):
    # your code goes here
    letter = string.ascii_lowercase
    pattern = []
    for i in range(0,size):
        s = "-".join(letter[i:n])
        pattern.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(pattern[:0:-1]+pattern))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)