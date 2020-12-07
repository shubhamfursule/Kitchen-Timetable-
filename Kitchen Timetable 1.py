
T=int(input())
for i in range(0,T+1):
    count=0
    sub=0
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    if B[0]<=A[0]:
        count+=1
    for j in range(1,N):
            
        if B[j]<=A[j]-A[j-1]:
            count+=1
            print(count)