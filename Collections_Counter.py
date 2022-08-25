# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input())
Sizes = Counter(map(int,input().split()))
N = int(input())
Revenue = 0

for person in range(N):
    s, Xi = map(int,input().split())
    if s in Sizes and Sizes[s] > 0:
        Sizes[s] = Sizes[s] - 1
        Revenue = Revenue + Xi
            
print(Revenue)
