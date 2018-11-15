import queue


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = queue.Queue()
        self.qt = queue.Queue()
        self.topv=None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        while self.q.qsize() > 0:
            self.qt.put(self.q.get_nowait())
        self.q.put(x)
        self.topv=x
        while self.qt.qsize() > 0:
            self.q.put(self.qt.get_nowait())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.get_nowait()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.topv

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q.empty()

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(1);
obj.push(2);
a=obj.top();
b=obj.pop();
c=obj.empty();
print()

