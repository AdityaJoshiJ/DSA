from abc import ABC, abstractmethod


class AbstractCallme(ABC):

    def __init__(self, input1, input2, input3):
        self.input1 = input1
        self.input2 = input2
        self.input3 = input3

    @abstractmethod
    def callme(self, operationString, position, result, input3, prevResult):
        pass

    def run(self):
        result = self.callme(self.input2, 0, self.input1, self.input3, "")
        print(result)


class ConcreteCallme(AbstractCallme):

    def callme(self, operationString, position, result, input3, prevResult):
        if position >= len(operationString):
            return result
        else:
            char = operationString[position]
            if char == 'w':
                prevResult = result
                result = self.callme(
                    operationString, position + 1, result, input3, prevResult)
            elif char == 'd':
                prevResult = result
                result = result[:-input3]
                result = self.callme(
                    operationString, position + 1, result, input3, prevResult)
            elif char == 'u':
                result = self.callme(
                    operationString, position + 1, prevResult, input3, result)
            else:
                result = result + char
                result = self.callme(
                    operationString, position + 1, result, input3, prevResult)
        return result


obj = ConcreteCallme(input(), input(), int(input()))
obj.run()
