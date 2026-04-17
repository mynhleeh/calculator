class MathEngine():
    @staticmethod
    def parse(val):
        try: return int(val)
        except ValueError:
            try: return float(val)
            except: raise "ERROR"
    
    @staticmethod
    def calculate(a, opr: str, b):
        valA = MathEngine.parse(a)
        valB = MathEngine.parse(b)

        if opr == '+': return valA + valB
        if opr == '-': return valA - valB
        if opr == '*' or opr == 'x': return valA * valB
        if opr == '/': return valA / valB if valB != 0 else "ERROR"
        return "ERROR"
    

if __name__ == '__main__':
    a, opr, b = input().split()
    print(MathEngine.calculate(a, opr, b))