import operator

class MathEngine():
    def __init__(self):
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '%': operator.mod,
            '^': operator.pow,
            # '.': operator.
        }

    def calculate(self, a: str, opr: str, b: str):
        try:
            valA, valB = float(a), float(b)
            func = self.operations.get(opr)

            if func: return func(valA, valB)
            else: return "ERROR"
        except: return "ERROR"