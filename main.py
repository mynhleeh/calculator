from math_engine import MathEngine
from ui import CalculatorView

class calculate_control:
    def __init__(self):
        self.engine = MathEngine()
        self.view = CalculatorView(action_callback=self.handle_input)

        self.cur, self.pre, self.opr = "", "", ""
        self.reset_next_input = False


    def handle_input(self, char: str):
        if char == 'C':
            self.cur, self.pre, self.opr = "", "", ""
            self.reset_next_input = False
        
        elif char == 'DEL':
            if self.cur: self.cur = self.cur[:-1]
            elif self.opr: self.cur, self.pre, self.opr = self.pre, "", ""

        elif char == '=':
            if self.cur and self.pre and self.opr:
                result = self.engine.calculate(self.pre, self.opr, self.cur)
                self.cur, self.pre, self.opr = str(result), "", ""
                self.reset_next_input = True

        elif char == '.':
            if self.reset_next_input: self.cur, self.reset_next_input = "0.", False
            elif '.' not in self.cur:
                if self.cur == "": self.cur = "0."
                else: self.cur += '.'

        elif char in ['+', '-', '*', '/', '%', '^']:
            if self.pre and self.cur and self.opr:
                result = self.engine.calculate(self.pre, self.opr, self.cur)
                self.pre, self.cur, self.opr = str(result), "", char

            elif self.cur: self.pre, self.opr, self.cur = self.cur, char, ""
            elif self.pre: self.opr = char

            self.reset_next_input = False

        else:
            if self.reset_next_input: self.cur, self.reset_next_input = char, False
            else: self.cur += char

        full = f"{self.pre}{self.opr}{self.cur}"
        if full == "": self.view.update_screen("0")
        else: self.view.update_screen(full)

    def run(self):
        self.view.run()

if __name__ == '__main__':
    app = calculate_control()
    app.run()