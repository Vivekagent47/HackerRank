# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for i in range(n):
    try:
        a, b = map(int,input().split())
        div = a//b
        print(div)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)