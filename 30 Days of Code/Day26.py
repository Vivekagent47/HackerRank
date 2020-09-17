# Enter your code here. Read input from STDIN. Print output to STDOUT
rd, rm, ry = map(int, input().split())
ed,em, ey = map(int, input().split())

if (ry, rm, rd) <= (ey, em, ed):
    print(0)
elif (ry, rm) == (ey, em):
    print(15 * (rd - ed))
elif ry == ey:
    print(500 * (rm - em))
else:
    print(10000)