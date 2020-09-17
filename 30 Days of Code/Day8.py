# Enter your code here. Read input from STDIN. Print output to STDOUT

phone_book = dict()

for _ in range(int(input())):
    temp = list(map(str, input().split()))
    phone_book[temp[0]] = temp[1]

while True:
    try:
        name = input()
        if name in phone_book:
            print(name, "=", phone_book[name], sep="")
        else : 
            print("Not found")   
    except: 
        break
