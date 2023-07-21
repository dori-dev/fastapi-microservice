class Fibonacci:
    def __init__(self):
        self.memo = {}

    def __call__(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 1:
            self.memo[n] = n
        else:
            self.memo[n] = self(n - 1) + self(n - 2)
        return self.memo[n]


fib = Fibonacci()
