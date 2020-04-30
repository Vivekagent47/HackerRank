
# Enter your code here. Read input from STDIN. Print output to STDOUT
no_subs,no_ids = map(int, input().split())
sheet = list()

for i in range(no_ids):
    temp = list(map(float, input().split()))
    sheet.append(temp)

for i in zip(*sheet):
    avg = sum(i)/len(i)
    print(avg)