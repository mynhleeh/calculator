from math_engine import MathEngine
from ui import CalculatorView
from abc import ABC, abstractmethod

class CalcState(ABC):
    @abstractmethod
    def handle_number(self, context, num: str): pass

    @abstractmethod
    def handle_operator(self, context, opr: str): pass

    @abstractmethod
    def handle_equal(self, context): pass

    @abstractmethod
    def handle_backspace(self, context): pass


class InitState(CalcState):
    def handle_number(self, context, num):
        if context.cur == '0':
            if num == '.': context.cur += num
            else: context.cur = num 
        elif '.' not in context.cur: context.cur += num
        elif '.' in context.cur and num != '.': context.cur += num
        
        context.updateUI(context.cur)

    def handle_operator(self, context, op: str):
        if op == '-' and context.cur == '0':
            context.cur = '-'
            context.updateUI(context.cur)

        else:
            context.pre = context.cur
            context.opr = op
            context.cur = ""
            context.change_state(OperatorState())
            context.updateUI(f"{context.pre}{context.opr}")

    def handle_equal(self, context): pass
    def handle_backspace(self, context): pass


class OperatorState(CalcState):
    def handle_number(self, context, num):
        context.cur += num
        context.change_state(TypingState())
        context.updateUI(f"{context.pre}{context.opr}{context.cur}")

    def handle_operator(self, context, opr: str):
        context.opr = opr
        context.updateUI(f"{context.pre}{context.opr}")

    def handle_equal(self, context):
        context.updateUI("ERROR")

    def handle_backspace(self, context):
        context.cur = context.pre
        context.pre = ""
        context.opr = ""

        context.change_state(InitState()) 
        context.updateUI(context.cur)


class TypingState(CalcState):
    def handle_number(self, context, num):
        if num == '.':
            if not context.cur: context.cur = "0."
            elif '.' in context.cur: pass
            else: context.cur += num
        else: context.cur += num

        context.updateUI(context.cur)
        context.updateUI(f"{context.pre}{context.opr}{context.cur}")

    def handle_operator(self, context, opr: str):
        result = context.engine.calculate(context.pre, context.opr, context.cur)

        if result == "ERROR":
            context.pre, context.opr, context.cur = "", "", result
            context.change_state(ErrorState)
            context.updateUI(context.cur)

        else:
            context.pre = result
            context.opr = opr
            context.cur = ""
            context.updateUI(f"{context.pre}{context.opr}")

    def handle_equal(self, context):
        result = context.engine.calculate(context.pre, context.opr, context.cur)

        if result == "ERROR":
            context.pre, context.opr, context.cur = "", "", result
            context.last_opr, context.last_val = "", ""
            
            context.change_state(ErrorState)
            context.updateUI(context.cur)

        else:
            context.last_opr = context.opr
            context.last_val = context.cur

            context.pre = ""
            context.opr = ""
            context.cur = str(result)
            
            context.change_state(ResultState())
            context.updateUI(str(result))

    def handle_backspace(self, context):
        if len(context.cur) > 1: context.cur = context.cur[:-1]
        else: context.cur = "0"

        context.updateUI(f"{context.pre}{context.opr}{context.cur}")


class ResultState(CalcState):
    def handle_number(self, context, num):
        context.pre = ""
        context.opr = ""
        context.cur = num
        
        context.change_state(InitState())
        context.updateUI(context.cur)

    def handle_operator(self, context, opr: str):
        context.pre = context.cur
        context.opr = opr
        context.cur = ""
        
        context.change_state(OperatorState())
        context.updateUI(f"{context.pre}{context.opr}")

    def handle_equal(self, context):
        if context.last_opr and context.last_val:
            result = context.engine.calculate(context.cur, context.last_opr, context.last_val)
            
            context.cur = str(result)
            context.updateUI(context.cur)
    
    def handle_backspace(self, context): pass


class ErrorState(CalcState):
    def handle_number(self, context, num):
        context.pre, context.opr, context.cur = "", "", num
        context.change_state(ErrorState)
        context.updateUI(context.cur)

    def handle_operator(self, context, opr): pass
    def handle_equal(self, context): pass
    def handle_backspace(self, context): pass


class CalculatorControl:
    def __init__(self):
        self.engine = MathEngine()
        self.view = CalculatorView(action_callback=self.handle_input)

        self.state: CalcState = InitState()
        self.pre, self.opr, self.cur = "", "", "0"
        self.last_opr, self.last_val = "", ""

        self.updateUI("0")

    def change_state(self, new_state: CalcState):
        self.state = new_state

    def updateUI(self, text: str):
        self.view.update_screen(text)

    def handle_input(self, char: str):
        if char == 'C':
            self.pre, self.opr, self.cur = "", "", "0"
            self.change_state(InitState())
            self.updateUI("0")

        elif char in '0123456789.': self.state.handle_number(self, char)
        elif char in "+-*/%^":  self.state.handle_operator(self, char)
        elif char == '=': self.state.handle_equal(self)
        elif char == '⌫': self.state.handle_backspace(self)

    def run(self):
        self.view.run()

if __name__ == '__main__':
    app = CalculatorControl()
    app.run()