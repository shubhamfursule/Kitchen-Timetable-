T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    A=[0]+A
    B=list(map(int,input().split()))
    count=0
    for j in range(N):
        if B[j]<=A[j+1]-A[j]:
            count+=1
    print(count)
