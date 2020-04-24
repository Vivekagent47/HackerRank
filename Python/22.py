n, m = map(int,input().split())
for j in range (n//2):
    pattern = ('.|.'*(2*j + 1)).center(m, '-')
    print(pattern)

note = ('WELCOME').center(m,'-')
print(note)

for j in range (n//2,0,-1):
    pattern = ('.|.'*(2*j - 1)).center(m, '-')
    print(pattern)
