# design a browser history system
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Browser:
    
    def __init__(self, homepage: str):
        self.homepage = Node(homepage)

    def visit(self, url: str) -> None:
        # Discard all forward history
        new_node = Node(url)
        self.homepage.next = new_node
        new_node.prev = self.homepage
        self.homepage = new_node

    def back(self, steps: int) -> str:
        while steps:
            if self.homepage.prev:
                self.homepage = self.homepage.prev
            else:
                break
            steps -= 1
        return self.homepage.data

    def forward(self, steps: int) -> str:
        while steps:
            if self.homepage.next is None:
                break
            self.homepage = self.homepage.next
            steps -= 1
        return self.homepage.data
def main():
    browserHistory = Browser("leetcode.com")
    browserHistory.visit("google.com")       # You are in "leetcode.com". Visit "google.com"
    browserHistory.visit("facebook.com")     # You are in "google.com". Visit "facebook.com"
    browserHistory.visit("youtube.com")      # You are in "facebook.com". Visit "youtube.com"
    print(browserHistory.back(1))            # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    print(browserHistory.back(1))            # You are in "facebook.com", move back to "google.com" return "google.com"
    print(browserHistory.forward(1))         # You are in "google.com", move forward to "facebook.com" return "facebook.com"
    browserHistory.visit("linkedin.com")     # You are in "facebook.com". Visit "linkedin.com"
    print(browserHistory.forward(2))         # You are in "linkedin.com", you cannot move forward any steps.
    print(browserHistory.back(2))            # You are in "linkedin.com", move back two steps to "google.com" return "google.com"
    print(browserHistory.back(7))            # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

if __name__ == "__main__":
    main()

