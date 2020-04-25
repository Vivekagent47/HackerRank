# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

angle = str(int(round(math.degrees(math.atan2(AB,BC)))))+"°"

print(angle)