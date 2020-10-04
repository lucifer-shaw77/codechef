t=int(input())
for _ in range(t):
    N=int(input())
    A=list(map(int,input().split()))
    count=0
    temp=-1
    A.sort()
    for i in range(N):
        if(A[i]!=0 and A[i]!=temp):
            count+=1
            temp=A[i]
    print(count)