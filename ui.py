import customtkinter as ctk
from math_engine import MathEngine
import re

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue") 

class Calculator:
    def __init__(self, engine):
        self.engine = engine
        
        # Window
        self.root = ctk.CTk()
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.display_var = ctk.StringVar(value="")

        # UI
        self.setupUI()

    def setupUI(self):
        # Auto resize
        for i in range(5): self.root.grid_rowconfigure(i, weight=1)
        for i in range(4): self.root.grid_columnconfigure(i, weight=1)

        # Screen
        self.screen = ctk.CTkEntry(
            self.root, 
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            height=50
        )
        self.screen.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]
        row_val, col_val = 1, 0

        for button in buttons:
            btn = ctk.CTkButton(
                self.root,
                text=button,
                command=lambda x=button: self.on_click(x),
                width=50, 
                height=50)
            btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
            
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_click(self, char):
        current_val = self.display_var.get()

        if char == 'C': self.display_var.set("")
        elif char == '=':
            try:
                parts = re.split(r'(\+|-|\*|/|x)', current_val)
                
                if len(parts) == 3:
                    a, opr, b = parts
                    result = self.engine.calculate(a, opr, b)
                    self.display_var.set(str(result))
                else: self.display_var.set("ERROR")
            except Exception: self.display_var.set("ERROR")

        else: self.display_var.set(current_val + char)

    def run(self):
        self.root.mainloop()