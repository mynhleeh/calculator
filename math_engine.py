import operator

class MathEngine():
    def __init__(self):
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '%': operator.mod,
            '^': operator.pow
        }

    @staticmethod
    def format_result(value: float):
        return int(value) if value.is_integer() else value

    def calculate(self, a: str, opr: str, b: str):
        valA, valB = float(a), float(b)
        func = self.operations.get(opr)

        if func: return self.format_result(func(valA, valB))
        return "ERROR"