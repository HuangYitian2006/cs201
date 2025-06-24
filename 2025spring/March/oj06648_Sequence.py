import heapq

for _ in range(int(input())):
    m,n=map(int,input().split())
    seq1=sorted(map(int,input().split())) #seq1存储最小的n个和
    for i in range(m-1):
        seq2=sorted(map(int,input().split()))
        min_heap=[(seq1[i]+seq2[0],i,0)for i in range(n)]
        heapq.heapify(min_heap)
        result=[]
        for _ in range(n):
            cur_sum,i,j=heapq.heappop(min_heap) #i,j为seq1，seq2所取的数的坐标
            result.append(cur_sum)
            if j+1<n: #换成下一个数！
                heapq.heappush(min_heap,(seq1[i]+seq2[j+1],i,j+1))
        seq1=result
    print(*seq1)

