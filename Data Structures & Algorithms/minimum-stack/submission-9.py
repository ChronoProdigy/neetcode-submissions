class MinStack:

    def __init__(self):
        self._items = []
        self._min = 2147483649
        self._minStack = []

    def push(self, val: int) -> None:
        self._items.append(val)
        if val < self._min:
            self._min = val
        self._minStack.append(self._min)

    def pop(self) -> None:
        self._minStack.pop()
        if len(self._minStack) > 0:
            self._min = self._minStack[-1]
        elif len(self._minStack) == 0:
            self._min = 2147483649
        return self._items.pop()

    def top(self) -> int:
        return self._items[-1]

    def getMin(self) -> int:
        return self._min