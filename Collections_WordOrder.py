# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
words= {}
count = 0

for i in range(N):
    word = input()
    if word not in words:
        count += 1
        words[word] = 1

    elif word in words:
        words[word] += 1
         
print(count)
print(" ".join(str(words[i]) for i in words))