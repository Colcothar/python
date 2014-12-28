class Fib:
    
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

limit=int(input("Please enter the range for Fibonacci series\n"))

for n in Fib(limit):
	print(n, end=' ')
print("\n")
