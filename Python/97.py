# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

i = input()

match = re.search(r"([0-9a-zA-Z])\1+", i)

if match:
    print(match.group(1))
else:
    print(-1)