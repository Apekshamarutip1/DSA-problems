def maxsub(s):
    max_sofar=s[0]
    cur_max=s[0]
    
    for i in range(1,len(s)):
        cur_max=max(s[i],cur_max+s[i])
        max_sofar=max(max_sofar,cur_max)
    return max_sofar    
    
for _ in range(int(input())):
    n=input()
    s=list(map(int, input().split()))
    print(maxsub(s))