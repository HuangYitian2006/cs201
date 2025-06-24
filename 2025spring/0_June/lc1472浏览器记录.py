class Node:
    def __init__(self,url:str):
        self.val=url
        self.next=None
        self.prev=None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.now=Node(homepage)

    def visit(self, url: str) -> None:
        cur=self.now #存的是一个指针
        self.now.next=Node(url)
        self.now=self.now.next
        self.now.prev=cur

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.now.prev is not None:
                self.now=self.now.prev
            else:break
        return self.now.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.now.next is not None:
                self.now=self.now.next
            else:break
        return self.now.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)