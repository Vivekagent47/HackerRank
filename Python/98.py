# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
REGEX = '(?<=[' + CONSONANTS + '])([' + VOWELS + ']{2,})[' + CONSONANTS + ']'

match = re.findall(REGEX, s, re.IGNORECASE)
if match:
    print(*match, sep='\n')
else:
    print('-1')
