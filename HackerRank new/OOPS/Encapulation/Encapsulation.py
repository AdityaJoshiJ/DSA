class Number:
    def __init__(self):
        self.n = int(input())
        self._sumofn()
        # self.__perfact()

    def _sumofn(self):
        s = 0
        for i in range(1, self.n+1):
            s = s + i

        i += 1
        print("sum is :", s)

    def __perfact(self):
        print("yes")


obj = Number()
