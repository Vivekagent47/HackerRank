import datetime
case = int(input())
for i in range(case):
    first = input().strip()
    second = input().strip()
    time_format = "%a %d %b %Y %H:%M:%S %z"
    time_sec1 = datetime.datetime.strptime(first,time_format)
    time_sec2 = datetime.datetime.strptime(second,time_format)
    # print(time_sec1)
    # print(time_sec2)
    print(int(abs((time_sec1-time_sec2).total_seconds())))