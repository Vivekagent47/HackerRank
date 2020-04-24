def minion_game(s):
    n = len(s)
    # print(lst)
    kevin = 0
    stuart = 0
    for sub in range(n):
        # print(s[sub])
        if s[sub] == "A" or s[sub] == "E" or s[sub] == "I" or s[sub] == "O" or s[sub] == "U":
            kevin = kevin + (len(s)-sub)
        else :
            stuart = stuart + (len(s)-sub)
    # print(kevin,stuart)
    if kevin > stuart:
        print("Kevin",kevin)
    elif kevin == stuart:
        print("Draw")
    else:
        print("Stuart",stuart)
    
if __name__ == '__main__':
    s = input()
    minion_game(s)