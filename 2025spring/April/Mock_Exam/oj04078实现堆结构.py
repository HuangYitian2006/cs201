class BinaryHeap:
    def __init__(self):
        self.heap=[]

    def _perc_up(self,i):
        while (i-1)//2>=0:
            parent=(i-1)//2
            if self.heap[i]<self.heap[parent]:
                self.heap[i],self.heap[parent]=self.heap[parent],self.heap[i]
            i=parent

    def insert(self,item):
        self.heap.append(item)
        self._perc_up(len(self.heap)-1)

    def delete(self):
        self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
        result=self.heap.pop()
        self._perc_down(0)
        return result

    def _get_min_child(self,i):
        if i*2+2>len(self.heap)-1:
            return i*2+1
        return i*2+1 if self.heap[i*2+1]<self.heap[i*2+2] else i*2+2

    def _perc_down(self,i):
        while i*2+1<len(self.heap):
            min_child=self._get_min_child(i)
            if self.heap[i]>self.heap[min_child]:
                self.heap[i],self.heap[min_child]=self.heap[min_child],self.heap[i]
            else: break
            i=min_child

    def heapify(self,alist):
        self.heap=alist.copy()
        i = len(self.heap) // 2 - 1
        while i >= 0:
            self._perc_down(i)
            i = i - 1



n=int(input().strip())
b=BinaryHeap()
for _ in range(n):
    x=input().strip()
    if x[0]=='2':
        print(b.delete())
    else:
        b.insert(int(x.split()[1]))