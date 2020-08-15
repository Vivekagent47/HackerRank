#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.

def acmTeam(n, m, topic):
    maxKnown = 0
    teams = 0
    for i in range(n-1): 
        for j in range(i+1, n):
            known_topics = 0
            for t in range(m):
                if topic[i][t] == '1' or topic[j][t] == '1':
                    known_topics += 1

            if known_topics > maxKnown:
                maxKnown = known_topics
                teams = 1
            elif known_topics == maxKnown:
                teams += 1
     
    return maxKnown, teams


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)
    result = acmTeam(n, m, topic)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
    
