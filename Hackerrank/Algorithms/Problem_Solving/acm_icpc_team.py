# Problem Statement : https://www.hackerrank.com/challenges/acm-icpc-team

import itertools
N,M = map(int,raw_input().strip().split())
knowledge=[]
for i in range(N):
    knowledge.append(int(raw_input(),2))
mx = -float('inf')
teams=0
for p1,p2 in itertools.combinations(range(N),2):
    combined_topics = bin(knowledge[p1]|knowledge[p2]).count('1')
    if (combined_topics==mx):
        teams+=1
    elif (combined_topics>mx):
        mx = combined_topics
        teams=1

print(mx)
#print('\n')
print(teams)
