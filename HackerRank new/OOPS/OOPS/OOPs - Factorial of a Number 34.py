class factorial:
    def __init__(self):
        self.n = int(input())

        def facto(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n*facto(n-1)

        fa = facto(self.n)
        print(fa)


f = factorial()
