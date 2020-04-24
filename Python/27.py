
def merge_the_tools(string, k):
    for s in range(0,len(string),k):
        sub_string = string[s:k+s]
        sub_letter = [sub_string[i] for i in range(len(sub_string))]
        modify = []
        for i in sub_letter: 
            if i not in modify: 
                modify.append(i)
        for i in range(len(modify)):
            print(modify[i],end="")
        print()
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)