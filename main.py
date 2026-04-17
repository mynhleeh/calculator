from math_engine import MathEngine
from ui import View

class calculate_cotrol:
    def __init__(self):
        self.engine = MathEngine()
        self.view = View(action_callback=self.handle_input)

        self.cur, self.pre, self.opr = "", "", ""


    def handle_input(self, char: str):
        current_val = self.view.display_var.get()

        if char == 'C': self.view.update_screen("")
        elif char == '=':
            if self.cur and self.pre and self.opr:
                result = self.engine.calculate(self.pre, self.opr, self.cur)
                self.view.update_screen(str(result))

            else: self.view.update_screen("ERROR")

        elif char in ['+', '-', '*', '/']:
            self.view.update_screen(current_val + char)

            if self.cur:
                self.pre, self.opr, self.cur = self.cur, char, ""
        else: 
            self.cur += char
            self.view.update_screen(current_val + char)

    def run(self):
        self.view.run()

if __name__ == '__main__':
    app = calculate_cotrol()
    app.run()