from math_engine import MathEngine
from ui import Calculator

if __name__ == '__main__':
    engine = MathEngine()
    app = Calculator(engine)
    app.run()