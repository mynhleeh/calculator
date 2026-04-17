class MathEngine():    
    @staticmethod
    def calculate(a: str, opr: str, b: str):
        try:
            valA, valB = float(a), float(b)

            if opr == '+': return valA + valB
            if opr == '-': return valA - valB
            if opr == '*' or opr == 'x': return valA * valB
            if opr == '/': return valA / valB
        except:
            return "ERROR"
    

if __name__ == '__main__':
    a, opr, b = input().split()
    print(MathEngine.calculate(a, opr, b))