class ListNode:

    def __init__(self, url: str, prev: 'ListNode | None' = None, next: 'ListNode | None' = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr_page = ListNode(url=homepage)

    def visit(self, url: str) -> None:
        new_page = ListNode(url=url, prev=self.curr_page)
        self.curr_page.next = new_page
        self.curr_page = new_page

    def back(self, steps: int) -> str:
        while self.curr_page.prev and steps > 0:
            self.curr_page = self.curr_page.prev
            steps -= 1
        return self.curr_page.url


    def forward(self, steps: int) -> str:
        while self.curr_page.next and steps > 0:
            self.curr_page = self.curr_page.next
            steps -= 1
        return self.curr_page.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)