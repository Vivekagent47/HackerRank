#Write your code here
class Calculator():
    def power(self, n, p):
        if p >= 0 and n >= 0:
            return n**p
        else:
            return "n and p should be non-negative"

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   